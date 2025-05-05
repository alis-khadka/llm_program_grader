import pandas as pd
from docx import Document
import json
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

def extract_docx_text(file_path):
    """Extract text from a .docx file"""
    # Ensure the file path is absolute or relative to the script dir
    if not os.path.isabs(file_path):
        file_path = os.path.join(script_dir, file_path)
    doc = Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

# 1. Load comments CSV
comments_csv_path = os.path.join(script_dir, "Comments.csv")
try:
    comments_df = pd.read_csv(comments_csv_path)
except FileNotFoundError:
    print(f"Error: Could not find Comments.csv at {comments_csv_path}")
    exit() # Or handle the error appropriately

# 2. Process each lab
for lab_num in range(1, 10):
    lab_key = f"Lab_{lab_num}"
    
    # Create lab dictionary
    lab_data = {
        "lab_number": lab_num,
        "problem_description": "",
        "reference_solution": "",
        "comments": []
    }

    # 3. Load problem description
    doc_path = os.path.join(script_dir, f"Lab_{lab_num}.docx")
    if os.path.exists(doc_path):
        lab_data["problem_description"] = extract_docx_text(doc_path)
    else:
        print(f"Warning: Could not find {doc_path}")

    # 4. Load solution
    solution_path = os.path.join(script_dir, f"Lab_{lab_num}_solution.docx")
    if os.path.exists(solution_path):
        lab_data["reference_solution"] = extract_docx_text(solution_path)
    else:
        print(f"Warning: Could not find {solution_path}")

    # 5. Extract comments
    if lab_key in comments_df.columns:
        # Filter non-empty comments
        lab_comments = comments_df[lab_key].dropna().tolist()
        lab_data["comments"] = [c for c in lab_comments if str(c).strip()]

    # 6. Save to JSON
    output_file = os.path.join(script_dir, f"Lab_{lab_num}.json")
    with open(output_file, 'w') as f:
        json.dump(lab_data, f, indent=2)

    print(f"Created {output_file} with:")
    print(f"- {len(lab_data['problem_description'].split())} words in description")
    print(f"- {len(lab_data['reference_solution'].split())} words in solution")
    print(f"- {len(lab_data['comments'])} comments\n")