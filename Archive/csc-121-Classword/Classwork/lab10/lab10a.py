from collections import Counter

'''
Author: Taylor Goodspeed
Date: 10/28/2023
Class: CSC-121
Program: lab10-A.py
'''

'''
objective:

Write a program with a function that accepts a string as an argument and returns the number of vowels
that the string contains.  The application should have another function that accepts a string as an
argument and returns the number of consonants that the string contains.  The application should let
the user enter a string, and should display the number of vowels and the number of consonants it contains. 
'''

# global variables
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'


def vowel_countO(input_string):
    """
    This function takes a string as input and returns the number of vowels in the string.
    """
    vowel_count = 0
    for char in input_string.lower():
        if char in vowels:
            vowel_count += 1
    return vowel_count


def conts_count(input_string):
    """
    This function takes a string as input and returns the number of consonants in the string.
    """
    consonants_count = 0
    for char in input_string.lower():
        if char in consonants:
            consonants_count += 1
    return consonants_count

from collections import Counter

def display_counts(input_string):
    """
    This function takes a string as input and displays the count of each vowel and consonant in the string.
    
    Args:
    input_string (str): The string to be analyzed.
    
    Returns:
    None
    """
    input_string = input_string.lower()
    
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    
    char_count = Counter(input_string)
 
    individual_vowel_counts = {char: char_count[char] for char in vowels if char in char_count}
    individual_consonant_counts = {char: char_count[char] for char in consonants if char in char_count}
    
    print("Vowel counts: ")
    for vowel, count in individual_vowel_counts.items():
        print(f"{vowel}: {count}")
        
    print("Consonant counts: ")
    for consonant, count in individual_consonant_counts.items():
        print(f"{consonant}: {count}")


# main code block
if __name__ == "__main__":
    input_string = input("Enter a string: ")
    print("The number of vowels in the string is", vowel_countO(input_string))
    print("The number of consonants in the string is", conts_count(input_string))
    print("The count of each vowel and consonant in the string is: ")
    display_counts(input_string)
