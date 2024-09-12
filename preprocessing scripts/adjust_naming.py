import os
import re

# Define the source directory
source_dir = '/Users/caculuz/Downloads/python/second_part'

# Get a list of files in the source directory
files = os.listdir(source_dir)

# Loop through each file and rename it
for filename in files:
    # Construct the full file path
    file_path = os.path.join(source_dir, filename)
    
    # Check if it's a file (not a directory)
    if os.path.isfile(file_path):
        # Split the file name and extension
        name, ext = os.path.splitext(filename)
        
        # Remove the last "_X" part from the file name
        if "_" in name:
            new_name = "_".join(name.split("_")[:-1])
            new_filename = f"{new_name}{ext}"
            new_file_path = os.path.join(source_dir, new_filename)
            
            # Rename the file
            os.rename(file_path, new_file_path)

print("Files renamed successfully!")
