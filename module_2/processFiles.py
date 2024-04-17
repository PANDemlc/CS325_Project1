# processFiles.py
# Braden Burgener

# The SOLID principle I inlcuded was S (Single Responsibility Principle)
# Each function has a specific, focused responsibility
# Code is more maintainable and easy to understand with compartmentalization of functions into specific responsibilities

import os
from module_1.scrapText import get_text

# Take in the name and path of the input.txt file containing all of the links - 'name' variable
# Output is that it repeatedly calls other functions and passes urls in so text can be scrapped
def open_file(name):
    try:
        with open(name, 'r') as file:
            for line in file:
                url = line.strip()
                # Call function to scrap text of title and body text of article
                title, body = get_text(url)
                # Call function that creats a file for the scrapped text
                make_file(title, body)
    # Error if the file path or name is not found
    except FileNotFoundError:
        print(f"Input file '{name}' doesn't exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Takes in the title of the article and all of the body text
# Creates a new file that containes the scrapped article
def make_file(title, body):
    name = f"{title}.txt"
    count = 1
    folder_name = os.path.join('Data', 'processed')

    # If the name of the file already exists, dont overwrite. Creates a new filename with increasing numbers
    while os.path.exists(os.path.join(folder_name, name)):
        name = f"{title}-{count}.txt"
        count += 1

    # Make the name of the file the title of the article
    # Write the title and body text of the article to the file
    with open(os.path.join(folder_name, name), 'w') as file:
        file.write(title)
        file.write("\n")
        file.write(body)