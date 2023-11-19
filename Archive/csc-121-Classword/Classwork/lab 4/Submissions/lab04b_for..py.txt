'''
Name: Taylor Goodspeed
Class: CSC 121
Date: September 9, 2023
Program: lab04b
'''

'''
#demo code
age = input("How old are you? ")
age = int(age)
print("Happy Birthday To You ! ")
for i in range(age):
    print(f"Are you {i+1}")
'''

Guess = 0 # Guess var init. 
Age = int(input('How old are you?: ')) # Age input
for Guess in range(Age): # for loop to cycle through age guesses
    print(f'Happy BirthDay!!! Are you {Guess+1} years old?') # loop output, print message and Guess var. +1 until it matches input.
    
