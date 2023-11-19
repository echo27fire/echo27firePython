'''
Name: Taylor Goodspeed
Date: Nov 18, 2023
Assignment:  Lab09c - retail code main file
'''

from retailitem import RetailItem

def main():
    """
    This function creates RetailItem objects and displays their details.
    """
    # Creating RetailItem objects
    item1 = RetailItem("Jacket", 12, 59.95)
    item2 = RetailItem("Designer Jeans", 40, 34.95)
    item3 = RetailItem("Shirt", 20, 24.95)

    # Displaying the details of each item
    print("Item #1:")
    print(item1)
    print("\nItem #2:")
    print(item2)
    print("\nItem #3:")
    print(item3)

if __name__ == "__main__":
    main()
