import sys
import os

def input_file():
    file_to_examine = input("Enter the filename / path of the .py file to examine: ") #user input for the file to examine later

    if not file_to_examine.endswith('.py'): # determine if the file has the correct extension
        print("This does not appear to be a Python code file")
        sys.exit(1)  # Exit if not a Python file

    if not os.path.exists(file_to_examine):
        print(f"There does not appear to be a file called {file_to_examine}. Verify path / filename.") #verify that the file exisits
        sys.exit(1)  # Exit if file does not exist
# code exits after these steops to allow the user access to term and verify name / path of file.

    return file_to_examine # file has passed checks and input is returned to rest of script

def examine_file(file_to_examine):
    line_count = 0 # init line_count at 0
    with open(file_to_examine, 'r') as file:
        for line in file:
            line = line.strip() #remove white space 
            if line == '' or line.startswith('#'): #determine if a line is blank or starts with # and thus not counted.
                continue
            line_count += 1 #increment actual lines of code
    print(f"The number of lines of code in {file_to_examine} is {line_count}") # printe results

def main(): # define the main function
    file_to_examine = input_file() #call the input file function and pass result to file_to_examine var.
    examine_file(file_to_examine) #call examine_file function,


main()
