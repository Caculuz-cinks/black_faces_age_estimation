import os
import re

# Define the source directory
source_dir = '/Users/caculuz/Downloads/python/first_part'

# Define the regex pattern to match the filename structure
pattern = re.compile(r'^(.*_)(\d+)(\.\w+)$')

# List to store proposed renames
proposed_renames = []

# Initialize the even number counter
next_even_number = 2

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

            # Create the new filename with the serialized even number
            new_name = f"{prefix}{next_even_number}{extension}"
            new_file_path = os.path.join(source_dir, new_name)

            # Add to rename list
            proposed_renames.append((file_path, new_file_path))

            # Increment the even number by 2
            next_even_number += 2

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