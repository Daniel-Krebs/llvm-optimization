import re

def extract_section():
    file_path = input("Enter the text file path: ").strip()
    print("Select a section number:")
    print("1. Total parsing frontend")
    print("2. Total parsing backend")
    print("3. Files that took longest to parse (compiler frontend)")
    print("4. Files that took longest to codegen (compiler backend)")
    print("5. Templates that took longest to instantiate")
    print("6. Template sets that took longest to instantiate")
    print("7. Functions that took longest to compile")
    print("8. Function sets that took longest to compile/optimize")
    section_number = input("Enter the section number (1-8): ").strip()

    sections = {
        "1": "Time summary:\nCompilation",
        "2": "Time summary:\nCompilation",
        "3": "Files that took longest to parse (compiler frontend):",
        "4": "Files that took longest to codegen (compiler backend):",
        "5": "Templates that took longest to instantiate:",
        "6": "Template sets that took longest to instantiate:",
        "7": "Functions that took longest to compile:",
        "8": "Function sets that took longest to compile / optimize:"
    }

    # Validate the section number
    if section_number not in sections:
        print(f"Invalid section number: {section_number}. Please choose a number between 1 and 8.")
        return

    section_header = sections[section_number]

    try:
        # Read the file contents
        with open(file_path, 'r') as file:
            contents = file.read()

        # Locate the start of the desired section
        start_match = re.search(re.escape(section_header), contents)
        if not start_match:
            print(f"Section {section_number} ('{section_header}') not found in the file.")
            return

        start_idx = start_match.end()

        # Locate the end of the section or end of file
        next_section_match = re.search(r"\n\s*\*{4}\s*", contents[start_idx:])
        end_idx = next_section_match.start() + start_idx if next_section_match else len(contents)

        # Extract and print the section
        section_text = contents[start_idx:end_idx].strip()
        print(f"\nSection {section_number}: {section_header}\n")
        print(section_text)

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    extract_section()
