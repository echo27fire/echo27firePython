'''
Author: Taylor Goodspeed
Date: Sep 16, 2023
Class: CSC 121 FA23
Program: lab05b
'''
import random

def random_counter():
    # Initialize counters for even and odd numbers
    even_count = 0
    odd_count = 0

    # Loop 100 times to generate 100 random numbers
    for _ in range(100):
        # Determine a random lower bound between 0 and a random number between 0 and 100
        lower_bound = random.randint(0, random.randint(0, 100))
        
        # Determine a random upper bound that is always greater than the lower bound
        upper_bound = random.randint(lower_bound, random.randint(lower_bound + 1, 100))
        
        # Generate a random number within the range defined by lower_bound and upper_bound
        number = random.randint(lower_bound, upper_bound)
        
        # Check if the generated number is even or odd and increment the respective counter
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    # Print the total counts of even and odd numbers generated
    print(f"Even numbers: {even_count}")
    print(f"Odd numbers: {odd_count}")

def main():
    # Invoke the random_counter function to execute the random number generation and counting
    random_counter()

# Call the main function to run the program
main()


'''
Additional Notes:
this program can be greatly expanded and used in other areas.
1. add a-z and symbols: password generator, specify length.
2. add letters and increase length, API / secure password generator
3. dictionary call? passprase generator? 

other thoughts:

bind script to hot key on Stream Deck and to quickly exicute if indeed of random numbers :)
'''
