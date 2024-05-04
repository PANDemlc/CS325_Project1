# processFiles.py
# Braden Burgener

# The SOLID principle I inlcuded was S (Single Responsibility Principle)
# Each function has a specific, focused responsibility
# Code is more maintainable and easy to understand with compartmentalization of functions into specific responsibilities

import os
import validators
from module_1.scrapText import get_text
from webpage_creation import textToHTML

# Take in the name and path of the input.txt file containing all of the links - 'name' variable
# Output is that it repeatedly calls other functions and passes urls in so text can be scrapped
def open_file(name):
    try:
        with open(name, 'r') as file:
            clear_file('webpage_creation/input.txt')
            for line in file:
                url = line.strip()

                if not validators.url(url):
                    print(f"Invalid URL: {url}")
                    continue

                # Call function to scrap text of title and body text of article
                title, body = get_text(url)
                # Call function that creats a file for the scrapped text
                make_file(title, body)
                # Print all titles and bodies to one file for HTML creation
                print_to_file(title, body)
        textToHTML.txt_to_html('webpage_creation/input.txt', 'webpage_creation/output.html')
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

# Print all titles and bodies to one file for HTML creation
def print_to_file(title, body):
    with open('webpage_creation/input.txt', 'a') as f:
        f.write(title + '\n')
        f.write(body + '\n')

# Clear the input file for HTML creation each time the program is run
def clear_file(file_name):
    with open(file_name, 'w') as f:
        pass