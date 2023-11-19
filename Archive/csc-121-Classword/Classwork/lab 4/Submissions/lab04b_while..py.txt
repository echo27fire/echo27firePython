'''
Name: Taylor Goodspeed
Class: CSC 121
Date: September 9, 2023
Program: lab04b
'''


Age_In = int(input('How old are you?: ')) #get input age
print ('Happy Birthday to you!') # print message
Age_Count = 0 # init. Age_Count variable
while Age_Count < Age_In: #while loop while count < input
    Age_Count += 1 #itterate count
    print (f'Are you {Age_Count}?')
