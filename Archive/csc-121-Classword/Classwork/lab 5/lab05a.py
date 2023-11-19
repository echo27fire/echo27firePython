'''
Author: Taylor Goodspeed
Date: Sep 16, 2023
Class: CSC 121 FA23
Program: lab05a
'''

# functions

def feet_to_inches(feet): #define feet -> inches conversion
    # Multiply the number of feet by 12 to get the equivalent length in inches
    inches = feet * 12
    return inches

# Main code body
try:
    # Prompt the user to input the number of feet (allowing for fractional values)
    feet = float(input("How many feet would you like to convert to inches?: "))
    
    # Call the conversion function
    inches = feet_to_inches(feet)
    
    # Display the conversion result, rounded to two decimal places
    print(f"{feet} feet is equal to {inches:.2f} inches.")
except ValueError:
    # Handle invalid with an error message
    print("Invalid input. Please enter a valid number.")
