import json
import os

# Directory containing the individual lab JSON files
script_dir = os.path.dirname(os.path.abspath(__file__))
input_dir = script_dir # Assuming JSON files are in the same directory as this script

# Output file path
output_file_path = os.path.join(script_dir, "combined_labs.json")

combined_data = []

# Loop through lab numbers 1 to 9
for lab_num in range(1, 10):
    input_file_name = f"Lab_{lab_num}.json"
    input_file_path = os.path.join(input_dir, input_file_name)

    if os.path.exists(input_file_path):
        try:
            with open(input_file_path, 'r', encoding='utf-8') as f:
                lab_data = json.load(f)
                # Ensure the lab_number from the file matches (optional check)
                if lab_data.get("lab_number") == lab_num:
                    combined_data.append(lab_data)
                else:
                    print(f"Warning: Mismatch in lab number for {input_file_name}. Skipping.")
        except json.JSONDecodeError:
            print(f"Error: Could not decode JSON from {input_file_name}. Skipping.")
        except Exception as e:
            print(f"Error reading {input_file_name}: {e}. Skipping.")
    else:
        print(f"Warning: File not found {input_file_path}. Skipping.")

# Write the combined data to the output file
try:
    with open(output_file_path, 'w', encoding='utf-8') as f:
        json.dump(combined_data, f, indent=2) # Use indent=2 for pretty printing
    print(f"Successfully combined labs into {output_file_path}")
    print(f"Total labs combined: {len(combined_data)}")
except Exception as e:
    print(f"Error writing combined file {output_file_path}: {e}")
