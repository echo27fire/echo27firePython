'''
Author: Taylor Goodspeed
Date: 10/28/2023
Class: CSC-121
Description:  lab10b - String Operation Practice
'''



# Part 1:  Accessing Strings - POSITIVE and NEGATIVE Index
# You are given the following string for all questions in this part.
mystr = "fall for leaves"  #DO NOT CHANGE THIS

#Q1: Write a print statement like:  print(f"{mystr[YOUR_INDEX_HERE]}") that will output "f", where
# YOUR_INDEX_HERE is replaced by a NON-NEGATIVE number
# Expected output:
# f

print("Q1")
print(f"{mystr[0]}")
print("\n")

#Q2: Write a print statment like:  print(f"{mystr[YOUR_INDEX_HERE]}") that will output "s", where
# YOUR_INDEX_HERE is replaced by a NON-NEGATIVE number
# Expected output:
# s

print("Q2")
print(f"{mystr[14]}")
print("\n")

#Q3: Write a print statment like:  print(f"{mystr[YOUR_INDEX_HERE]}") that will output "s", where
# YOUR_INDEX_HERE is replaced by a NEGATIVE number
# Expected output:
# s

print
print(f"{mystr[-1]}")
print("\n")



# Part 2:  Slicing Strings
# You are given the following string for all questions in this Part.
mystr = "fall for leaves"   #DO NOT CHANGE THIS

#Q4: Write a print statement like:  print(f"{mystr[YOUR_START:YOUR_STOP:YOUR_STEP]}") that will output "all", where
# YOUR_START, YOUR_STOP, and YOUR_STEP are replaced by numbers.  You may use less than 3 values in your print statement.
# Expected output:
# all

print("Q4")
print(f"{mystr[1:4]}")
print("\n")

#Q5: Write a print statement like:  print(f"{mystr[YOUR_START:YOUR_STOP:YOUR_STEP]}") that will output "leave", where
# YOUR_START, YOUR_STOP, and YOUR_STEP are replaced by numbers.  You may use less than 3 values in your print statement.
# Make YOUR_START a NON-NEGATIVE number, and YOUR_STOP a NEGATIVE number.
# Expected output:
# leave

print("Q5")
print(f"{mystr[9:-1]}")
print("\n")

#Q6: Write a print statement like:  print(f"{mystr[YOUR_START:YOUR_STOP:YOUR_STEP]}") that will output "alf", where
# YOUR_START, YOUR_STOP, and YOUR_STEP are replaced by numbers.  You will need 3 values for this, and YOUR_STEP
# should be a POSITIVE number.
# Expected output:
# alf

# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
# f a l l   f o r   l  e  a  v  e  s"

print("Q6")
print(f"{mystr[1:7:2]}")
print("\n")

#Q7: Write a print statment like:  print(f"{mystr[YOUR_START:YOUR_STOP:YOUR_STEP]"}) that will output "lfrl", where
# YOUR_START, YOUR_STOP, and YOUR_STEP are replaced by numbers.  YYou will need 3 values for this, and YOUR_STEP
# # should be a NEGATIVE number.
# Expected output:
# sve

# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
# f a l l   f o r   l  e  a  v  e  s"
print("Q7")
print(f"{mystr[14:9:-2]}")
print("\n")


# Part 3:  String Methods and Built-in Python Functions
# You are given the following strings for all questions in this part.
mystr = "the cat goes Meow."  # DO NOT CHANGE THIS
otherstr = "cookies>milk>fudge>cake>ice cream"   # DO NOT CHANGE THIS

#Q8: Write a print statement like:  print(f"The length of the string is: {YOUR_CODE_HERE}") that will output the
# length of the string.  Use a built-in python function.
# Expected output:
# The length of the string is: 18

print("Q8")
print(f"The length of the string is: {len(mystr)}")
print("\n")


#Q9: Write a print statement like:  print(f"The words in the string are: {YOUR_CODE_HERE]") that will output the
# list of words in the string.  Use a built-in python method.
# Expected output:
# The words in the string are: ["the","cat","goes","Meow."]

print("Q9")
print(f"The string has the words: {mystr.split()}")


#Q10: Write a print statement like:  print(f"The words in the string are: {YOUR_CODE_HERE]") that will output the
# list of words in the string from string otherstr.  Use a built-in python method.
# Expected output:
# The words in the other string are:  ['cookies', 'milk', 'fudge', 'cake', 'ice cream']

print("Q10")
print(f"The string has the words: {otherstr.split('>')}")
print("\n")




#Q11:  Write a print statement like:  print(f"{mystr.YOUR_METHOD_HERE()}") that will
# output the following: "The cat goes meow."    Use a python string method.
# Expected output:
# The cat goes meow.

print("Q11")
print(f"{mystr.lower().capitalize()}")
print("\n")



#Q12:  Write a print statement like:  print(f"{mystr.YOUR_METHOD_HERE()}") that will
# output the following: "THE CAT GOES MEOW."    Use a python string method.
# Expected output:
# THE CAT GOES MEOW.

print("Q12")
print(f"{mystr.upper()}")
print("\n")

#Q13:  Write a print statement like:  print(f"{mystr.YOUR_METHOD_HERE()}") that will
# output the following: "the cat goes meow."    Use a python string method.
# Expected output:
# the cat goes meow.

print("Q13")
print(f"{mystr.lower()}")
print("\n")


#Q14:  Write a print statement like:  print(f"Is {searchword} in otherstr? {YOUR_CODE_HERE}") that will
# indicate True if the searchword is in the string otherstr.
# Test your code with the two provided searchword, using string otherstr.
# Expected output:
# Is cookies in otherstr? True
# Is chocolate in otherstr? False
searchword1 = "cookies"          # DO NOT CHANGE THIS
searchword2 = "chocolate"       # DO NOT CHANGE THIS
# Uncomment these lines and fill in YOUR_CODE_HERE
# print(f"Is {searchword1} in otherstr? {YOUR_CODE_HERE}")
# print(f"Is {searchword2} in otherstr? {YOUR_CODE_HERE}")

print("Q14")
print(f"Is {searchword1} in otherstr", searchword1 in otherstr)
print(f"Is {searchword2} in otherstr", searchword2 in otherstr)
print("\n")


#Q15 Write a print statement that uses the REPETITION OPERATOR to display the provided string onestr
# five times.  print(f"Repeated string is: {YOUR_CODE_HERE}")
# Expected output:
# Repeated string is: HappyHappyHappyHappyHappy
onestr = "Happy"   # DO NOT CHANGE THIS
# Uncomment this line and fill in YOUR_CODE_HERE
# print(f"Repeated string is: {YOUR_CODE_HERE}")

print("Q15")
print(f"Repeated string is: {onestr * 5}")
print("\n")


# Part 4:  Putting Things Together
# You are given different strings for each question in this part.

#Q16:  Using the following string "X-DSPAM-Confidence: 0.8475".
# Use find and string slicing to extract the portion of the string after the colon character and
# then use the float function to convert the extracted string into a floating point number called num.
# print out the numeric value of num + 1 using print(f"One larger than num is {num + 1:.4f}")
# Hint:  Create a variable say start_index and use the find method to find the index of the colon
# in string mystr.  Then use string slicing to get the numeric part of the string: "0.8475".  Finally
# use the float type converter to make that string a floating point number, and print it out with 4
# digits after the decimal point.
# Expected output:
# One larger than num is:  1.8475
mystr = "X-DSPAM-Confidence: 0.8475"  # DO NOT CHANGE THIS
# num = YOUR_CODE_HERE
# print(f"One larger than num is {num + 1:.4f}")

print("Q16")
index_start = mystr.find(':')
num_str = mystr[index_start + 1:].strip()
num = float(num_str)
print(f"One larger than num is {num + 1:.4f}")
print("\n")





#Q17:  Write a loop to determine how many characters in a string are numeric digits.
# Display the count of numeric digits.  Use a python string method to check if each
# position in the string is a numeric digit.  print(f"There are {count} numeric digits.")
# Expected output:
# There are 6 numeric digits.
mystr = "The weather at 287 West 34th Street was humid.  I thought it was Gr8." # DO NOT CHANGE THIS
# print(f"There are {count} numeric digits.")

count = 0
for char in mystr:
    if char.isdigit():
        count += 1

print("Q17")        
print(f"There are {count} numeric digits.")
print("\n")





#Q18:  Write a loop to determine how many characters in a string are alphabetic.
# Display the count of alphabetic digits.  Use a python string method to check if each
# position in the string is alphabetic.  print(f"There are {count} alphabetic characters.")
# Expected output:
# There are 29 alphabetic characters.
mystr = "Fred lives at 287 West 34th Street, London."  # DO NOT CHANGE THIS
#print(f"There are {count} alphabetic characters.")

print("Q18")

count = 0
for char in mystr:
    if char.isalpha():
        count += 1

print(f"There are {count} alphabetic characters.")
print("\n")




#Q19:  Write a loop to determine how many characters in a string are upper case/capital letters.
# Display the count.  print(f"There are {count} upper case characters.")
# Expected output:
# There are 11 upper case characters.
mystr = "Sun, Wind, and Fire.  All 3 are FORCES of Nature."  # DO NOT CHANGE THIS
#print(f"There are {count} upper case characters.")

print("Q19")
count = 0
for char in mystr:
    if char.isupper():
        count += 1
print(f"there are {count} upper case characters.")

print("\n")






#Q20:  Write your own question, demonstrating a *different* concept you learned in this
# lesson, either in the text, videos, or independent research.  Write your question with
# (following the model shown above), including your expected output.
# Then write the solution to your question.




# YOUR QUESTION - Write your Question here, including Expected Output
# P1 - Can you write a program to convert the following Morse code back to text?
# "- .... .. ... / .. ... / . -. -.-. .-. -.-- .--. - . -.. / .. -. / -- --- .-. ... . / -.-. --- -.. ."
# expected output: This is encrypted in morse code

# P2 - Expand the code take in the input "I like to write in morse code!" and convert it to morse code
# expected output:  ..  /  .-.. .. -.- .  /  - ---  /  .-- .-. .. - .  /  .. -.  /  -- --- .-. ... .  /  -.-. --- -.. . -.-.--

# P3 - write code that

# SOLUTION - Write your Solution to Your Question Q20 here.

# morse code dictionary, DO NOT CHANGE THIS
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ',': '--..--', '.': '.-.-.-',
    '?': '..--..', '!': '-.-.--', "'": '.----.',
    ' ': ' / '
}
# Function to convert morse code to text
def convert_morse_to_text(morse_code):
    """
    Converts a string of Morse code to plain text.

    Args:
        morse_code (str): A string of Morse code.

    Returns:
        str: The decoded message in plain text.
    """
    words = morse_code.split(' / ')
    decoded_words = []
    
    for word in words:
        letters = word.split(' ')
        decoded_word = ''
        for letter in letters:
            matching_keys = [k for k, v in MORSE_CODE_DICT.items() if v == letter]
            if matching_keys:  # Check if the list is not empty
                decoded_word += matching_keys[0]
        decoded_words.append(decoded_word)
    
    decoded_message = ' '.join(decoded_words)
    return decoded_message.capitalize()


# function to convert text to morse code
def string_to_morse(input_string):
    """
    Converts a given string to its equivalent morse code representation.

    Args:
        input_string (str): The string to be converted to morse code.

    Returns:
        str: The morse code representation of the input string.
    """
    uppercase_input = input_string.upper()
    morse_list = [MORSE_CODE_DICT[char] for char in uppercase_input if char in MORSE_CODE_DICT]
    return ' '.join(morse_list)


# Decode from Morse to Text
#code = "- .... .. ... / .. ... / . -. -.-. .-. -.-- .--. - . -.. / .. -. / -- --- .-. ... . / -.-. --- -.. ."
code = " -- --- .-. ... .  /  -.-. --- -.. .  /  -.-. --- -. ...- . .-. - . -.. .-.-.-  /  - .... .. ...  /  .. ...  /  - .... .  /  .- -. ... .-- . .-.  /  ..-. --- .-.  /  - .... .  /  ..-. .. .-. ... -  /  .--. .- .-. -  /  --- ..-.  /  --.- ..--- ----- -.-.--"
result = convert_morse_to_text(code)
print(f"The decoded text is: \n {result}")

# Encode from Text to Morse
user_input = input("Enter a string to convert to morse code: ")
result = string_to_morse(user_input)
print(f"The morse code for '{user_input}' is: \n {result}")


