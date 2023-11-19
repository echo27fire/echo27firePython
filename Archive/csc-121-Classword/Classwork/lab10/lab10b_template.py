"""
Name:
Date:
Description:  lab10b - String Operation Practice
"""

# Part 1:  Accessing Strings - POSITIVE and NEGATIVE Index
# You are given the following string for all questions in this part.
mystr = "fall for leaves"  #DO NOT CHANGE THIS

#Q1: Write a print statement like:  print(f"{mystr[YOUR_INDEX_HERE]}") that will output "f", where
# YOUR_INDEX_HERE is replaced by a NON-NEGATIVE number
# Expected output:
# f


#Q2: Write a print statment like:  print(f"{mystr[YOUR_INDEX_HERE]}") that will output "s", where
# YOUR_INDEX_HERE is replaced by a NON-NEGATIVE number
# Expected output:
# s


#Q3: Write a print statment like:  print(f"{mystr[YOUR_INDEX_HERE]}") that will output "s", where
# YOUR_INDEX_HERE is replaced by a NEGATIVE number
# Expected output:
# s


# Part 2:  Slicing Strings
# You are given the following string for all questions in this Part.
mystr = "fall for leaves"   #DO NOT CHANGE THIS

#Q4: Write a print statement like:  print(f"{mystr[YOUR_START:YOUR_STOP:YOUR_STEP]}") that will output "all", where
# YOUR_START, YOUR_STOP, and YOUR_STEP are replaced by numbers.  You may use less than 3 values in your print statement.
# Expected output:
# all


#Q5: Write a print statement like:  print(f"{mystr[YOUR_START:YOUR_STOP:YOUR_STEP]}") that will output "leave", where
# YOUR_START, YOUR_STOP, and YOUR_STEP are replaced by numbers.  You may use less than 3 values in your print statement.
# Make YOUR_START a NON-NEGATIVE number, and YOUR_STOP a NEGATIVE number.
# Expected output:
# leave


#Q5: Write a print statement like:  print(f"{mystr[YOUR_START:YOUR_STOP:YOUR_STEP]}") that will output "alf", where
# YOUR_START, YOUR_STOP, and YOUR_STEP are replaced by numbers.  You will need 3 values for this, and YOUR_STEP
# should be a POSITIVE number.
# Expected output:
# alf


#Q7: Write a print statment like:  print(f"{mystr[YOUR_START:YOUR_STOP:YOUR_STEP]"}) that will output "lfrl", where
# YOUR_START, YOUR_STOP, and YOUR_STEP are replaced by numbers.  YYou will need 3 values for this, and YOUR_STEP
# # should be a NEGATIVE number.
# Expected output:
# sve


# Part 3:  String Methods and Built-in Python Functions
# You are given the following strings for all questions in this part.
mystr = "the cat goes Meow."  # DO NOT CHANGE THIS
otherstr = "cookies>milk>fudge>cake>ice cream"   # DO NOT CHANGE THIS

#Q8: Write a print statement like:  print(f"The length of the string is: {YOUR_CODE_HERE}") that will output the
# length of the string.  Use a built-in python function.
# Expected output:
# The length of the string is: 18


#Q9: Write a print statement like:  print(f"The words in the string are: {YOUR_CODE_HERE]") that will output the
# list of words in the string.  Use a built-in python method.
# Expected output:
# The words in the string are: ["the","cat","goes","Meow."]



#Q10: Write a print statement like:  print(f"The words in the string are: {YOUR_CODE_HERE]") that will output the
# list of words in the string from string otherstr.  Use a built-in python method.
# Expected output:
# The words in the other string are:  ['cookies', 'milk', 'fudge', 'cake', 'ice cream']


#Q11:  Write a print statement like:  print(f"{mystr.YOUR_METHOD_HERE()}") that will
# output the following: "The cat goes meow."    Use a python string method.
# Expected output:
# The cat goes meow.


#Q12:  Write a print statement like:  print(f"{mystr.YOUR_METHOD_HERE()}") that will
# output the following: "THE CAT GOES MEOW."    Use a python string method.
# Expected output:
# THE CAT GOES MEOW.


#Q13:  Write a print statement like:  print(f"{mystr.YOUR_METHOD_HERE()}") that will
# output the following: "the cat goes meow."    Use a python string method.
# Expected output:
# the cat goes meow.


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

#Q15 Write a print statement that uses the REPETITION OPERATOR to display the provided string onestr
# five times.  print(f"Repeated string is: {YOUR_CODE_HERE}")
# Expected output:
# Repeated string is: HappyHappyHappyHappyHappy
onestr = "Happy"   # DO NOT CHANGE THIS
# Uncomment this line and fill in YOUR_CODE_HERE
# print(f"Repeated string is: {YOUR_CODE_HERE}")


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

#Q17:  Write a loop to determine how many characters in a string are numeric digits.
# Display the count of numeric digits.  Use a python string method to check if each
# position in the string is a numeric digit.  print(f"There are {count} numeric digits.")
# Expected output:
# There are 6 numeric digits.
mystr = "The weather at 287 West 34th Street was humid.  I thought it was Gr8." # DO NOT CHANGE THIS
# print(f"There are {count} numeric digits.")

#Q18:  Write a loop to determine how many characters in a string are alphabetic.
# Display the count of alphabetic digits.  Use a python string method to check if each
# position in the string is alphabetic.  print(f"There are {count} alphabetic characters.")
# Expected output:
# There are 29 alphabetic characters.
mystr = "Fred lives at 287 West 34th Street, London."  # DO NOT CHANGE THIS
#print(f"There are {count} alphabetic characters.")

#Q19:  Write a loop to determine how many characters in a string are upper case/capital letters.
# Display the count.  print(f"There are {count} upper case characters.")
# Expected output:
# There are 11 upper case characters.
mystr = "Sun, Wind, and Fire.  All 3 are FORCES of Nature."  # DO NOT CHANGE THIS
#print(f"There are {count} upper case characters.")

#Q20:  Write your own question, demonstrating a *different* concept you learned in this
# lesson, either in the text, videos, or independent research.  Write your question with
# (following the model shown above), including your expected output.
# Then write the solution to your question.

# YOUR QUESTION - Write your Question here, including Expected Output

# SOLUTION - Write your Solution to Your Question Q20 here.
