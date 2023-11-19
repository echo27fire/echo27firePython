
'''
Program: Wallpaper Management
Date: 2023-10-28
Version: 1.0
'''

import os
from PIL import Image
import shutil
import hashlib

# Corrected global paths
root_wallpaper = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\"
widescreen_subfolder = "Widescreen"
portrait_subfolder = "Portrait"  # Corrected spelling'
ultrawide_subfolder = "UltraWide"

# Joined paths
widescreen_path = os.path.join(root_wallpaper, widescreen_subfolder)
portrait_path = os.path.join(root_wallpaper, portrait_subfolder)
ultrawide_path = os.path.join(root_wallpaper, ultrawide_subfolder)


def get_image_dimensions(file_path):
    with Image.open(file_path) as img:
        return img.size  # returns a tuple (width, height)

# Function to get the creation date of a file
def get_creation_date(path_to_file):
    return os.path.getctime(path_to_file)

# Function to calculate the SHA-256 hash of a file
def calculate_hash(path_to_file):
    hash_object = hashlib.sha256()
    with open(path_to_file, "rb") as file:
        while chunk := file.read(4096):
            hash_object.update(chunk)
    return hash_object.hexdigest()

# Function to remove duplicate images based on their hash values
def remove_duplicate_hash(directory):
    hash_map = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_hash(file_path)
            if file_hash not in hash_map:
                hash_map[file_hash] = file_path
            else:
                try:
                    os.remove(file_path)
                    print(f"Removed duplicate file: {file_path}")
                except OSError as e:
                    print(f"Error removing file {file_path}: {e}")

# Function to check if the image file is in the correct folder based on its dimensions
def folder_check(file_path, is_widescreen):
    try:
        width, height = get_image_dimensions(file_path)
        base_folder_path = widescreen_path if is_widescreen else portrait_pathf
        
        # Determine the correct resolution folder based on image dimensions
        resolution_folder = str(width if is_widescreen else height)
        
        # Check the current directory of the file
        current_dir = os.path.dirname(file_path)
        
        # Skip if already in a resolution folder or at the root wallpaper directory
        if current_dir == base_folder_path or os.path.basename(current_dir).isdigit():
            return
        
        # Build the correct resolution folder path
        correct_folder_path = os.path.join(current_dir, resolution_folder)
        
        # Create the resolution folder if it doesn't exist
        if not os.path.exists(correct_folder_path):
            os.makedirs(correct_folder_path)
        
        # Construct the new file path
        target_file_path = os.path.join(correct_folder_path, os.path.basename(file_path))
        
        # Move the file to the new path
        shutil.move(file_path, target_file_path)
        print(f"Moved {file_path} to {target_file_path}")
    except Exception as e:
        print(f"Error moving {file_path}: {e}")


def check_runts(root_wallpaper):
    # Absolute paths for runts subfolders
    wide_runts = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\Runts\\Wide"
    port_runts = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\Runts\\Port"

    # Function to get image dimensions
    def get_image_dimensions(file_path):
        with Image.open(file_path) as img:
            return img.size  # returns a tuple (width, height)

    # Ensure runts folders exist
    for path in [wide_runts, port_runts]:
        if not os.path.exists(path):
            os.makedirs(path)

    # Iterate over the files in the root_wallpaper path and its subdirectories
    for folder_name, _, filenames in os.walk(root_wallpaper):
        for file in filenames:
            file_path = os.path.join(folder_name, file)
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                try:
                    width, height = get_image_dimensions(file_path)
                    # Check if the image fails the size check
                    if (width < 3440 and height < 1440) or (width < 1080 and height < 2400):
                        # Decide the folder based on the aspect ratio
                        dest_folder = port_runts if width < height else wide_runts
                        target_file_path = os.path.join(dest_folder, file)
                        shutil.move(file_path, target_file_path)
                        print(f"Moved {file_path} to {target_file_path}")
                except Exception as e:
                    print(f"Error checking runts for {file_path}: {e}")

# The path to the root wallpaper directory
root_wallpaper = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\"
check_runts(root_wallpaper)



def rename_files(directory_path):
    file_list = []

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            full_path = os.path.join(root, file)
            file_stat = os.stat(full_path)
            creation_time = file_stat.st_ctime
            file_list.append((creation_time, full_path))

    file_list.sort(key=lambda x: x[0])

    counter = 0

    for creation_time, full_path in file_list:
        counter_str = str(counter).zfill(5)
        two_levels_up = os.path.basename(os.path.dirname(os.path.dirname(full_path)))
        original_file_name, file_extension = os.path.splitext(os.path.basename(full_path))
        new_file_name = f"{counter_str}_{two_levels_up}{file_extension}"
        new_full_path = os.path.join(os.path.dirname(full_path), new_file_name)

        try:
            os.rename(full_path, new_full_path)
            print(f"Renamed: {full_path} -> {new_full_path}")
        except Exception as e:
            print(f"Failed to rename {full_path} -> {new_full_path} due to {str(e)}")

            # Attempt to rename the offending file to a temporary name
            try:
                temp_name = os.path.join(os.path.dirname(full_path), f"TEMP_{original_file_name}{file_extension}")
                os.rename(new_full_path, temp_name)
                print(f"Temporarily renamed offending file: {new_full_path} -> {temp_name}")

                # Attempt to rename the original file again
                os.rename(full_path, new_full_path)
                print(f"Successfully renamed original file after error handling: {full_path} -> {new_full_path}")

                # Rename the offending file back to its new name
                os.rename(temp_name, new_full_path)
                print(f"Renamed offending file back to new name: {temp_name} -> {new_full_path}")
            except Exception as e:
                print(f"Failed to handle error properly: {str(e)}")

        counter += 1
# The rest of your script remains unchanged

def scan_for_ports(src_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                src_file_path = os.path.join(root, file)
                
                try:
                    with Image.open(src_file_path) as img:
                        width, height = img.size
                        print(f"Processing: {src_file_path} (Dimensions: {width}x{height})")  # Debugging line
                        if height > width:
                            dest_file_path = os.path.join(dest_dir, file)
                            
                            counter = 1
                            while os.path.exists(dest_file_path):
                                filename, file_extension = os.path.splitext(file)
                                dest_file_path = os.path.join(dest_dir, f"{filename}_{counter}{file_extension}")
                                counter += 1

                            shutil.move(src_file_path, dest_file_path)
                            print(f"Moved: {src_file_path} to {dest_file_path} (Dimensions: {width}x{height})")
                        else:
                            print(f"Skipped: {src_file_path} is not a portrait image.")  # Debugging line
                except Exception as e:
                    print(f"Could not open image {src_file_path}: {e}")



def main():
    
    # Remove duplicates in all subfolders
    for path in [widescreen_path, portrait_path]:
        remove_duplicate_hash(path)
        
    src_dir = r'C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\Widescreen'
    dest_dir = r'C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\Portrait\\111_Landing'
    scan_for_ports(src_dir, dest_dir)
    
    # Organize files within each subfolder of Widescreen and Portrait
    for is_widescreen, base_path in [(True, widescreen_path), (False, portrait_path)]:
        for subdir, dirs, files in os.walk(base_path):
            # Skip the root Widescreen and Portrait directories
            if subdir == base_path:
                continue

            # Process only if not already in a resolution folder
            if not any(folder.isdigit() for folder in subdir.replace(base_path, '').split(os.sep)):
                for file in files:
                    if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                        file_path = os.path.join(subdir, file)
                        folder_check(file_path, is_widescreen)

    # Check and handle runts
    check_runts(root_wallpaper)

    # Rename files in Widescreen and Portrait paths
    for base_path in [widescreen_path, portrait_path]:
        for subdir, dirs, files in os.walk(base_path):
            # Skip the root directories
            if subdir in [widescreen_path, portrait_path]:
                continue

            # Skip resolution directories and only rename files in subfolders
            if subdir.count(os.path.sep) - base_path.count(os.path.sep) == 1:
                rename_files(subdir)

    print("Wallpaper organization completed.")

if __name__ == "__main__":
    main()
