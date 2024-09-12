

import os
import shutil
import random
from collections import defaultdict

# Define the source directory and destination directory
source_dir = '/Users/caculuz/Downloads/python/trimed_b'
dest_dir = '/Users/caculuz/Downloads/python/trimed_c'

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

# Define age ranges for sampling
# Example: for age 4, sample from ages 3 to 7
sampling_age_ranges = {
    '0': range(0, 1),
    '1': range(0, 2),
    '2': range(1, 3),
    '3': range(2, 4),
    '4': range(2, 7),
    '5': range(3, 7),
    '6': range(4, 8),
    '7': range(5, 10),
    '8': range(7, 10),
    '9': range(8, 13),
    '10': range(8, 13),
    '11': range(10, 14),
    '12': range(10, 15),
    '13': range(10, 15),
    '14': range(12, 16),
    '15': range(14, 18),
    '16': range(15, 20),
    '17': range(17, 22),
    '18': range(18, 23),
    '19': range(19, 24),
    '20': range(20, 25),
    '21': range(21, 26),
    '22': range(22, 27),
    '23': range(23, 28),
    '24': range(24, 29),
    '25': range(25, 30),
    '26': range(26, 31),
    '27': range(27, 32),
    '28': range(28, 33),
    '29': range(29, 34),
    '30': range(30, 35),
    '31': range(31, 36),
    '32': range(32, 37),
    '33': range(33, 38),
    '34': range(34, 39),
    '35': range(35, 40),
    '36': range(36, 41),
    '37': range(37, 42),
    '38': range(38, 43),
    '39': range(39, 44),
    '40': range(40, 45),
    '41': range(41, 46),
    '42': range(42, 47),
    '43': range(43, 48),
    '44': range(44, 49),
    '45': range(45, 50),
    '46': range(46, 51),
    '47': range(47, 52),
    '48': range(48, 53),
    '49': range(49, 54),
    '50': range(50, 55),
    '51': range(51, 56),
    '52': range(52, 57),
    '53': range(53, 58),
    '54': range(54, 59),
    '55': range(52, 58),
    '56': range(56, 61),
    '57': range(54, 61),
    '58': range(54, 61),
    '59': range(56, 62),
    '60': range(60, 65),
    '61': range(61, 66),
    '62': range(60, 65),
    '63': range(60, 65),
    '64': range(60, 65),
    '65': range(65, 71),
    '66': range(66, 71),
    '67': range(65, 71),
    '68': range(65, 71),
    '69': range(65, 71),
    '70': range(65, 81),
    '71': range(65, 81),
    '72': range(65, 81),
    '73': range(65, 81),
    '74': range(65, 81),
    '75': range(65, 81),
    '76': range(70, 81),
    '77': range(70, 81),
    '78': range(70, 81),
    '79': range(70, 81),
    '80': range(75, 91),
    '81': range(75, 91),
    '82': range(75, 91),
    '83': range(75, 91),
    '84': range(75, 91),
    '85': range(75, 91),
    '86': range(80, 91),
    '87': range(80, 91),
    '88': range(80, 91),
    '89': range(80, 91),
    '90': range(90, 100),
    '91': range(90, 100),
    '92': range(90, 100),
    '93': range(90, 100),
    '94': range(90, 100),
    '95': range(90, 100),
    '96': range(90, 100),
    '97': range(90, 100),
    '98': range(90, 100),
    '99': range(90, 100),
    '100': range(90, 100)
}

# Function to generate a new filename
def generate_new_filename(age, gender, serial, ext):
    random_number = random.randint(1, 6)
    gender_digit = '0' if gender == 'male' else '1'
    new_filename = f"{age}_{gender_digit}_{random_number}_{serial}{ext}"
    return new_filename

# Function to duplicate files
def duplicate_files():
    serial_number = 1
    
    # Collect all files by gender from all ages
    all_files_by_gender = {
        'male': [],
        'female': []
    }
    
    for age in age_range:
        age_str = str(age)
        all_files_by_gender['male'].extend(files_by_age_gender[age_str]['male'])
        all_files_by_gender['female'].extend(files_by_age_gender[age_str]['female'])
    
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
        
        # Define sampling range for current age
        sampling_range = sampling_age_ranges.get(age_str, age_range)
        sampled_males = [filename for age in sampling_range for filename in files_by_age_gender[str(age)]['male']]
        sampled_females = [filename for age in sampling_range for filename in files_by_age_gender[str(age)]['female']]
        
        # Calculate how many duplicates are needed
        if len(male_files_to_keep) < 100:
            needed_males = 100 - len(male_files_to_keep)
            if sampled_males:
                male_files_to_keep.extend(random.sample(sampled_males, min(needed_males, len(sampled_males))))
            male_files_to_keep = male_files_to_keep[:100]

        if len(female_files_to_keep) < 100:
            needed_females = 100 - len(female_files_to_keep)
            if sampled_females:
                female_files_to_keep.extend(random.sample(sampled_females, min(needed_females, len(sampled_females))))
            female_files_to_keep = female_files_to_keep[:100]

        # Move or copy the selected files to the destination folder
        for filename in male_files_to_keep:
            src_path = os.path.join(source_dir, filename)
            file_ext = os.path.splitext(filename)[1]  # Get the file extension (.jpg or .png)
            new_filename = generate_new_filename(age_str, 'male', serial_number, file_ext)
            serial_number += 1
            dest_path = os.path.join(dest_dir, new_filename)
            shutil.copy(src_path, dest_path)  # Use shutil.move() if you want to move instead of copy

        for filename in female_files_to_keep:
            src_path = os.path.join(source_dir, filename)
            file_ext = os.path.splitext(filename)[1]  # Get the file extension (.jpg or .png)
            new_filename = generate_new_filename(age_str, 'female', serial_number, file_ext)
            serial_number += 1
            dest_path = os.path.join(dest_dir, new_filename)
            shutil.copy(src_path, dest_path)  # Use shutil.move() if you want to move instead of copy

        # Print status
        print(f"Age {age_str}: kept {len(male_files_to_keep)} males and {len(female_files_to_keep)} females")

# Duplicate files as needed
duplicate_files()

print("Files duplicated and copied successfully!")