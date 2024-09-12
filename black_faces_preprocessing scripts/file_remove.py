import os

# Define the source directory
source_dir = '/Users/caculuz/Downloads/python/first_part'

# Define the part of the name to remove
part_to_remove = ' - Copy'

# Loop through the files in the source directory
for filename in os.listdir(source_dir):
    # Construct the full file path
    file_path = os.path.join(source_dir, filename)
    
    # Check if it's a file (not a directory)
    if os.path.isfile(file_path):
        # Create the new filename by removing the specified part
        new_filename = filename.replace(part_to_remove, '')
        
        # Construct the full path for the new file
        new_file_path = os.path.join(source_dir, new_filename)
        
        # Rename the file
        os.rename(file_path, new_file_path)

print("File names updated successfully!")
