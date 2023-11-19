'''
Author: Taylor Goodspeed
Date:11-4-2023
Program: lab11c - DTCC Course information.
'''

# Class info as a comment
'''
Class - -room loc- instructor - time - room - credit hours
NOS-120-190 bld 10 rm 112 Uzan - 5:45 pm - 3
NOS-230-170 bld 10 rm 111 Neal - 3:00 pm - 3
NOS-231-100 bld 10 rm 111 Neal - 1:00 pm - 3
NET-125-170  bld 10 rm 112 Green- 1:00 pm -3
CTI-110-170 bld 9 rm 239 Milla - 1;00 pm - 3
'''


# dict of class -> room
class_room = {
    'NOS-120':'10-112',
    'NOS-230':'10-111',
    'NOS-231':'10-111',
    'NET-125':'10-112',
    'CTI-110':'9-239'
}

# dict of class -> instructor
class_instructor = {
    'NOS-120':'Uzan',
    'NOS-230':'Neal',
    'NOS-231':'Neal',
    'NET-125':'Green',
    'CTI-110':'Milla'
}

# dict class -> meeting time
class_time = {
    'NOS-120':' Tuesday 5:45 pm,',
    'NOS-230':' Wednesday 3:00 pm',
    'NOS-231':' Wednesday 1:00 pm',
    'NET-125':' Thursday 1:00 pm',
    'CTI-110':' Monday 1:00 pm'
}

# dict of class -> credit hours
class_credit = {
    'NOS-120':'3',
    'NOS-230':'3',
    'NOS-231':'3',
    'NET-125':'3',
    'CTI-110':'3'
}

# Functions
def find_course(course_number):
    """
    Finds the course details for a given course number.

    Args:
        course_number (str): The course number to search for.

    Returns:
        None
    """
    # Check if the course number exists in the dictionaries
    if course_number in class_instructor:
        # Get and print course details
        print(f"Class: {course_number}")
        print(f"Instructor: {class_instructor[course_number]}")
        print(f"Location (Building-Room): {class_room[course_number]}")
        print(f"Meeting Day & Time: {class_time[course_number]}")
        print(f"Credit Hours: {class_credit[course_number]}")
    else:
        # Print course does not exist
        print("Course does not exist")

def main():
    """
    This function prompts the user to enter a course number until they enter 'q' to quit.
    For each course number entered, it calls the find_course function to search for the course.
    """
    while True:
        course_in = input("Enter a course number (or 'q' to quit): ").upper()
        if course_in == 'Q':
            break
        find_course(course_in)

# Call the main function to run the program
main()