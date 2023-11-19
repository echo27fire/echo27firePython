'''
Name: Taylor Goodspeed
Date Oct 7, 2023
Class: CSC 121
Progarm: Lottery number generator.
'''


# Import required libraries
import random

# Functions
def display_numbers(lottery_numbers):
    '''
    Display function for 7-digit lottery numbers.
    '''
    print("The numbers generated for this lottery draw are:", end=' ') # intro sentance, end=' ' stops a newline from forming.
    for number in lottery_numbers:  # loop through each number in the lottery list.
        print(number, end='')  # print numbers w/o adding extra characters or spaces.


def main():
    '''
    Generate a 7-digit lottery number.
    Numbers are selected in a pool range of 0-9.
    Numbers are stored in a list, then displayed in the output.
    '''
    
    LOTTERY_LENGTH = 7  # Declare a constant to specify the length of the lottery number
    lottery_numbers = []  # Initialize an empty list to store the generated lottery numbers
    
    # Loop LOTTERY_LENGTH to generate each number for the draw
    for _ in range(LOTTERY_LENGTH):
        num = random.randint(0, 9)  # Generate a random number between 0 and 9
        lottery_numbers.append(num)  # Append the generated number to the lottery_numbers list
    
    # Call the display_numbers function to display the generated lottery number
    display_numbers(lottery_numbers) 


# Invoke main & program start
if __name__ == '__main__':
    main()
