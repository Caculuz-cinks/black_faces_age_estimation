import os
import shutil
from collections import defaultdict
import itertools

# Define the source directory and destination directory
source_dir = '/Users/caculuz/Downloads/python/trimed'
dest_dir = '/Users/caculuz/Downloads/python/trimed_b'

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

# Function to duplicate files
def duplicate_files():
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
        
        # Calculate how many duplicates are needed
        if male_files:
            while len(male_files_to_keep) < 100:
                male_files_to_keep.extend(male_files[:100 - len(male_files_to_keep)])
            male_files_to_keep = male_files_to_keep[:100]
        else:
            male_files_to_keep = []
        
        if female_files:
            while len(female_files_to_keep) < 100:
                female_files_to_keep.extend(female_files[:100 - len(female_files_to_keep)])
            female_files_to_keep = female_files_to_keep[:100]
        else:
            female_files_to_keep = []

        # Create duplicate filenames to avoid conflicts
        def get_unique_filename(dest_folder, filename):
            base, ext = os.path.splitext(filename)
            count = 1
            new_filename = filename
            while os.path.exists(os.path.join(dest_folder, new_filename)):
                new_filename = f"{base}_{count}{ext}"
                count += 1
            return new_filename
        
        # Move or copy the selected files to the destination folder
        for filename in male_files_to_keep + female_files_to_keep:
            src_path = os.path.join(source_dir, filename)
            unique_filename = get_unique_filename(dest_dir, filename)
            dest_path = os.path.join(dest_dir, unique_filename)
            shutil.copy(src_path, dest_path)  # Use shutil.move() if you want to move instead of copy

        # Print status
        print(f"Age {age_str}: kept {len(male_files_to_keep)} males and {len(female_files_to_keep)} females")

# Duplicate files as needed
duplicate_files()

print("Files duplicated and copied successfully!")