'''
Author: Taylor Goodspeed
Date: Sep 1, 2023
Class: CSC 121
Assignment: lab03b
'''

# Functions

# Program start
print("-----------------------------------")
print("This is where the fun begins!")
print("-----------------------------------\n\n")

age_in = input("What is your age?: ")
age = float(age_in)  # Correct the variable name
print(f"The age you have inputted is {age}\n")  # Use f-string for the age variable

'''
Calculation rules:
Negative age: Display error message.
0-1 yr = Infant
1-13 = Child
13-20 = Teenager
20-100 = Adult
100+ = Centenarian
'''

# Note: do not use <= for upper limit: incorrect results because upper limit will not properly trigger.
if age < 0:  #Test1 Catch if age is negative
    print('ERROR: Age invalid')
elif age >= 0 and age < 1:  # Test2 if age is between 0 and 1: Infant
    print('This person is an infant!')
elif age >= 1 and age < 13:  # Test3 if age is at least 1 but less than 13: Child
    print('This person is a child!')
elif age >= 13 and age < 20:  # Test4 if age is at least 13 but less than 20: Teenager
    print('This person is a teenager!')
elif age >= 20 and age < 100:  # Test5 if age is at least 20 but less than 100: Adult
    print('This person is an adult!')
else:  # test6 Catch if age is 100 or more
    print('This person is a centenarian!')
