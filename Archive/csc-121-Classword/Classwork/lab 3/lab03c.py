'''
Author: Taylor Goodspeed
Date: Sep 1, 2023
Class: CSC 121
Assignment: lab03c - Golf Calculator.
'''

# Program Guidelines
'''
Invalid par: value is not 3, 4, 5
Eagle: strokes are two less than par.
Birdie: strokes are one less than par.
Par: strokes == par 
Bogey: strokes are 1 greater than par.
No match: output not caught by above rules.
'''

# functions


# Program Start
par_in = int(input('What is par for this hole?: '))

if par_in not in [3, 4, 5]:
    print('Invalid par input detected.')
else: # stroke processing is required to be tested under else, otherise will process regardless of bad par input
    strokes_in = int(input('How many strokes did you record for this hole of golf?: '))
    if strokes_in == par_in - 2: # Test if Eagle is achieved
        print("You got an Eagle!") # display result
    elif strokes_in == par_in - 1: # Test if Birdie is achieved
        print("You got an Birdie!") # display result
    elif strokes_in == par_in: # Test if par is achieved
        print("You got par!") # display result
    elif strokes_in == par_in + 1: # Test if Bogey is achieved
        print("You got a Bogey!") # display result
    else: # catch for other results
        print('Not sure what that score is, but we might not want to talk about it :)')

'''
code future:
add:
hole in 1
add double eagle
add double and tribble bogey
additional holes
    track all 18 holes
    calculate total score.
'''