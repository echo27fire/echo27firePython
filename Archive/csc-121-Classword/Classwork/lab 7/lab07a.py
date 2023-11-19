'''
Author: Taylor G.
Date: Sep 30, 2023
Class: CSC 121
program: lab07a - file display
'''
import os


# Variable for what file to open. Path is relative to the code running location. Change as appropriate for files in another path.
open_file = "numbers.txt"  

'''  testing notes:
 VS-Code cannot seem to find this file in same path as code. Theory: odd venv issue? 
 For some reason it appears that VS code attempted to find the file two directory's up? 
 IE: C:\Github\TG-CSC-121-DTCC-FA23 and not C:\Github\TG-CSC-121-DTCC-FA23\Classwork\Lab 7
 workaround 1: use Mu to test.
 workaround 2: copy or soft link file to path code is running from for VS code. use output of line 26: getcwd from os mod. to ID path.
'''

# Added line for debugging. Uses the module from the import os to display the current working path of the script.
print(os.getcwd()) 

try: # phase 1: attempt to open the file
    with open(open_file, "r") as num_file: #open the file variable in "r" or read only mode
        for line in num_file: #loop through lines in the test file
            try:
                number = int(line.strip())  #reads the line in the file, removes whitespace, and converts to an interger.
                print(number)
            except ValueError: # error if a line in the file is 'bad' 
                print(f"Invalid line detected: {line.strip()}")

except FileNotFoundError: # error message if the file under 'open_file' variable cannot be found
    print(f"The file {open_file} is not found. Check the file path variable")  # Added f-string

except Exception as error: # general unspesified error.
    print(f"An error has occurred: {error}")  # Added f-string
