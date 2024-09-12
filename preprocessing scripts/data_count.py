import os
from collections import defaultdict

# Define the directory containing the files
directory = '/Users/caculuz/Downloads/python/trimed_b'

# Dictionaries to store the count of males and females for each age
age_male_count = defaultdict(int)
age_female_count = defaultdict(int)

# Check if directory exists
if not os.path.isdir(directory):
    print(f"Directory {directory} does not exist.")
    exit()

# Loop through the files in the directory
for filename in os.listdir(directory):
    # Check if it's a file and matches the expected naming format
    file_path = os.path.join(directory, filename)
    if os.path.isfile(file_path):
        # Split the filename by underscores, ignoring the extension
        parts = filename.split('_')
        
        # Ensure the filename has at least 4 parts (age, gender, and others)
        if len(parts) >= 4:
            # The first part of the filename is the age
            age = parts[0]
            
            # The second part of the filename is the gender
            gender = parts[1]
            
            if gender == '0':
                # Increment the male count for this age
                age_male_count[age] += 1
            elif gender == '1':
                # Increment the female count for this age
                age_female_count[age] += 1
        else:
            print(f"Filename format incorrect: {filename}")

# Define the range of ages to check
age_range = range(101)

# Prepare lists for ages with no males or no females
no_males_ages = []
no_females_ages = []

# Check for ages with no males or no females
for age in age_range:
    age_str = str(age)
    if age_male_count[age_str] == 0:
        no_males_ages.append(age_str)
    if age_female_count[age_str] == 0:
        no_females_ages.append(age_str)

# Write the results to a file
with open('ages_with_missing_data.txt', 'w') as file:
    if no_males_ages:
        file.write("Ages with no males:\n")
        for age in no_males_ages:
            file.write(f"Age {age}\n")
    else:
        file.write("All ages have males.\n")
    
    file.write("\n")  # Add a newline to separate sections
    
    if no_females_ages:
        file.write("Ages with no females:\n")
        for age in no_females_ages:
            file.write(f"Age {age}\n")
    else:
        file.write("All ages have females.\n")