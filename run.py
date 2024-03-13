# run.py
# Braden Burgener

import os

from module_2 import processFiles
  
# Calls first function to start scrapping atricles given the filename as a preset parameter
def main():
    filename = "Data/raw/input.txt"
    processFiles.open_file(filename)

if __name__ == "__main__":
    main()