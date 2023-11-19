'''
Auth: Taylor Goodspeed
Date: Sep 23, 2023
Class: CSC 121
Program: lab06b

'''


# variables
numerator = 27 # 'top' value
denominator = 0 # 'bottom' value 


# try variables a nd return result if 
try:  # try variables a and return result
    result = numerator / denominator
except ZeroDivisionError: # runs on if attempting to devide by 0
    print("you cannot devide by zero (0). Setting result to 'none'") #notify user that attempting to devide by 0 is not allowed
    result = None # none 'switch' set result to nothing if attempting to devide by 0

if result is not None: # checks if the none 'switch' is flipped
    print(f"{result} is the result of this division operation")
else: #if result is None, print error message
    print("an error has occured and division can not be preformed. ")