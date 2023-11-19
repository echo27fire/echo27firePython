'''
Name: Taylor Goodspeed
Class: CSC 121
Date: September 9, 2023
Program: lab04a
'''

DayCount = 1
Total_Bug = 0
Days = 0

Days = int(input('How many days did you collected bugs?: '))


while DayCount <= Days:
    print(f'\nToday is day {DayCount}') # print the current day being input
    Collected_Bugs = int(input('How many bags of bugs did the bug collector bag?: ')) # gather input
    Total_Bug += Collected_Bugs     # Accumulate the total bugs collected.
    print(f"\nSo far we've collected {Total_Bug} bugs") # print running total
    DayCount += 1    # Increment the day count

# Display the total number of bugs collected at the end
print(f'\n \nThe total number of bugs collected is {Total_Bug} creepy crawlys!')
