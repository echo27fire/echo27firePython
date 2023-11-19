'''
Author: Taylor Goodspeed
Date: Nov 10, 2023
Program: Lab 12 - Pickle Demo
Description: Demo code for the pickle module in python.
'''

# Importing the pickle module, which is used for serializing and deserializing Python objects.
import pickle

# Example 1: highest protocol and dump
print("\nExample 1: highest protocol and dump")
# Creating a dictionary to be pickled.
data_high = {
    'name': 'Pickle',
    'date': 'November 11-high pickle'
}

# Opening a file in write-binary mode. The file is named 'data_highest_protocol.pkl'.
# Using a context manager (with statement) to ensure proper handling of file resources.
with open('data_highest_protocol.pkl', 'wb') as file:
    # Using pickle.dump to serialize 'data_high' and write it to the file.
    # Specifying the use of the highest protocol available for efficiency.
    pickle.dump(data_high, file, protocol=pickle.HIGHEST_PROTOCOL)

# Indicating completion of the serialization process for this part.
print("Data has been serialized with the highest protocol")


'''
---------------------------------------------------------------------------------------------
'''

# Example 2: default protocol and dump
print("\n\nExample 2: default protocol and dump")
# Creating another dictionary to be pickled.
data_default = {
    'name': 'Pickle',
    'date': 'November 11-default pickle'
}

# Opening another file in write-binary mode for the default protocol demonstration.
with open('data_default_protocol.pkl', 'wb') as file:
    # Serializing 'data_default' using the default protocol this time.
    pickle.dump(data_default, file)

# Indicating completion of the serialization process for the default protocol.
print("Data has been serialized with the default protocol")

'''
---------------------------------------------------------------------------------------------
'''

# Example 3: Dumps and Loads
print("\n\nExample 3: Dumps and Loads")
# Creating a third dictionary for in-memory serialization/deserialization.
data = {
    'name': 'Pickle',
    'date': 'November 11'
}

# Serializing 'data' to a byte string using pickle.dumps.
serialized_data = pickle.dumps(data)
# Deserializing 'serialized_data' back into a Python object.
deserialized_data = pickle.loads(serialized_data)

# Displaying the original, serialized, and deserialized data.
print("This is the Original data:", data)
print("This is the data under serialization:", serialized_data)
print("This is the data deserialized:", deserialized_data)

'''
---------------------------------------------------------------------------------------------
'''

# Example 4: Deserialize data from Example 1 and 2
print("\n\nExample 4: Deserialize data from Example 1 and 2")
# File paths for the serialized data files.
high_pickle = 'data_highest_protocol.pkl'
default_pickle = 'data_default_protocol.pkl'

# Opening the first file in read-binary mode to deserialize the data.
with open(high_pickle, 'rb') as file:
    deserialize_high = pickle.load(file)

# Opening the second file in read-binary mode to deserialize the data.
with open(default_pickle, 'rb') as file:
    deserialize_default = pickle.load(file)

# Printing the deserialized data from both files.
print("high_pickle:", deserialize_high)
print("default_pickle:", deserialize_default)

'''
---------------------------------------------------------------------------------------------
'''

# Example 5 - Code Execution during unpickling
print("\n\nExample 5 - Code Execution during unpickling")
# Defining a class that will execute code during unpickling.
class ExecuteCodeOnUnpickle:
    # Overriding the __reduce__ method, which pickle uses to determine how to serialize objects.
    def __reduce__(self):
        # Returning a tuple where the first element is a callable (print function),
        # and the second element is a tuple of arguments for the callable.
        return (print, ('Oh no! Code was executed during unpickling!',))

# Creating an instance of the ExecuteCodeOnUnpickle class.
obj = ExecuteCodeOnUnpickle()

# Serializing the object. This will not execute the code yet.
pickle_obj = pickle.dumps(obj)

# Deserializing the object. This triggers the execution of the print function.
pickle.loads(pickle_obj)
