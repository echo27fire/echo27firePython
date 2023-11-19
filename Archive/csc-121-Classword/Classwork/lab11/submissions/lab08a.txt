'''
Author: Taylor Goodspeed
Date: 11-4-2023
Progam: lab 08a- dictionary's and sets

'''
# Part 1:  Dictionary Practice

# Q1:  Create an empty Dictionary as variable mydict1, and display the dictionary using print.
# print(f"Empty dictionary mydict1 = {mydict1}")
# Expected output:
# Empty dictionary mydict1 = {}
print("\nQ1")

mydict1 = {}
print(mydict1)

# Q2:  Create an empty Dictionary a different way than Q1 as variable mydict2, and display the dictionary using print.
# print(f"Empty dictionary mydict2 = {mydict2}")
# Expected output:
# Empty dictionary mydict2 = {}
print("\nQ2")
mydict2 = dict()
print(f"Empty dictionary mydict = {mydict2}")



# Q3:  Create a dictionary named mydict with these keys:  name, age, and city
# and these associated values:  John, 25, New York
# and display the dictionary:  print(f"mydict = {mydict}")
# Expected output not shown, as it gives away the answer.
print("\nQ3")

mydict = {'name': 'John', 'age': 25, 'city': 'New York'}
print(f"mydict = {mydict}")



# Q4: Write a function called build_dict()
# that takes no argument and returns a hard-coded dictionary
# with these keys:  name, age, and city
# and these associated values:  John, 25, New York
# A starter version of the function build_dict is provided below
# with a pass (ignore) to prevent errors.  Modify that function.
# Expected output not given as it gives away the answer.
print("\nQ4")
def build_dict():
    return {
        'name': 'John',
        'age': 25,
        'city': 'New York'
    }

mydict = build_dict()
print(f"mydict = {mydict}")

#print(f"mydict = {mydict}")  # uncomment this when you get to this question



# Q5: Assume mydict references a dictionary.  Write an assignment statement to
# assign the number/count of key/value pairs in the dictionary to a variable named how_many.
# Display the variable how_many.  print(f"how_many = {how_many}")
# Expected output:
# how_many = 4
mydict = {'color': 'green', 'fav_number': 7, 'movie': 'Avatar', 'major': 'Computer Programming'}
print("\nQ5")
how_many = len(mydict)
print(f"how many = {how_many}")




# Q6:  Assume mydict references a dictionary.  Write an assignment statement to get
# all the keys in a dictionary called mydict and assign to a variable called my_keys.
# Display the variable my_keys.  print(f"my_keys = {my_keys}")
# Display the type of the variable my_keys.  print(f"type(my_keys) = {type(my_keys)}")
# Expected output: (may be in a different order; type may also be class <list>)
# my_keys_list = ['name', 'movie', 'street_addr', 'color']
# type(my_keys) = <class 'dict_keys'>
mydict = {'name': 'Bob', 'movie': 'Avatar', 'street_addr': 'West Main St', 'color':'orange'}
print("\nQ6")
my_keys = mydict.keys()
print(f"my_keys = {list(my_keys)}")
print(f"type(my_keys) = {type(my_keys)}")



# Q7:  Assume mydict references a dictionary.  Write an assignment statement to get
# all the keys in the dictionary and assign to a *list* called my_keys_list.
# Display the variable my_keys_list.  print(f"my_keys_list = {my_keys_list}")
# Display the type of the variable my_keys_list.  print(f"type(my_keys_list) = {type(my_keys_list)}")
# Display my_keys_list in ascending order/alphabetically.
# Expected output: (may be in a different order, except for keys in order)
# my_keys_list = ['name', 'movie', 'street_addr', 'color']
# type(my_keys_list) = class <list>
# keys in order = ['color', 'name', 'movie', 'street_addr']
mydict = {'name': 'Bob', 'movie': 'Avatar', 'street_addr': 'West Main St', 'color':'orange'}
print("\nQ7")
my_keys_list = list(mydict.keys())
print(f"my_keys_list = {my_keys_list}")
print(f"type(my_keys_list) = {type(my_keys_list)}")
keys_in_order =sorted(my_keys_list)
print(f"keys in order = {keys_in_order}")



# Q8:  Assume mydict references a dictionary.  Write a for loop to display each of
# the keys with an identifying string "Key:" on a seperate line.
# Expected output:
# Key:  color
# Key:  fav_number
# Key:  movie
# Key:  major
mydict = {'color': 'green', 'fav_number': 7, 'movie': 'Avatar', 'major': 'Computer Programming'}
print("\nQ8")
for key in mydict:
    print(f"key: {key}")






# Q9:  Assume mydict references a dictionary.  Write a for loop to display each of
# the values with an identifying string "Value:" on a seperate line.
# Expected output:
# Value:  green
# Value:  7
# Value:  avatar
# Value:
mydict = {'color': 'green', 'fav_number': 7, 'movie': 'Avatar', 'major': 'Computer Programming'}
print("\nQ9")
for value in mydict.values():
    print(f"value: {value}")





# Q10:  Assume mydict references a dictionary.  Write a for loop to display each of the
# tuples of (key, value) pairs in the dictionary with an identifying string "Tuple: "
# on a seperate line.
# Your for loop should start with: for key, value in
# Expected output:
# Tuple:  (color, green)
# Tuple:  (fav_number, 7)
# Tuple:  (movie, Avatar)
# Tuple:  (major, Computer Programming)
mydict = {'color': 'green', 'fav_number': 7, 'movie': 'Avatar', 'major': 'Computer Programming'}
print("\nQ10")
for key, value in mydict.items():
    print(f"Tuple: ({key}), {value})")




# Q11:  Assume mydict references a dictionary.  Write a line of code to replace the value
# associated with the key 'color' with the value 'blue'.
# Do not recreate the whole dictionary.
# Display the dictionary.  print(f"mydict = {mydict}")
# Expected output: (can be in a different order)
# mydict =  {'color': 'blue', 'fav_number': 7, 'movie': 'Avatar', 'major': 'Computer Programming'}
mydict = {'color': 'green', 'fav_number': 7, 'movie': 'Avatar', 'major': 'Computer Programming'}
print("\nQ11")
mydict['color'] = 'blue'
print(f"mydict = {mydict}")


# Q12:  Assume mydict references a dictionary.  Write a line of code to add the key 'name'
# and the value of your last name to the dictionary mydict.
# Do not recreate the whole dictionary
# Display the dictionary.  print(f"mydict = {mydict}")
# Expected output:  (can be in a different order)
# mydict = {'color': 'green', 'fav_number': 7, 'movie': 'Avatar', 'major': 'Computer Programming', 'name': YOUR_NAME_WILL_BE_HERE }
mydict = {'color': 'green', 'fav_number': 7, 'movie': 'Avatar', 'major': 'Computer Programming'}
print("\nQ12")
mydict['name'] = 'Goodspeed'
print(f"mydict = {mydict}")


# Q13:  Assume mydict references a dictionary.
# Write an assignment statement to get all the keys and assign to a *list* called my_keys_list.
# Display the variable my_keys_list.  print(f"my_keys_list = {my_keys_list}")
# Display the type of the variable my_keys_list.  print(f"type(my_keys_list) = {type(my_keys_list)}")
# Display my_keys_list in ascending order/alphabetically.
# Expected output: (may be in a different order, except last one)
# my_keys_list = ['name', 'movie', 'street_addr', 'color']
# type(my_keys_list) = class <list>
# keys in order = ['color', 'name', 'movie', 'street_addr']
mydict = {'name': 'Bob', 'movie': 'Avatar', 'street_addr': 'West Main St', 'color':'orange'}
print("\nQ13")
my_keys_list =list(mydict.keys())
print(f"my_keys_list = {my_keys_list}")
print(f"type(my_keys_list) = {type(my_keys_list)}")
keys_in_order = sorted(my_keys_list)
print(f"keys in order = {keys_in_order}")




# Q14:  Write an if statement that displays 'IS A KEY' if my_key1 is a key in the
# dictionary mydict, or 'NOT A KEY'.  Write a second if statement to do the same for my_key2.
# Expected output:
# street_addr IS A KEY
# favorite NOT A KEY
mydict =  {'name': 'Bob', 'movie': 'Avatar', 'street_addr': 'West Main St', 'color':'orange'}
my_key1 = 'street_addr'
my_key2 = 'favorite'
print("\nQ14")
if my_key1 in mydict:
    print(f"{my_key1} IS A KEY")
else:
    print(f"{mydict1} IS NOT A KEY")

if my_key2 in mydict:
    print(f"{my_key2} NOT A KEY")
else:
    print(f"{my_key2} NOT A KEY")


# Part 2:  Set Practice
# Q15: Assume myset1 and myset2 are two sets.  Create a set variable myset3 that contains all the items
# in EITHER of these sets using a set method.  Display myset1, myset2, and myset3.
# print(f"myset3 = {myset3}")
# Expected output: (set values can be in any order)
# myset1 = {8, 9, 2, 4}
# myset2 = {1, 2, 6, 9, 12}
# myset3 = {1, 2, 4, 6, 8, 9, 12}
my_set1 = {2, 9, 4, 8}
my_set2 = {6, 9, 12, 2, 1}
print("\nQ15")
myset3 = my_set1.union(my_set2)
print(f"myset1 = {my_set1}")
print(f"myset2 = {my_set2}")
print(f"myset3 = {myset3}")


# Q16: Assume myset1 and myset2 are two sets.  Create a set variable myset3 that contains all the items
# in BOTH of these sets using a set method.  Display myset1, myset2, and myset3.
# Expected output: (set values can be in any order)
# myset1 = {8, 9, 2, 4}
# myset2 = {1, 2, 6, 9, 12}
# myset3 = {9, 2}
my_set1 = {2, 9, 4, 8}
my_set2 = {6, 9, 12, 2, 1}
print("\nQ16")
my_set3 = my_set1.intersection(my_set2)
print(f"myset1 = {my_set1}")
print(f"myset2 = {my_set2}")
print(f"myset3 = {my_set3}")


# Q17:  Assume myset references a set variable.
# Do the following steps:
# (1) Display the set and number of elements in the set.
# (2) Add the number 12 to the set, and Display the set and the number of elements in the set.
# (3) Add the number 11 to the set, and Display the set and the number of elements in the set.
# (4) Remove the number 4, and Display the Set and number of elements in the set.
# Expected output: (set values can be in any order)
# Set: {1, 4, 7, 9, 11}, Number of Elements: 5
# Set: {1, 4, 7, 9, 11, 12}, Number of Elements: 6
# Set: {1, 4, 7, 9, 11, 12}, Number of Elements: 6
# Set: {1, 7, 9, 11, 12}, Number of Elements: 5
myset = {1, 9, 11, 4, 7}
print("\nQ17")
print(f"Set: {myset}, Number of Elements: {len(myset)}")
myset.add(12)
print(f"Set: {myset}, Number of Elements: {len(myset)}")
myset.add(11)
print(f"Set: {myset}, Number of Elements: {len(myset)}")
myset.remove(4)
print(f"Set: {myset}, Number of Elements: {len(myset)}")



# Q18: Assume myset1 and myset2 are two sets.  Create a set variable myset3 that contains all the items
# all the items that are either ONLY in myset1 OR ONLY in myset2, but NOT IN BOTH sets. Use a set method.
# Display myset1, myset2, and myset3.
# Expected output:  (set values can be in any order)
# myset1 = {8, 9, 2, 4}
# myset2 = {1, 2, 6, 9, 12}
# myset3 = {1, 4, 6, 8, 12}
myset1 = {2, 9, 4, 8}
myset2 = {6, 9, 12, 2, 1}
print("\nQ18")
myset3 = myset1.symmetric_difference(myset2)
print(f"myset1 = {myset1}")
print(f"myset2 = {myset2}")
print(f"myset3 = {myset3}")


# Q19: Assume myset1 and myset2 are two sets.  Create a set variable myset3 that
# contains all the items that are IN myset1, but NOT IN myset2.
# Use a set method.
# Display myset1, myset2, and myset3.
# Expected output:  (set values can be in any order)
# myset1 = {8, 9, 2, 4}
# myset2 = {1, 2, 6, 9, 12}
# myset3 = {8, 4}
myset1 = {2, 9, 4, 8}
myset2 = {6, 9, 12, 2, 1}
print("\nQ19")


# Q20: Assume myset1 and myset2 are two sets.  Create a set variable myset3 that
# contains all the items that are IN myset2, but NOT IN myset1.
# Use a set method.
# Display myset1, myset2, and myset3.
# Expected output:  (set values can be in any order)
# myset1 = {8, 9, 2, 4}
# myset2 = {1, 2, 6, 9, 12}
# myset3 = {1, 12, 6}
my_set1 = {2, 9, 4, 8}
my_set2 = {6, 9, 12, 2, 1}
print("\nQ20")




# Part 3:  Challenge (worth 5x points of other questions)
# Q21:  Assume mystr references a string.  Convert mystr to upper case.
# Create an empty dictionary called my_count_dict.
# Write a for loop to loop through each character of the string, and
# using an accumulator pattern to count the number of each character found in the
# string.
# Display the maximum count of all the letters using your dictionary.
# Hint:  Your dictionary my_count_dict will have each upper case version of a letter in the
# string mystr as a key, and increase the count of the number of those seen so far as the
# value.  When the loop ends, the count of each letter will be the value.
# Expected output:
# my_count_dict = {'T': 1, 'H': 1, 'E': 1, ' ': 3, 'R': 1, 'A': 2, 'I': 3, 'N': 3, 'S': 1, 'P': 1}
# maximum count = 3
mystr = "The rain in Spain"
print("\nQ21")
mystr = mystr.upper()
my_count_dict ={}
for char in mystr:
    if char in my_count_dict:
        my_count_dict[char] += 1
    else:
        my_count_dict[char] = 1

print(f"my_count_dict ={my_count_dict}")
max_count = max(my_count_dict.values())
print(f"maximum count ={max_count}")



# Extra Credit.  For Q21, display the letter or letters that have the maximum count.
# Expected output: (can be displayed as a list or on seperate lines, etc. as long as it finds
# and displays these two letters):
# I
# N
print("\nExtra Credit")
max_count = max(my_count_dict.values())
max_count_letters = [letter for letter, count in my_count_dict.items() if count == max_count]
for letter in max_count_letters:
    print(letter)
