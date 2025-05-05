import json
import os
import random
import subprocess
import io
import sys
import cProfile
import pstats
import traceback
import re
from pylint.lint import PyLinter
from pylint.reporters.text import TextReporter

# --- Configuration ---
SELECTED_PROBLEM_IDS = [
    "19_20-2-2-python",
    "19_20-5-1-python", 
    "20_21-1-2-python",
    "19_20-3-1-python",
    "20_21-3-1-python", 
    "20_21-3-2-python"
]

# Mapping problem IDs to specific student files
SPECIFIC_STUDENT_FILES = {
    "19_20-2-2-python": ["BUQGY7N7.py"],
    "19_20-5-1-python": ["BUQGY7N7.py"],
    "20_21-1-2-python": ["2V5AQFDC.py"],
    "19_20-3-1-python": ["3QDYQU4I.py"],
    "20_21-3-1-python": ["2DXKHJJW.py"],
    "20_21-3-2-python": ["2FXPE3DD.py"]
}
STUDENT_SOLUTIONS_DIR = os.path.join("dataset", "solutions")
SELECTED_TESTS_FILE = os.path.join("human_eval", "selected_tests_for_ppt.json")
PYTHON_EXECUTABLE = "C:/Users/MSI/anaconda3/envs/mlProject/python.exe" # Adjust if needed
NUM_STUDENTS_PER_PROBLEM = 1 # Now we're selecting specific students
PYLINT_OPTIONS = ['--disable=all', '--enable=W,E,F'] # Basic Pylint checks

def load_tests(tests_file_path):
    """Loads the selected tests from the JSON file."""
    try:
        with open(tests_file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Selected tests file not found at {tests_file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {tests_file_path}")
        return None

def get_student_files(problem_dir):
    """Gets a list of Python files from the problem's solution directory."""
    if not os.path.isdir(problem_dir):
        return []
    return [f for f in os.listdir(problem_dir) if f.endswith(".py")]

def run_functionality_tests(student_file_path, tests):
    """Runs test cases against the student's code using subprocess."""
    passed_count = 0
    total_count = len(tests)
    results = []

    for test in tests:
        test_code = test.get("testcode", "")
        expected_output = test.get("expected", "").strip()

        # Combine student code and test code for execution
        try:
            with open(student_file_path, 'r', encoding='utf-8') as f_student:
                student_code = f_student.read()
        except Exception as e:
            results.append({"test": test.get("test_number"), "status": "ERROR", "detail": f"Failed to read student file: {e}"})
            continue

        full_code = student_code + "\n\n" + test_code

        try:
            # Run the combined code in a separate process
            process = subprocess.run(
                [PYTHON_EXECUTABLE, "-c", full_code],
                capture_output=True,
                text=True,
                timeout=5, # Add a timeout to prevent infinite loops
                encoding='utf-8'
            )

            actual_output = process.stdout.strip()
            stderr_output = process.stderr.strip()

            if process.returncode != 0:
                 results.append({"test": test.get("test_number"), "status": "FAIL", "detail": f"Runtime Error: {stderr_output}", "expected": expected_output, "actual": actual_output})
            elif actual_output == expected_output:
                passed_count += 1
                results.append({"test": test.get("test_number"), "status": "PASS"})
            else:
                 results.append({"test": test.get("test_number"), "status": "FAIL", "detail": "Output Mismatch", "expected": expected_output, "actual": actual_output})

        except subprocess.TimeoutExpired:
             results.append({"test": test.get("test_number"), "status": "FAIL", "detail": "Timeout Expired"})
        except Exception as e:
             results.append({"test": test.get("test_number"), "status": "ERROR", "detail": f"Execution Error: {e}"})

    return passed_count, total_count, results

def run_pylint_check(student_file_path):
    """Runs pylint as a subprocess and returns the score (0–10) or None on error."""
    if not os.path.exists(student_file_path):
        print(f"  Error: target file not found for Pylint: {student_file_path}")
        return None

    # Build the command: use the same interpreter you use for functionality tests
    cmd = [
        PYTHON_EXECUTABLE, "-m", "pylint",
        *PYLINT_OPTIONS,
        student_file_path
    ]

    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=15
        )
        output = proc.stdout + proc.stderr

        # Look for the “Your code has been rated at 7.50/10” style line
        m = re.search(r"rated at\s+([0-9]+\.[0-9]+)/10", output)
        if m:
            return float(m.group(1))
        else:
            print(f"  Warning: could not parse Pylint score for {os.path.basename(student_file_path)}")
            # Uncomment to debug:
            # print(output)
            return None

    except subprocess.TimeoutExpired:
        print(f"  Error: Pylint on {os.path.basename(student_file_path)} timed out")
        return None
    except Exception:
        print(f"  Error running Pylint on {os.path.basename(student_file_path)}:")
        traceback.print_exc(file=sys.stdout)
        return None

def run_complexity_check(student_file_path, test_to_profile):
    """Runs cProfile on the student's code with a specific test case."""
    if not test_to_profile:
        return "No suitable test case found for profiling.", None

    test_code = test_to_profile.get("testcode", "")
    stats_string = "Error during profiling."
    profile_stats = None

    try:
        with open(student_file_path, 'r', encoding='utf-8') as f_student:
            student_code = f_student.read()
    except Exception as e:
        return f"Failed to read student file: {e}", None

    full_code = student_code + "\n\n" + test_code

    try:
        # Use cProfile directly
        profiler = cProfile.Profile()
        profiler.runctx(full_code, globals(), locals())

        # Get stats
        s = io.StringIO()
        ps = pstats.Stats(profiler, stream=s).sort_stats('cumulative')
        ps.print_stats(15) # Print top 15 cumulative time functions
        stats_string = s.getvalue()
        profile_stats = ps.total_tt # Total time spent in functions

    except Exception as e:
        stats_string = f"Profiling Error: {e}"

    return stats_string, profile_stats

# --- Main Execution ---
if __name__ == "__main__":
    tests_file = r"C:\Users\MSI\Documents\VS Code Projects\llm_program_grader\dataset\tests.json"
    solutions_base_dir = r"C:\Users\MSI\Documents\VS Code Projects\llm_program_grader\dataset\solutions"

    all_tests_data = load_tests(tests_file)
    if not all_tests_data:
        sys.exit(1)

    overall_results = {}

    for problem_id in SELECTED_PROBLEM_IDS:
        print(f"--- Processing Problem: {problem_id} ---")
        problem_dir = os.path.join(solutions_base_dir, problem_id)
        
        # Use the specific student files instead of random selection
        if problem_id in SPECIFIC_STUDENT_FILES:
            selected_students = SPECIFIC_STUDENT_FILES[problem_id]
            # Verify the files exist
            for student in selected_students:
                if not os.path.exists(os.path.join(problem_dir, student)):
                    print(f"  Warning: Student file {student} not found for {problem_id}")
        else:
            student_files = get_student_files(problem_dir)
            if not student_files:
                print(f"  No student solution files found in {problem_dir}")
                continue
            selected_students = student_files[:NUM_STUDENTS_PER_PROBLEM]
        
        print(f"  Selected students: {selected_students}")

        problem_tests = all_tests_data.get(problem_id)
        if not problem_tests:
            print(f"  No tests found for {problem_id} in {tests_file}")
            continue

        # Find the first non-example test for profiling
        profile_test_case = next((t for t in problem_tests if not t.get("is_example", False)), None)
        if not profile_test_case and problem_tests:
             profile_test_case = problem_tests[0] # Fallback to first test if no non-example

        overall_results[problem_id] = {}

        for student_filename in selected_students:
            student_file_path = os.path.join(problem_dir, student_filename)
            if not os.path.exists(student_file_path):
                print(f"  Error: Student file not found: {student_file_path}")
                continue
                
            print(f"\n  Checking student: {student_filename}")
            student_results = {}

            # Continue with your existing code for functionality, pylint, complexity checks
            # ...
            
            # 1. Functionality Check
            print("    Running functionality tests...")
            passed, total, func_details = run_functionality_tests(student_file_path, problem_tests)
            pass_rate = (passed / total * 100) if total > 0 else 0
            student_results["functionality"] = {"passed": passed, "total": total, "pass_rate": f"{pass_rate:.2f}%", "details": func_details}
            print(f"      Result: {passed}/{total} tests passed ({pass_rate:.2f}%)")
            
            # 2. Code Quality Check
            print("    Running Pylint check...")
            pylint_score = run_pylint_check(student_file_path)
            student_results["quality"] = {"pylint_score": pylint_score}
            print(f"      Pylint Score: {pylint_score if pylint_score is not None else 'Error'}/10.0")
            
            # 3. Complexity Check
            print(f"    Running cProfile check (using test {profile_test_case.get('test_number', 'N/A') if profile_test_case else 'None'})...")
            profile_output, total_time = run_complexity_check(student_file_path, profile_test_case)
            student_results["complexity"] = {"cprofile_total_time": total_time, "cprofile_output_summary": profile_output}
            print(f"      cProfile Total Time: {total_time if total_time is not None else 'Error'}")

            overall_results[problem_id][student_filename] = student_results

    # Save the results to a JSON file
    output_results_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "specific_students_results.json")
    try:
        with open(output_results_file, 'w', encoding='utf-8') as f_res:
            json.dump(overall_results, f_res, indent=2)
        print(f"\n--- Overall results saved to {output_results_file} ---")
    except IOError as e:
        print(f"\nError writing results file: {e}")

    print("\n--- Manual Checking Complete ---")