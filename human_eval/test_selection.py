import json
import os

# --- Configuration ---
SELECTED_PROBLEM_IDS = [
    # Easy
    "19_20-1-1-python", "19_20-2-1-python", "19_20-2-2-python",
    "19_20-5-1-python", "19_20-5-2-python",
    # Medium
    "19_20-3-1-python", "19_20-6-1-python", "20_21-1-1-python",
    "20_21-1-2-python", "21_22-1-1-python",
    # Difficult
    "19_20-4-1-python", "19_20-4-2-python", "20_21-3-1-python",
    "20_21-3-2-python", "21_22-3-1-python",
]
INPUT_TESTS_FILE = os.path.join("dataset", "tests.json")
OUTPUT_TESTS_FILE = os.path.join("dataset", "selected_tests.json")
# --- End Configuration ---

def filter_tests(input_path, output_path, selected_ids):
    """Reads tests, filters by ID, and writes to a new JSON file."""
    try:
        with open(input_path, 'r', encoding='utf-8') as f_in:
            all_tests = json.load(f_in)
    except FileNotFoundError:
        print(f"Error: Input tests file not found at {input_path}")
        return
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {input_path}")
        return

    selected_tests = {
        test_id: test_data
        for test_id, test_data in all_tests.items()
        if test_id in selected_ids
    }

    try:
        with open(output_path, 'w', encoding='utf-8') as f_out:
            json.dump(selected_tests, f_out, indent=2)
        print(f"Successfully created {output_path} with tests for {len(selected_tests)} problems.")
    except IOError as e:
        print(f"Error writing to {output_path}: {e}")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    abs_input_path = r"C:\Users\MSI\Documents\VS Code Projects\llm_program_grader\dataset\tests.json"
    abs_output_path = r"C:\Users\MSI\Documents\VS Code Projects\llm_program_grader\human_eval\selected_tests.json"
    filter_tests(abs_input_path, abs_output_path, SELECTED_PROBLEM_IDS)