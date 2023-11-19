"""
Name: Taylor G
Date: August 26, 2023
Script: lab02 c assignment, shopping calculator

"""
# Global Variables
Tax_Rate = 0.07  # sales tax percentage

#variables for item selection, referanced by Menu function
Item1, Item2, Item3 = 'Books', 'Movies', 'Video Games' 

# Global Functions
def SubTotal(Cart_Total, Tax_Rate):
    return Cart_Total * Tax_Rate

# Function for totcal cost calculation
def ItemCost(quantity, price):
    quantity_cost = quantity * price #multiply the quanitty by price
    rounded_cost = round(quantity_cost, 2) # round to 2 deci. places (dealing with money)
    return rounded_cost #return the rounded cost for processing outside of function

#Function for Main Menu
def Menu():
    print('Hello! Welcome to ShopCalc, your friendly shopping calculator.')
    print("Please select an option below to start calculating the total cost of items in your cart.")
    print(f"1: {Item1}")
    print(f"2: {Item2}")
    print(f"3: {Item3}")
    print("--------------------------------")
    answer = input("Please enter the number of the item you would like to calculate: ")

    valid_answers = ["1", "2", "3"]
    item_names = { "1": Item1, "2": Item2, "3": Item3 }

    if answer not in valid_answers:
        print("Sorry, could you please select a valid item number? Thanks!")
        return Menu()
    else:
        selected_item_name = item_names[answer]
        print(f'Great choice! Let\'s start adding up your {selected_item_name}.')
        return selected_item_name
    
# Reciept function
def Reciept(purchaes, subtotal, tax_ammount, grand_total):

    subtotal = total_cost
    tax_amount = SubTotal(subtotal, Tax_Rate)
    grand_total = subtotal + tax_amount

    print("\nReceipt:")
    print("--------------------------")
    for purchase in purchases:
        item_name, quantity, price, item_cost = purchase
        print(f"{item_name} ({quantity} x ${price:.2f}): ${item_cost:.2f}")
    print("--------------------------")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax: ${tax_amount:.2f} Current sales tax is:{Tax_Rate * 100:.0f}% of subtotal")
    print(f"Grand Total: ${grand_total:.2f}")


total_cost = 0
purchases = []

# while loop keeps menu / input cycle running until user says 'no' I have everything.
while True:
    selected_item_name = Menu()
    
    quantity = float(input(f"How many {selected_item_name} are you purchasing? "))
    price = float(input(f"How much does each {selected_item_name} cost? "))
    
    item_cost = ItemCost(quantity, price)
    total_cost += item_cost #cummulative adding of item cost -> total cost 
    
    purchases.append((selected_item_name, quantity, price, item_cost))  # Store purchase details
    
    print(f'The cost of your {selected_item_name} selection is ${item_cost:.2f}.')
    
    another_item = input("Would you like to add another item (yes/no)? ").lower() # Menu escape section. 'lower' will convert the respnse to lower caseto process match
    if another_item != "yes": #this section could be expanded. What if user, like in main menu, submits a code breaking or unexpected response?
        break

subtotal = total_cost
tax_amount = SubTotal(subtotal, Tax_Rate)
grand_total = subtotal + tax_amount


#call reciept functin and display final cost to user
Reciept(purchases, subtotal, tax_amount, grand_total)



'''
print("\nReceipt:")
print("--------------------------")
for purchase in purchases:
    item_name, quantity, price, item_cost = purchase
    print(f"{item_name} ({quantity} x ${price:.2f}): ${item_cost:.2f}")
print("--------------------------")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax_amount:.2f} Current sales tax is:{Tax_Rate * 100:.0f}% of subtotal")
print(f"Grand Total: ${grand_total:.2f}")
'''
