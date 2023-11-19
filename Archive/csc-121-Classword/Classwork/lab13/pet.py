'''
Author: Taylor Goodspeed
Date: Nov 18, 2023
Program: Lab 13a - Pets
Description: Pets Class - class file
'''
class Pet:
    """
    Represents a pet with a name, animal type, and age.
    """

    class Pet:
        def __init__(self, name="", animal_type="", age=0):
            """
            Initializes a new instance of the Pet class.

            Args:
                name (str): The name of the pet.
                animal_type (str): The type of animal the pet is.
                age (int): The age of the pet.
            """
            self.__name = name
            self.__animal_type = animal_type
            self.__age = age

    def set_name(self, name):
        self.__name = name # set the name of the pet

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type # set the animal type of the pet IE: dog, cat, etc.

    def set_age(self, age):
        self.__age = age # set the age of the pet

    def get_name(self):
        return self.__name # return the name of the pet to the user

    def get_animal_type(self):
        return self.__animal_type # return the animal type of the pet to the user

    def get_age(self):
        return self.__age # return the age of the pet to the user
