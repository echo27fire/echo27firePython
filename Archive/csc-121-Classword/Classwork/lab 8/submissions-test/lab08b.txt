'''
Name: Taylor Goodspeed
Date: Oct 7, 2023
Class: CSC 121
Program: Statistics Calc.
'''

# functions
def list_statistics(alist):
    '''
    This functio displays some statistics about the numbers submitted by the user.
    '''
    number_of_items = len(alist) # number of items in alist object
    smallest_item = min(alist) # smallset value item in alist
    biggest_item = max(alist) # largets value item in alist
    total_items = sum(alist) # total sum of all items in the list
    average_of_items = total_items / number_of_items # calculate the average of numbers in alist


    # these lines print the values from the above variables.
    print(f"The number of items is: {number_of_items}")
    print(f"The smallest item is: {smallest_item}")
    print(f"The largest item is: {biggest_item}")
    print(f"Total of items: {total_items}")
    print(f"The average of the items is: {average_of_items:.2f}") # average is displayed to 2 deci. places.

def largerthan(threshold, alist):
    '''
    this function takes a supplied 'threshold' value, and compares it against values in alist
    if a value in alist is greater than the threashold, these values are returned.
    '''
    return [x for x in alist if x > threshold]

def main():
    '''
    main function summary: asks for user to input 10 numerical values and uses the largerthan and list_statistics functions
    to display / calculate some metrics on that input.
    '''

    # ask user for input. Verify that input meets the requirement of comma seperate values.
    while True:
        try:
            number_input = input("Please enter 10 numbers separated by commas: ")
            number_list = [float(x.strip()) for x in number_input.split(",")]

            # if supplied values do not = 10, error out untill the correct number of values is entered.
            if len(number_list) != 10:  
                remaining_numbers = 10 - len(number_list) # calculate number of remaining numbers from supplied numbers.
                raise ValueError(f"You need to supply 10 numbers! Supply {remaining_numbers} more!") # display the remaining values to submit.
            
            break
        except ValueError as e: # general error catch.
            print(f"ERROR: {e}. Please try again.")

    threshold_value = float(input("Input a value to use as a threshold: ")) # ask user for threashhold value.

    print("\nStatistics for the provided list: ")
    list_statistics(number_list) # call list_statistics function

    larger_than_list = largerthan(threshold_value, number_list) # call larger_than_list function and display resulting values.
    print(f"\nNumbers in the list larger than {threshold_value}: {larger_than_list}")


#invoke main & program start
if __name__ == "__main__":
    main()
