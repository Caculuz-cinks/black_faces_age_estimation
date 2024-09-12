import os
import shutil

# Define the source directories and destination directory
source_dir1 = '/Users/caculuz/Downloads/python/second_part'
source_dir2 = '/Users/caculuz/Downloads/python/first_part'
dest_dir = '/Users/caculuz/Downloads/python/FAE_D1_collated'

# Create the destination directory if it doesn't exist
os.makedirs(dest_dir, exist_ok=True)

# Function to move files from source to destination
def merge_folders(source_dir, dest_dir):
    # Loop through the files in the source directory
    for filename in os.listdir(source_dir):
        # Construct the full file path
        source_file = os.path.join(source_dir, filename)
        dest_file = os.path.join(dest_dir, filename)
        
        # Check if it's a file (not a directory)
        if os.path.isfile(source_file):
            # Move or copy the file to the destination folder
            shutil.move(source_file, dest_file)
            # shutil.copy(source_file, dest_file)  # Use this line instead if you want to copy files

# Merge files from both source directories into the destination directory
merge_folders(source_dir1, dest_dir)
merge_folders(source_dir2, dest_dir)

print("Files merged successfully!")
