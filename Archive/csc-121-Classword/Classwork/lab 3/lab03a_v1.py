'''
Author: Taylor Goodspeed
Date: Sep 1, 2023
Class: CSC 121
Assignment: lab03a v1 - if elif else tree
'''

# Functions
def AreaCalc(width, height):
    return width * height

# ------------------------------------------------------------------------------------------------------

# Program Start
# Gather info on rectangle 1 (r1)
print("-----------------------------------")
print("This is where the fun begins!")
print("-----------------------------------")
print("Let's get the dimensions of the first rectangle, shall we?\n")  # new line break

# r1 width
width1_in = input('What is the width of rectangle 1?: ')  # r1 width input
width1 = float(width1_in)  # converts r1 width input and saves to width1 as float
print(f"So the width is {width1}? Neat!\n")  # r1 width input, new line break

# r1 height
height1_in = input('Now, what is the height?: ')  # r1 height input
height1 = float(height1_in)  # converts r1 height input and saves to height1 as float
print(f"Height of {height1} has been noted. Thanks!\n")  # r1 height input, new line break

# Next line calls AreaCalc and saves area to Area1
Area1 = AreaCalc(width1, height1)  # call AreaCalc and save result to Area1

# ------------------------------------------------------------------------------------------------------

# Rectangle 2 (r2)
print("-----------------------------------")
print("Great, now let's move on to the second rectangle.")
print("-----------------------------------")
print("Let's get the dimensions of the second rectangle, shall we?")

# r2 width
width2_in = input('What is the width of rectangle 2?: ')
width2 = float(width2_in)
print(f"So the width is {width2}? Neat!\n")  # r2 width input

# r2 height
height2_in = input('Now, what is the height?: ')
height2 = float(height2_in)
print(f"Height of {height2} has been noted. Thanks!\n")  # r2 height input

# Next line calls AreaCalc and saves area to Area2
Area2 = AreaCalc(width2, height2)  # call AreaCalc and save result to Area2

# ------------------------------------------------------------------------------------------------------

# This section compares the calculated values of R1 and R2 from Area1 and Area2 variables
print(f"\n\nThe area of Rectangle 1 is {Area1} and the area of Rectangle 2 is {Area2}")  # display the area of each rectangle

if Area1 > Area2:  # compare r1 to r2 area
    print(f"Hey, Rectangle 1 is bigger than the second with an area of {Area1}")
elif Area2 > Area1:  # compare r2 to r1 area
    print(f"The second rectangle is larger with an area of {Area2}")
else:  # 3rd option if r1 and r2 are the same size
    print(f"Looks like both rectangles have the same area of {Area1}.")

# section outputs the all the variables one last time.
print('\n\nFor reference, here are the supplied height, width, and area:')
print(f'Rectangle 1: Height={height1} Length={width1} Area={Area1}')
print(f'Rectangle 2: Height={height2} Length={width2} Area={Area2}')
