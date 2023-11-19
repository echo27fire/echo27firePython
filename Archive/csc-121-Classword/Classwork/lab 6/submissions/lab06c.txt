'''
Auth: Taylor Goodspeed
Date: Sep 23, 2023
Class: CSC 121
Program: fuel gauge
'''

while True:
    try:
        fuelIn = input("Enter the fuel remaining as 'fuel in tank / total fuel capacity': ")
        # fuel in tank will be represented as X/Y 
        x_value, y_value = fuelIn.split('/')

        # convert values to int
        x = int(x_value)
        y = int(y_value)

        # test: is X > Y OR is Y == 0
        if x > y or y == 0:
            raise ValueError("Invalid input: fuel in tank cannot exced capacity, or an invalid capacity was entered.")
        
        # here the fuel tank % is calculated and rounded.
        percentage = round((x / y) * 100)


        # test the percentange and display result if falls into specific conditions
        if percentage <= 1:
            print("E") #tank is empty more or less
        elif percentage >= 99:
            print("F") # tank is full or nearly full
        else:
            print(f"{percentage}%")
        
        break # ends the while loop once input is sucessful.

    # exception / error handleing.
    except ValueError:
        print ("Verify that fuel in tank and capacity are intergers: Verify X is less than or = to y")
    except ZeroDivisionError:
        print("you cannot devide by zero. Verify correct fuel capacity was input.")
    except Exception as e:
        print(f"an error that was not expected has occured: {e}")