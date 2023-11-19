'''
Auth: Taylor Goodspeed
Date: Sep 23, 2023
Class: CSC 121
Program: lab06a
'''

# Variables
total = 0
count = 0

while True:
    userIn = input("Please enter a number or press Enter to end: ")

    if userIn == "":  # Test if user input is 'blank' or just Enter was pressed
        break  # Break loop, move to testing numbers

    try:
        number = float(userIn)
        total += number  # Add input number to total
        count += 1  # Iterate number count for each input
    except ValueError:  # Catch invalid input
        print("You have input an invalid number, please try again.")

try:
    average = total / count  # Calculate average, then print. average = sum of all nums / number of entries iterated
    print(f"The average of the entered numbers is {average:.2f}")
except ZeroDivisionError:  # Catch zero division
    print("You have submitted invalid number(s). Unable to continue.")
