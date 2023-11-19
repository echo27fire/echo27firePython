'''
Author: Taylor Goodspeed
Date: 10/28/2023
Class: CSC-121
Program: LAB10-C.py
'''

'''
Write a program that asks the user to enter a 10-digit character telephone number in the format XXX-XXX-XXXX.
The application should display the telephone number with any alphabetic characters that appeared in the original
translated to their numeric equivalent.
For example, if the user enters 555-GET-FOOD, the application should display 555-438-3663.
'''

PHONE_LETTER_NUMBER_DICT = {
    'A': '2', 'B': '2', 'C': '2',
    'D': '3', 'E': '3', 'F': '3',
    'G': '4', 'H': '4', 'I': '4',
    'J': '5', 'K': '5', 'L': '5',
    'M': '6', 'N': '6', 'O': '6',
    'P': '7', 'Q': '7', 'R': '7', 'S': '7',
    'T': '8', 'U': '8', 'V': '8',
    'W': '9', 'X': '9', 'Y': '9', 'Z': '9'
}

def get_user_number():
    """
    Prompts the user to enter a 10-digit number in the format XXX-XXX-XXXX and returns the input as a string.

    Returns:
    str: The user's input as a string.
    """
    return input("Enter a 10-digit number to convert in the format XXX-XXX-XXXX: ").upper()

def convert_to_number(phone_input):
    """
    Converts a phone number string with letters to a phone number string with numbers.

    Args:
        phone_input (str): The phone number string to convert.

    Returns:
        str: The converted phone number string.
    """
    return ''.join([PHONE_LETTER_NUMBER_DICT.get(char, char) for char in phone_input])



def display_conversion(converted_input):
    """
    Displays the converted number.

    Parameters:
    converted_input (float): The converted number to be displayed.

    Returns:
    None
    """
    print(f"The converted number is {converted_input}")

if __name__ == "__main__":
    phone_input = get_user_number()
    converted_input = convert_to_number(phone_input)
    display_conversion(converted_input)
