import os
import glob

# Specify the folder path (replace with your actual folder path)
folder_path = '/Users/mcw/Documents/llvm/llama.cpp/ninja_build_new_2'

# Get all JSON files in the folder and subdirectories
json_files = []

# Walk through the directory tree
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith('.json'):  # Check if the file ends with .json
            json_files.append(os.path.join(root, file))

# Specify the path to the output text file
output_file = '/Users/mcw/Documents/llvm/jsonfiles.txt'

# Open the output file in write mode
with open(output_file, 'w') as f:
    if json_files:
        f.write("JSON files found:\n")
        for json_file in json_files:
            f.write(f"{json_file}\n")
    else:
        f.write("No JSON files found in the specified folder and subfolders.\n")

print(f"The list of JSON files has been saved to {output_file}.")

