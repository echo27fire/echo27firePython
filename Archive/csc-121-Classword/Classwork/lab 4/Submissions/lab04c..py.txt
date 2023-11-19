'''
Name: Taylor Goodspeed
Class: CSC 121
Date: September 9, 2023
Program: lab04c
'''

# total cost function, calculates the total cost of an item by it's value and quatity
def TotalCost(item_cost, item_count):
    return item_cost * item_count

# reciept function prints a recipet, takes all provided variables as input for display and calculation
def receipt(Shirt_In, Game_In, Book_In, Cost_Tshirt, Cost_Game, Cost_Book, Total_Tshirt, Total_Game, Total_Book):
    print('\n\n****************************\n\n')
    print('Here is your receipt:')
    # Next three lines print the amount of items, their base cost, and total cost 
    print(f'Shirts: Total {Shirt_In} shirts at ${Cost_Tshirt:.2f} comes to: ${Total_Tshirt:.2f}')
    print(f'Games: Total {Game_In} games at ${Cost_Game:.2f} comes to: ${Total_Game:.2f}')
    print(f'Books: Total {Book_In} books at ${Cost_Book:.2f} comes to: ${Total_Book:.2f}')
    print('------------------------------------') # break
    Sub_Total = Total_Tshirt + Total_Book + Total_Game # calculate sub total based on number total of input items.
    print(f'Your Subtotal is: ${Sub_Total:.2f}\n') #prints the total of all items.

# Variables
# Item cost vars
Cost_Tshirt = 8.60
Cost_Game = 20.00
Cost_Book = 12.95

# Item Max vars
Max_Tshirt = 8
Max_Game = 2
Max_Book = 3

# Total Cost vars, init.
Total_Tshirt = 0
Total_Game = 0
Total_Book = 0

print(' ') # adds a blank line at start of output.
# Code Body
while True: #Shirt Loop
    Shirt_In = int(input('How many shirts are you buying?:'))
    if Shirt_In > Max_Tshirt or Shirt_In < 0: # test if input is in allowed range
        print('Sorry, could you try that again?')
    else:
        Total_Tshirt = TotalCost(Cost_Tshirt, Shirt_In) # calls TotalCost function and saves return to Total_'item'
        break

while True: #Game Loop
    Game_In = int(input('Now, how many games are you buying?: '))
    if Game_In > Max_Game or Game_In < 0: # test if input is in allowed range
        print('Sorry, can you try that again?')
    else:
        Total_Game = TotalCost(Cost_Game, Game_In) # calls TotalCost function and saves return to Total_'item'
        break

while True: #Book Loop
    Book_In = int(input('What about books? How many of those?: '))
    if Book_In > Max_Book or Book_In < 0: # test if input is in allowed range
        print('Sorry, can you try that again?')
    else:
        Total_Book = TotalCost(Cost_Book, Book_In) # calls TotalCost function and saves return to Total_'item'
        break

receipt(Shirt_In, Game_In, Book_In, Cost_Tshirt, Cost_Game, Cost_Book, Total_Tshirt, Total_Game, Total_Book)
