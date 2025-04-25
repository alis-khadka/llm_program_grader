import os
import json
import re
from natsort import natsorted


PROJECT_ROOT = os.getcwd()
DATASET_PATH = "./dataset/"
SOLUTIONS_PATH = DATASET_PATH + "solutions/"
RESULTS = "./json_results/"

# Load tasks and tests json file
task_file = os.path.join(PROJECT_ROOT, DATASET_PATH, "tasks.json")
test_file = os.path.join(PROJECT_ROOT, DATASET_PATH, "tests.json")

# Load 32B and 7B results
big_model_file = os.path.join(PROJECT_ROOT, RESULTS, "32B.json")
small_model_file = os.path.join(PROJECT_ROOT, RESULTS, "7B.json")

results_file = os.path.join(PROJECT_ROOT, RESULTS, "final_result.json")
stats_file = os.path.join(PROJECT_ROOT, RESULTS, "stats.json")

def get_submission_id(file_name):
    pattern = r'(.*)(?=\.py$)'
    match = re.search(pattern, file_name, re.DOTALL)
    name = match.group(1)
    return name

def build_analysis_object(analysis):
    return {
        "functionality_json": analysis["analysis_functionality_json"],
        "code_quality_json": analysis["analysis_code_quality_json"],
        "algorithimic_efficency_json": analysis["analysis_algorithimic_efficency_json"],
        "grade": analysis["grade"]
    }
    
    # return {
    #     analysis_one["model"]: {
    #         "functionality_json": analysis_one["analysis_functionality_json"],
    #         "code_quality_json": analysis_one["analysis_code_quality_json"],
    #         "algorithimic_efficency_json": analysis_one["analysis_algorithimic_efficency_json"],
    #         "grade": analysis_one["grade"]
    #     },
    #     analysis_two["model"]: {
    #         "functionality_json": analysis_two["analysis_functionality_json"],
    #         "code_quality_json": analysis_two["analysis_code_quality_json"],
    #         "algorithimic_efficency_json": analysis_two["analysis_algorithimic_efficency_json"],
    #         "grade": analysis_two["grade"]
    #     }
    # }

with open(task_file, 'r') as file:
    task_json = json.load(file)

with open(test_file, 'r') as file:
    test_json = json.load(file)

with open(big_model_file, "r") as f:
    big_json = json.load(f) 

with open(small_model_file, "r") as f:
    small_json = json.load(f) 

with open(results_file, "r") as f:
    results_json = json.load(f) 

with open(stats_file, "r") as f:
    stats_json = json.load(f) 

for index, (key, value) in enumerate(task_json.items()):
    folder_name = key
    print(f"______ START: Processing Folder: {folder_name} __________\n\n")

    results_json.setdefault(folder_name, {})
    stats_json.setdefault(folder_name, {})

    folder_dir = os.path.join(PROJECT_ROOT, SOLUTIONS_PATH, folder_name)
    for index, file_name in enumerate(natsorted(os.listdir(folder_dir))):
        file_path = os.path.join(PROJECT_ROOT, SOLUTIONS_PATH, folder_name,file_name)

        if file_name.endswith('.py') and os.path.isfile(file_path):
            print(f"______ Start: Processing folder: {folder_name} -> file: {file_name} __________ \n\n\n")

            with open(file_path, 'r') as file:
                student_code = file.read()

            file_id = get_submission_id(file_name)

            if file_id not in big_json[folder_name] or file_id not in small_json[folder_name]:
                stats_json[folder_name][file_id] = "Skipped"
                continue

            analysis_32b = big_json[folder_name][file_id]
            analysis_7b = small_json[folder_name][file_id]

            if analysis_32b.get("status", False) == "error" or analysis_7b.get("status", False) == "error":
                stats_json[folder_name][file_id] = "Error while parsing LLM response"
                continue


            results_json[folder_name][file_id] = {}
            results_json[folder_name][file_id][analysis_32b["model"]] = build_analysis_object(analysis_32b)
            results_json[folder_name][file_id][analysis_7b["model"]] = build_analysis_object(analysis_7b)
            results_json[folder_name][file_id]["student_submission"] = student_code

            print(f"\n\n\n______ End: Processing folder: {folder_name} -> file: {file_name} __________ \n\n\n")


with open(results_file, "w") as f:
    json.dump(results_json, f, indent=4)

with open(stats_file, "w") as f:
    json.dump(stats_json, f, indent=4)

