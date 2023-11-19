'''
Name: Taylor Goodspeed
Date: Nov 18, 2023
Assignment:  Lab09b - OOP Practice Exercise #2 - Code Completion
'''

'''
--pre config doc string--
The program should create a class that prints the title and author of a book.
Correct the 7 errors in the following code.
Each of the 7 errors is all the fixes on a single line of code.

When fixed, the program should display:
Your book is The Odyssey by Homer

For full credit, write comments and complete the docstring in this code!
'''

class Book:
    def __init__(self, title, author):
        """
        Initialize a Book object with a title and author.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title  # Set the title as an instance variable
        self.author = author  # Set the author as an instance variable

    def __str__(self):
        """
        Return a string representation of the Book object.

        Returns:
            str: A string representation of the book in the format "Your book is {title} by {author}".
        """
        return f"Your book is {self.title} by {self.author}"  # Reference instance variables


# Create an instance of the Book class
book = Book("The Odyssey", "Homer")
print(book)
