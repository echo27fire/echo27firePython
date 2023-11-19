'''
Author: Taylor G.
Date: Sep 30, 2023
Class: CSC 121
Program: lab07a - random number file creator +average calc of numbers generated. 
'''


import random
import os

def generate_random_numbers():  # random number file function.
    random_file = "lab07c_output.txt" # the file / path to write generated numbers to
    
    # this section uses functions from OS mod. to test of the file can actually be written before asking for input.
    directory = os.path.dirname(os.path.abspath(random_file))
    if not os.access(directory, os.W_OK): # if write is no 'ok' generate an error 
        print(f"ERROR: cannot continue path to write {random_file} is not writable")
        return  # Added return to stop function if path is not writable
    
    try:
        number_count = int(input("How many random numbers should be generated: ")) # ask user for input: how many numbers to generate.
    except ValueError:
        print("ERROR: input a valid whole number only.") #error if an invalid input is entered
        generate_random_numbers()  #call the function again to retry input.
        return

    with open(random_file, "w") as output_file:  #open the file to write, output_file is used as handle in this section.
        for _ in range(number_count):  
            random_number = random.randint(1, 500) #(1, 500) is the range of random numbers can be generated in.
            output_file.write(str(random_number) + "\n")  #write the random number to the file and create a newline.

    print(f"{number_count} random numbers have been generated and written to {random_file}") #message when output is complete.


# to use this, be sure function call in `def main()` is uncommented.
def average_calc():
    random_file = "lab07c_output.txt"
    try:  # Phase 1: Attempt to open the file
        num_sum = 0
        count = 0

        # Added line for debugging. Uses the module from the import os to display the current working path of the script.
        print(os.getcwd()) 

        with open(random_file, "r") as num_file:  # Open the file variable in "r" or read-only mode
            for line in num_file:  # Loop through lines in the text file
                try:
                    number = int(line.strip())  # Reads the line in the file, removes whitespace, and converts to an integer.
                    num_sum += number 
                    count += 1
                except ValueError:  # Error if a line in the file is 'bad'
                    print(f"Invalid line detected: {line.strip()}")

        if count == 0:  # If no valid numbers are detected, print an error that this is so.
            print(f"There were no valid numbers detected in {random_file}")
        else:
            ave = num_sum / count  # Calculate the average
            print(f"The average of numbers in {random_file} is {ave}")

    except FileNotFoundError:  # Error message if the file under 'open_file' variable cannot be found
        print(f"The file {random_file} is not found. Check the file path variable")  

    except Exception as error:  # General unspecified error.
        print(f"An error has occurred: {error}")


# main function
def main():
    # comment / uncommnet functions to toggle their use off / on.
    generate_random_numbers()  #call random number function.
    #average_calc() # call the average number function.

main()



