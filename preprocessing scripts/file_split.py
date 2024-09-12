import os
import shutil

# Define the source directory and destination directories
source_dir = '/Users/caculuz/Downloads/python/FAE_D1_collated'
dest_dir1 = '/Users/caculuz/Downloads/python/first_part'
dest_dir2 = '/Users/caculuz/Downloads/python/second_part'

criteria = "Copy"


# Loop through the files in the source directory
for filename in os.listdir(source_dir):
     # Construct the full file path
    file_path = os.path.join(source_dir, filename)

    # Check if it's a file (not a directory)
    if os.path.isfile(file_path):
        # Move the file based on the criteria
        if criteria in filename:
            shutil.move(file_path, os.path.join(dest_dir1, filename))
        else:
            shutil.move(file_path, os.path.join(dest_dir2, filename))

print("Files separated successfully!")

           


