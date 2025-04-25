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
final_stats_file = os.path.join(PROJECT_ROOT, RESULTS, "total_file_stat.json")

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

with open(final_stats_file, "r") as f:
    final_stats_json = json.load(f) 

for index, (key, value) in enumerate(task_json.items()):
    folder_name = key
    print(f"______ START: Processing Folder: {folder_name} __________\n\n")

    # results_json.setdefault(folder_name, {})
    # stats_json.setdefault(folder_name, {})
    final_stats_json.setdefault(folder_name, {})

    results_folder_details = results_json[folder_name]
    stats_folder_details = results_json[folder_name]

    folder_dir = os.path.join(PROJECT_ROOT, SOLUTIONS_PATH, folder_name)

    total_files = len(os.listdir(folder_dir))
    num_of_files_with_parsing_error = sum(1 for v in stats_json[folder_name].values() if v == "Error while parsing LLM response")
    num_of_files_skipped = sum(1 for v in stats_json[folder_name].values() if v == "skipped")
    num_of_files_processed = len(results_json[folder_name].keys())

    final_stats_json[folder_name] = {
        "total_files": total_files,
        "num_of_files_with_parsing_error": num_of_files_with_parsing_error,
        "num_of_files_skipped": num_of_files_skipped,
        "num_of_files_processed": num_of_files_processed,
        "does_the_numbers_make_sense?": total_files == num_of_files_skipped + num_of_files_with_parsing_error + num_of_files_processed
    }

with open(final_stats_file, "w") as f:
    json.dump(final_stats_json, f, indent=4)
