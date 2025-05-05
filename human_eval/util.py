import json
import os

# List of problem IDs to extract
PROBLEM_IDS = [
    "19_20-2-2-python",
    "19_20-5-1-python",
    "20_21-1-2-python", 
    "19_20-3-1-python",
    "20_21-3-1-python", 
    "20_21-3-2-python"
]

# Input and output files
INPUT_FILE = "manual_check_results.json"
OUTPUT_FILE = "extracted_problems.json"

def extract_problems(input_path, output_path, problem_ids):
    """Extract specified problems from the results file and save to a new JSON file."""
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            all_results = json.load(f)
    except Exception as e:
        print(f"Error reading input file: {e}")
        return False
    
    # Extract only the requested problems
    extracted_data = {
        problem_id: all_results.get(problem_id, {})
        for problem_id in problem_ids
        if problem_id in all_results
    }
    
    # Save to new file
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(extracted_data, f, indent=2)
        print(f"Successfully extracted {len(extracted_data)} problems to {output_path}")
        
        # List which problems were found and which weren't
        found = [pid for pid in problem_ids if pid in all_results]
        missing = [pid for pid in problem_ids if pid not in all_results]
        
        if found:
            print(f"Found problems: {', '.join(found)}")
        if missing:
            print(f"Missing problems: {', '.join(missing)}")
            
        return True
    except Exception as e:
        print(f"Error writing output file: {e}")
        return False

if __name__ == "__main__":
    # Get the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, INPUT_FILE)
    output_path = os.path.join(script_dir, OUTPUT_FILE)
    
    extract_problems(input_path, output_path, PROBLEM_IDS)