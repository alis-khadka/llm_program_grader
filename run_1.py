import os
import json
import torch
import re
import traceback
from natsort import natsorted

# from database import init_db, get_or_create, SessionLocal
# from models import Grade, StudentSubmission, Question

WORK_CACHE_PATH = '/work/pkhadk2/.cache'
os.makedirs(WORK_CACHE_PATH, exist_ok=True)
os.environ['HF_HOME'] = WORK_CACHE_PATH

PROJECT_ROOT = os.getcwd()
DATASET_PATH = "./dataset/"
SOLUTIONS_PATH = DATASET_PATH + "solutions/"

MAX_TOKENS=8192

FUNCTIONALITY = """
You are an expert programmer tasked with evaluating the functionality of a student's code submission for a programming assignment. Below is the assignment question and the student's code. Please follow these steps:

1. Analyze whether the code produces correct outputs for the given problem.
2. Test the code against a variety of standard and edge-case inputs (you may assume reasonable test cases for the problem).
3. Identify any logical errors, missing functionality, or unhandled edge cases.
4. Provide feedack that identitfies specififc issues and suggests improvements.

Finally, assign a grade (out of 10) for functionality based on how well the code meets the assignment's requirements.

Provide your response in JSON format only with short bullet points for analysis, and a final score with no improved code in json format only with keys : analysis, test_cases, final_score.
"""
CODE_QUALITY = """
You are an expert programmer tasked with evaluating the quality of a student's code. Below is the assignment question and the student's code, and the functionality evaluation from the previous step. Please follow these steps:

1. Assess the readability of the code, including variable names, comments, and logical organization.
2. Evaluate whether the code follows best practices, such as modularity, avoiding redundancy, and proper use of structures.
3. Analyze the maintainability of the code -- whether it would be easy for someone else to understand and modify.
4. Provide actionable feedback on how the student can improve the quality of their code.

Finally, assign a grade (out of 10) for code quality.

Provide your analysis in short bullet points and a final score with no improved code in json format only with keys : analysis, final_score.
"""
ALGORITHMIC_EFFICIENCY = """
You are an expert programmer tasked with evaluating the algorithmic efficiency of a student's code submission. Below is the assignment question, the student's code, the responses from the functionality and code quality evaluations from previous steps. Please follow these steps:

1. Analyze the time and space complexity of the code.
2. Identify any inefficiencies or performance bottlenecks in the implementation.
3. Suggest specific iptimizations, such as improving algorithms, restructuring loops, or using more efficient data structures.
4. Provide constructive feedback on how the student can improve the efficience of their code (if needed).

Finally, assign a grade (out of 10) for algorithmic efficiency.

Provide your analysis in short bullet points and a final score with no improved code in json format only with keys : analysis, final_score.
"""

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# # Initialize DB and tables
# init_db()

# # Create a new session
# session = SessionLocal()

# Load tasks and tests json file
task_file = os.path.join(PROJECT_ROOT, DATASET_PATH, "tasks.json")
test_file = os.path.join(PROJECT_ROOT, DATASET_PATH, "tests.json")

# 32B results
results_file = os.path.join(PROJECT_ROOT, "results.json")

def build_prompt(student_code, question_description, prompt_role, prompt_prefix):
    content = f"""
{prompt_prefix}

Assignment:
{question_description}

Student's Code:
```python
{student_code}
```
"""
    return {
        "role": prompt_role,
        "content": content
    }

def get_submission_id(file_name):
    pattern = r'(.*)(?=\.py$)'
    match = re.search(pattern, file_name, re.DOTALL)
    name = match.group(1)
    return name


def extract_json(text):
    try:
        string = re.sub("^(.*)(\n?)```json(\n?)(?={)", '', text, flags=re.S | re.M)
        json_str = re.sub("(?<=})(\n*)```(\n*)$", '', string, flags=re.S | re.M)
        # Removing comments if present
        json_str = re.sub("\s\s\/\/(.*)(?=\n)", "", json_str, flags=re.M)
        json_str = json_str.replace('True', 'true').replace('False', 'false').replace('None', 'null')
        # if match:
        # json_str = string.group(1)
        data = json.loads(json_str)
        return data
    except Exception as e:
        print(f"---------- ERROR -------------\n\n{text}")
        raise  # rethrow the exception

def build_submission_object(functionality, code_quality, algorithm):
    functionality_json = extract_json(functionality)
    code_quality_json = extract_json(code_quality)
    algorithm_json = extract_json(algorithm)

    grade = {
        "functionality": functionality_json["final_score"],
        "code_quality": code_quality_json["final_score"],
        "algorithm": algorithm_json["final_score"]
    }

    grade["avg_score"] = (grade["functionality"] + grade["code_quality"] + grade["algorithm"]) / 3

    return {
        "model": "DeepSeek-R1-Distill-Qwen-7B",
        "analysis_functionality": functionality,
        "analysis_functionality_json": functionality_json,
        "analysis_code_quality": code_quality,
        "analysis_code_quality_json": code_quality_json,
        "analysis_algorithimic_efficency": algorithm,
        "analysis_algorithimic_efficency_json": algorithm_json,
        "grade": grade
    }

def build_assigment_desc(title, description):
    return f"""
Title: {title}

Description:
{description}
"""

with open(task_file, 'r') as file:
    task_json = json.load(file)

with open(test_file, 'r') as file:
    test_json = json.load(file)

with open(results_file, "r") as f:
    results_json = json.load(f) 

tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/DeepSeek-R1-Distill-Qwen-7B", trust_remote_code=True)
tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(
    "deepseek-ai/DeepSeek-R1-Distill-Qwen-7B",
    trust_remote_code=True,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    use_safetensors=True
).cuda()


for index, (key, value) in enumerate(task_json.items()):
    if key == "21_22-3-2-python":
        folder_name = key
        print(f"______ START: Processing Folder: {folder_name} __________\n\n")

        # Initialize question object in results

        results_json.setdefault(folder_name, {})

        folder_dir = os.path.join(PROJECT_ROOT, SOLUTIONS_PATH, folder_name)
        for index, file_name in enumerate(natsorted(os.listdir(folder_dir))):
            file_path = os.path.join(PROJECT_ROOT, SOLUTIONS_PATH, folder_name,file_name)
            try:
                # if file_name.endswith('.py') and os.path.isfile(file_path) and (index <= 11):
                if file_name.endswith('.py') and os.path.isfile(file_path) and (index > 11 and index <= 22):

                    if (get_submission_id(file_name) in results_json[folder_name]):
                        continue

                    with open(file_path, 'r') as file:
                        student_code = file.read()

                    print(f"------------- Processing file: {file_name} --------------")

                    cot_prompts = []
                    print(value)
                    # cot_prompts.append(
                    #     {
                    #         "role": "assistant",
                    #         "content": "Provide the responses in JSON format only in a concise manner."
                    #     }
                    # )
                    cot_prompts=[
                        {
                            "role":"system",
                            "content":"""
You are a programming assignment grader.
Respond _only_ with JSON object matching this schema:
{
    "analysis": array of strings,
    "test_cases": array of test_cases (input, expected, actual),
    "final_score": integer out of 10
}

Data type should be compatible with JSON but not python in the JSON object. Do not output anything else.
                            """
                        },
                        build_prompt(
                            student_code,
                            build_assigment_desc(value["title_eng"], value["description_eng"]),
                            "user",
                            FUNCTIONALITY
                        )
                    ]

                    # inputs = tokenizer.apply_chat_template(
                    #     cot_prompts,
                    #     add_generation_prompt=True,
                    #     return_tensors="pt",
                    #     padding=True,
                    #     max_length=tokenizer.model_max_length,
                    #     truncation_side="left"
                    # ).to(model.device)
                    inputs = tokenizer.apply_chat_template(
                        cot_prompts,
                        add_generation_prompt=True,
                        return_tensors="pt",
                        padding=True
                    ).to(model.device)

                    response = model.generate(
                        inputs,
                        do_sample=False,
                        max_new_tokens=MAX_TOKENS,
                        eos_token_id=tokenizer.eos_token_id,
                        pad_token_id=tokenizer.pad_token_id
                    )

                    functionality_output = tokenizer.decode(response[0][len(inputs[0]):], skip_special_tokens=True)
                    print(functionality_output)

                    # cot_prompts.append(
                    #     {
                    #         "role": "assistant",
                    #         "content": functionality_output
                    #     }
                    # )
                    # cot_prompts.append(
                    #     build_prompt(
                    #         student_code,
                    #         build_assigment_desc(value["title_eng"], value["description_eng"]),
                    #         "user",
                    #         CODE_QUALITY
                    #     )
                    # )
                    cot_prompts = [
                        {
                            "role":"system",
                            "content":"""
You are a programming assignment grader.
Respond _only_ with JSON object matching this schema:
{
    "analysis": array of strings,
    "final_score": integer out of 10
}

Data type should be compatible with JSON but not python in the JSON object. Do not output anything else.
                            """
                        },
                        build_prompt(
                            student_code,
                            build_assigment_desc(value["title_eng"], value["description_eng"]),
                            "user",
                            CODE_QUALITY
                        )
                    ]

                    # inputs = tokenizer.apply_chat_template(
                    #     cot_prompts,
                    #     add_generation_prompt=True,
                    #     return_tensors="pt",
                    #     padding=True,
                    #     max_length=tokenizer.model_max_length,
                    #     truncation_side="left"
                    # ).to(model.device)
                    inputs = tokenizer.apply_chat_template(
                        cot_prompts,
                        add_generation_prompt=True,
                        return_tensors="pt",
                        padding=True
                    ).to(model.device)

                    response = model.generate(
                        inputs,
                        do_sample=False,
                        max_new_tokens=MAX_TOKENS,
                        eos_token_id=tokenizer.eos_token_id,
                        pad_token_id=tokenizer.pad_token_id
                    )

                    code_quality_output = tokenizer.decode(response[0][len(inputs[0]):], skip_special_tokens=True)
                    print(code_quality_output)

                    # cot_prompts.append(
                    #     {
                    #         "role": "assistant",
                    #         "content": code_quality_output
                    #     }
                    # )
                    # cot_prompts.append(
                    #     build_prompt(
                    #         student_code,
                    #         build_assigment_desc(value["title_eng"], value["description_eng"]),
                    #         "user",
                    #         ALGORITHMIC_EFFICIENCY
                    #     )
                    # )
                    cot_prompts = [
                        {
                            "role":"system",
                            "content":"""
You are a programming assignment grader.
Respond _only_ with JSON object matching this schema:
{
    "analysis": array of strings,
    "final_score": integer out of 10
}

Data type should be compatible with JSON but not python in the JSON object. Do not output anything else.
                            """
                        },
                        build_prompt(
                            student_code,
                            build_assigment_desc(value["title_eng"], value["description_eng"]),
                            "user",
                            ALGORITHMIC_EFFICIENCY
                        )
                    ]

                    # inputs = tokenizer.apply_chat_template(
                    #     cot_prompts,
                    #     add_generation_prompt=True,
                    #     return_tensors="pt",
                    #     padding=True,
                    #     max_length=tokenizer.model_max_length,
                    #     truncation_side="left"
                    # ).to(model.device)
                    inputs = tokenizer.apply_chat_template(
                        cot_prompts,
                        add_generation_prompt=True,
                        return_tensors="pt",
                        padding=True
                    ).to(model.device)

                    response = model.generate(
                        inputs,
                        do_sample=False,
                        max_new_tokens=MAX_TOKENS,
                        eos_token_id=tokenizer.eos_token_id,
                        pad_token_id=tokenizer.pad_token_id
                    )

                    algorithmic_efficiency_output = tokenizer.decode(response[0][len(inputs[0]):], skip_special_tokens=True)
                    print(algorithmic_efficiency_output)

                    results_json[folder_name][get_submission_id(file_name)] = build_submission_object(
                        functionality_output,
                        code_quality_output,
                        algorithmic_efficiency_output
                    )

                    print(f"______ END: Processing Folder: {folder_name} __________ \n\n\n")

            except Exception as e:
                print(f"----------- ERROR in file: {file_name} ---------------")
                results_json[folder_name][get_submission_id(file_name)] = {
                    "status": "error"
                }
                continue


with open(results_file, "w") as f:
    json.dump(results_json, f, indent=4)

