import os
import shutil
from collections import defaultdict

# Define the source directory and destination directory
source_dir = '/Users/caculuz/Downloads/python/FAE_D1_collated'
dest_dir = '/Users/caculuz/Downloads/python/trimed'

# Create the destination directory if it doesn't exist
os.makedirs(dest_dir, exist_ok=True)

# Dictionary to store the files for each age and gender
files_by_age_gender = defaultdict(lambda: {'male': [], 'female': []})

# Loop through the files in the source directory
for filename in os.listdir(source_dir):
    if os.path.isfile(os.path.join(source_dir, filename)):
        parts = filename.split('_')
        if len(parts) >= 4:
            age = parts[0]
            gender = 'male' if parts[1] == '0' else 'female'
            files_by_age_gender[age][gender].append(filename)

# Define the range of ages to process
age_range = range(101)

# Function to trim files
def trim_files():
    for age in age_range:
        age_str = str(age)
        male_files = files_by_age_gender[age_str]['male']
        female_files = files_by_age_gender[age_str]['female']
        
        # Determine the number of files to keep
        num_males_to_keep = min(100, len(male_files))
        num_females_to_keep = min(100, len(female_files))
        
        # Select files to keep (first 100 or as many as available)
        male_files_to_keep = male_files[:num_males_to_keep]
        female_files_to_keep = female_files[:num_females_to_keep]
        
        # Move the selected files to the destination folder
        for filename in male_files_to_keep + female_files_to_keep:
            src_path = os.path.join(source_dir, filename)
            dest_path = os.path.join(dest_dir, filename)
            shutil.copy(src_path, dest_path)  # Use shutil.move() if you want to move instead of copy
        
        # Print status
        print(f"Age {age_str}: kept {len(male_files_to_keep)} males and {len(female_files_to_keep)} females")

# Trim the files
trim_files()

print("Files trimmed and copied successfully!")
