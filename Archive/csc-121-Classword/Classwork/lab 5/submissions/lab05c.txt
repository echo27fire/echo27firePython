'''
Author: Taylor Goodspeed
Date: Sep 16, 2023
Class: CSC 121 FA23
Program: lab05b
'''

# Define a function to calculate the average of test scores
# *tests allows for a vaiable number of inputs to pass to the function. Cleaner and tidyer code.
def calc_average(*tests):
    return sum(tests) / len(tests)

# function to determine the grade corresponding to a score
# The function takes a score as input and returns the fixed scale letter grade.
def determine_grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score <= 89:
        return 'B'
    elif 70 <= score <= 79:
        return 'C'
    elif 60 <= score <= 69:
        return 'D'
    else:
        return 'F'

# primary function for calling the program.
def main():
    # collect 5 scores from the user
    # Prompt the user to input each score and enter into a list
    scores = [float(input(f"Enter your scores now: #{i+1}: ")) for i in range(5)]
    
    # Loop through each score to determine and display the corresponding grade
    # Enumerate through scores to get index and score for displaying score number and grade
    # TIL: Enumerate function adds a counter to an iterable, can access both the index and value in a loop. neat!
    for i, score in enumerate(scores):
        print(f"Score #{i+1} ({score}) is graded as: {determine_grade(score)}")
    
    # Calculate the average score using the previously defined function
    # Display the average score and its corresponding grade with two decimal places for the score
    average_score = calc_average(*scores)
    print(f"The average score is {average_score:.2f}")
    print(f"The average grade is: {determine_grade(average_score)}")

# start program with main function call.
main()
