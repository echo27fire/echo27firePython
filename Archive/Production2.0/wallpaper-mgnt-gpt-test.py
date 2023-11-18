''''
Program: Wallpaper Management
Date: 2023-10-28
Version: 1.0
'''

import os
from PIL import Image
import shutil
import hashlib

# Corrected global paths
root_wallpaper = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers - Copy\\"
widescreen_subfolder = "Widescreen"
portrait_subfolder = "Portrait"  # Corrected spelling
runt_subfolder = "Runts"

# Joined paths
widescreen_path = os.path.join(root_wallpaper, widescreen_subfolder)
portrait_path = os.path.join(root_wallpaper, portrait_subfolder)
runt_path = os.path.join(root_wallpaper, runt_subfolder)

# Function to get the dimensions of an image
def get_image_dimensions(image_path):
    with Image.open(image_path) as img:
        return img.width, img.height

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
def folder_check(file_path, width, height):
    correct_subfolder = widescreen_subfolder if width > height else portrait_subfolder
    resolution_folder = f"{width}x{height}"
    correct_folder_path = os.path.join(root_wallpaper, correct_subfolder, resolution_folder)

    if not os.path.exists(correct_folder_path):
        os.makedirs(correct_folder_path)

    shutil.move(file_path, os.path.join(correct_folder_path, os.path.basename(file_path)))
    print(f"File {file_path} moved to {correct_folder_path}")

# Function to check if the image belongs in the runts folder and move it if necessary
def check_runts(image_path):
    width, height = get_image_dimensions(image_path)
    wide_runts = os.path.join(runt_path, "Wide")
    port_runts = os.path.join(runt_path, "Port")

    for path in [wide_runts, port_runts]:
        if not os.path.exists(path):
            os.makedirs(path)

    if width < height:  # Portrait
        dest_folder = port_runts
    else:  # Widescreen
        dest_folder = wide_runts

    if (width < 2560 and height < 1440) or (height < 1920 and width < 1200):
        shutil.move(image_path, os.path.join(dest_folder, os.path.basename(image_path)))
        print(f"Moved {os.path.basename(image_path)} to {dest_folder}")
    else:
        print(f"File {os.path.basename(image_path)} is not a runt")

# Function to rename files in a directory
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
            counter += 1
        except OSError as e:
            print(f"Failed to rename {full_path} -> {new_full_path} due to {str(e)}")
            

import os

def main():
    """
    This script performs the following tasks:
    1. Removes duplicate images from specified directories
    2. Organizes images into correct folders based on their dimensions
    3. Checks for and handles "runt" images (images that are too small to be used as wallpapers)
    4. Renames files in the specified directories
    
    Args:
    None
    
    Returns:
    None
    """
    # Paths to the directories that will be processed
    directories = [widescreen_path, portrait_path, runt_path]
    
    # 1. Remove duplicates
    for directory in directories:
        print(f"Checking for duplicates in {directory}")
        remove_duplicate_hash(directory)
    
    # 2. Organize files into correct folders
    # This assumes every image file is directly within the given directories
    for directory in directories:
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                width, height = get_image_dimensions(file_path)
                folder_check(file_path, width, height)

    # 3. Check and handle runts
    for directory in directories:
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                check_runts(file_path)
                
    # 4. Rename files
    for directory in directories:
        print(f"Renaming files in {directory}")
        rename_files(directory)
    
    print("Wallpaper organization completed.")

if __name__ == "__main__":
    main()
