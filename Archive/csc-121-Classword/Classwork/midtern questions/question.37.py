'''
Name: Taylor Goodspeed
Date: 10/21/2023
Program: Midterm question 37
'''


# cat. input:
have_fur = input("Does the animal in question have fur (yes/no)? ")
can_fly = input("Can the animal in question fly (yes/no)? ")
live_in_water = input("Does the animal in question live in water (yes/no)? ")

# Initialize category variable
category = "Unknown"

# Check inputs and assign to correct class
if have_fur.lower() == "yes":
    category = "Mammal" # if characteristic = yes for fur assign to Mammal
elif can_fly.lower() == "yes":
    category = "Bird" # if characteristic = yes for being able to fly assign to Bird
elif live_in_water.lower() == "yes":
    category = "Aquatic" # if characteristic = yes for living in water assign to Aquatic
else:
    print("The animal in question is an unknown species.") # if characteristic != above assign to Unknown

print("The animal in question belongs to the", category, "category.") 
