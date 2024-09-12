import os
import re

# Define the source directory
source_dir = '/Users/caculuz/Downloads/python/second_part'

# Define the regex pattern to match the filename structure
pattern = re.compile(r'^(.*_)(\d+)(\.\w+)$')

# List to store proposed renames
proposed_renames = []

# Initialize the odd number counter
next_odd_number = 1

# Generate a list of filenames to rename
files = sorted(os.listdir(source_dir))

# Process each file
for filename in files:
    file_path = os.path.join(source_dir, filename)

    if os.path.isfile(file_path):
        match = pattern.match(filename)
        if match:
            # Extract the prefix, last digit, and extension
            prefix, last_digit, extension = match.groups()

            # Create the new filename with the serialized odd number
            new_name = f"{prefix}{next_odd_number:05d}{extension}"
            new_file_path = os.path.join(source_dir, new_name)

            # Check if the new file name already exists
            if os.path.exists(new_file_path):
                print(f"Conflict detected: {new_file_path} already exists. Skipping {filename}.")
            else:
                # Add to rename list
                proposed_renames.append((file_path, new_file_path))
                # Increment the odd number by 2
                next_odd_number += 2
        else:
            print(f"File '{filename}' does not match the expected pattern and will be skipped.")

# Ask for confirmation
print("\nProposed renames:")
for old, new in proposed_renames:
    print(f"{os.path.basename(old)} -> {os.path.basename(new)}")

confirm = input("\nDo you want to proceed with these renames? (yes/no): ").lower().strip()
if confirm == 'yes':
    # Perform the renames
    for old_path, new_path in proposed_renames:
        try:
            os.rename(old_path, new_path)
            print(f"Renamed '{os.path.basename(old_path)}' to '{os.path.basename(new_path)}'")
        except Exception as e:
            print(f"Error renaming '{os.path.basename(old_path)}' to '{os.path.basename(new_path)}': {e}")
    print("File renaming process completed!")
else:
    print("Renaming process cancelled.")
