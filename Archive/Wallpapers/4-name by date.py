import os
from datetime import datetime

def rename_files(directory_path):
    # Create an empty list to store the file info
    file_list = []
    
    # Loop through the files and sub-directories under the given directory path
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            full_path = os.path.join(root, file)
            
            # Get the file creation time
            file_stat = os.stat(full_path)
            creation_time = file_stat.st_ctime
            
            # Append a tuple containing the creation time and full path to the list
            file_list.append((creation_time, full_path))

    # Sort the list by creation time
    file_list.sort(key=lambda x: x[0])
    
    # Initialize counter for file prefix
    counter = 0

    # Rename the sorted files
    for creation_time, full_path in file_list:
        # Format the counter to a 5-digit string
        counter_str = str(counter).zfill(5)

        # Get the directory name two levels up
        two_levels_up = os.path.basename(os.path.dirname(os.path.dirname(full_path)))

        # Get the original file name and extension
        original_file_name, file_extension = os.path.splitext(os.path.basename(full_path))

        # Create the new file name, preserving the original file extension
        new_file_name = f"{counter_str}_{two_levels_up}{file_extension}"

        # Full path for the new file name
        new_full_path = os.path.join(os.path.dirname(full_path), new_file_name)

        # Rename the file
        os.rename(full_path, new_full_path)
        
        print(f"Renamed: {full_path} -> {new_full_path}")

        # Increment the counter
        counter += 1

if __name__ == "__main__":
    directory_path = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers"
    rename_files(directory_path)
