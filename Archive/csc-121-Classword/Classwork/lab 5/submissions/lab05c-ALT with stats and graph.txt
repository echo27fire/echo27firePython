'''
Author: Taylor Goodspeed
Date: Sep 16, 2023
Class: CSC 121 FA23
Program: lab05b
'''

#import statistics
#import matplotlib.pyplot as plt


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


# The calc_statistics function is dependant on the 'statistics module, uncomment line 8 and the function call in main()
# when uncommenting the module import, ensure prper formatting otherwise there will be an error. Noted error for improper tab.
def calc_statistics(scores):
    mean_score = statistics.mean(scores)
    std_dev_score = statistics.stdev(scores)
    print(f"The mean score is: {mean_score}")
    print(f"The standard deviation of the scores is: {std_dev_score}")


# The disp_statistics function is dependant on installing the matplotlib module and importing it as plt.
# this function will generate a new window with a graph showing the test score results and statistical information.
# install with: pip install matplotlib
# uncomment function call at end of main() to use as well as line 9
# refer to https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html for documentation.
def disp_statistics(scores):
    plt.hist(scores, bins=range(0, 101, 10), edgecolor='black')
    plt.title('Distribution of Test Scores')
    plt.xlabel('Test Score')
    plt.ylabel('Frequency')
    plt.show()



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


# uncomment these lines to call the respective functions, also ensure the appropriate module at the top is uncommented as well.
    #calc_statistics(scores)
    #disp_statistics(scores)


# start program with main function call.
main()
