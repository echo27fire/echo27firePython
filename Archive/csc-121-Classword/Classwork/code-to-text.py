import os
import shutil


def copy_python_files_to_text_files():
    """
    This function copies all Python files in a specified directory and its subdirectories
    to a new directory called 'submissions', with the file extension changed to .txt.
    """

    # Step 1: Set the directory input using a raw string to handle backslashes correctly
    dir_input = r"C:\\Github\\TG-CSC-121-DTCC-FA23\\Classwork\\lab13"

    # Step 2: Create a folder called 'submissions' if it doesn't exist already
    submissions_dir = os.path.join(dir_input, 'submissions')
    try:
        os.makedirs(submissions_dir, exist_ok=True)
    except Exception as e:
        print(f"Failed to create submissions directory: {e}")
        return

    # Step 3 & 4: Locate files ending in .py and copy them into the 'submissions'
    # folder with the extension changed to .txt
    for root, dirs, files in os.walk(dir_input):
        for file in files:
            if file.endswith('.py'):
                source = os.path.join(root, file)
                destination = os.path.join(submissions_dir, os.path.splitext(file)[0] + '.txt')
                try:
                    shutil.copy2(source, destination)
                except Exception as e:
                    print(f"Failed to copy {file}: {e}")

    print("The script has successfully executed.")


# Call the function to execute the script
copy_python_files_to_text_files()
