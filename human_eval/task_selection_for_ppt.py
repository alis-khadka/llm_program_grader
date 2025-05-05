import json
import os

# --- Configuration ---
SELECTED_PROBLEM_IDS = [
    # Only include the specified problems
    "19_20-2-2-python",
    "19_20-5-1-python",
    "20_21-1-2-python",
    "19_20-3-1-python",
    "20_21-3-1-python",
    "20_21-3-2-python",
]
INPUT_TASKS_FILE = os.path.join("dataset", "tasks.json")
OUTPUT_TASKS_FILE = os.path.join("human_eval", "selected_tasks.json")
# --- End Configuration ---

def filter_tasks(input_path, output_path, selected_ids):
    """Reads tasks, filters by ID, and writes to a new JSON file."""
    try:
        with open(input_path, 'r', encoding='utf-8') as f_in:
            all_tasks = json.load(f_in)
    except FileNotFoundError:
        print(f"Error: Input tasks file not found at {input_path}")
        return
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {input_path}")
        return

    selected_tasks = {
        task_id: task_data
        for task_id, task_data in all_tasks.items()
        if task_id in selected_ids
    }

    try:
        with open(output_path, 'w', encoding='utf-8') as f_out:
            json.dump(selected_tasks, f_out, indent=2)
        print(f"Successfully created {output_path} with {len(selected_tasks)} tasks.")
    except IOError as e:
        print(f"Error writing to {output_path}: {e}")

if __name__ == "__main__":
    abs_input_path = r"C:\Users\MSI\Documents\VS Code Projects\llm_program_grader\dataset\tasks.json"
    abs_output_path = r"C:\Users\MSI\Documents\VS Code Projects\llm_program_grader\human_eval\selected_tasks_for_ppt.json"
    filter_tasks(abs_input_path, abs_output_path, SELECTED_PROBLEM_IDS)