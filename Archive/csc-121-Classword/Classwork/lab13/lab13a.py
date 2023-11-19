'''
Author: Taylor Goodspeed
Date: Nov 18, 2023
Program: Lab 13a - Pets
Description: Pets Class
'''

from pet import Pet #import pet from pet.py seet pet.py for full class information.

def main():
    """
    This function creates a Pet object, prompts the user for pet details,
    sets the pet's attributes, and prints the pet's details.
    """
    my_pet = Pet()
    name = input("My pet's name is: ")
    animal_type = input("My pet is a: ")
    age = int(input("My pet is ___ years old: "))

    my_pet.set_name(name)
    my_pet.set_animal_type(animal_type)
    my_pet.set_age(age)

    print("\nPet Details: ")
    print("Name: ", my_pet.get_name())
    print("Type: ", my_pet.get_animal_type())
    print("Age: ", my_pet.get_age())


if __name__ == "__main__":
    main()