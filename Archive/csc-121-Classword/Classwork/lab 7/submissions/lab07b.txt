'''
Author: Taylor G.
Date: Sep 30, 2023
Class: CSC 121
Program: lab07a - file average
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

try:  # Phase 1: Attempt to open the file
    num_sum = 0
    count = 0

    # Added line for debugging. Uses the module from the import os to display the current working path of the script.
    print(os.getcwd()) 

    with open(open_file, "r") as num_file:  # Open the file variable in "r" or read-only mode
        for line in num_file:  # Loop through lines in the text file
            try:
                number = int(line.strip())  # Reads the line in the file, removes whitespace, and converts to an integer.
                num_sum += number 
                count += 1
            except ValueError:  # Error if a line in the file is 'bad'
                print(f"Invalid line detected: {line.strip()}")

    if count == 0:  # If no valid numbers are detected, print an error that this is so.
        print(f"There were no valid numbers detected in {open_file}")
    else:
        ave = num_sum / count  # Calculate the average
        print(f"The average of numbers in {open_file} is {ave}")

except FileNotFoundError:  # Error message if the file under 'open_file' variable cannot be found
    print(f"The file {open_file} is not found. Check the file path variable")  

except Exception as error:  # General unspecified error.
    print(f"An error has occurred: {error}")
