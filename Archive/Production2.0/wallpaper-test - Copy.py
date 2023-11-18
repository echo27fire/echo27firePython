
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
root_wallpaper = "C:\Users\echo2\OneDrive\Pictures\Wallpapers - Copy\"
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

def folder_check(file_path, base_subfolder):
    try:
        width, height = get_image_dimensions(file_path)
        # Check if the file is already in a resolution folder and skip if true
        if 'x' in os.path.basename(os.path.dirname(file_path)):
            return

        correct_folder = widescreen_path if width > height else portrait_path
        correct_subfolder = os.path.join(correct_folder, f"{width}x{height}")
        if not os.path.exists(correct_subfolder):
            os.makedirs(correct_subfolder)

        target_file_path = os.path.join(correct_subfolder, os.path.basename(file_path))
        shutil.move(file_path, target_file_path)
        print(f"Moved {file_path} to {target_file_path}")
    except Exception as e:
        print(f"Failed to move {file_path} to {correct_subfolder}: {e}")

def check_runts(image_path):
    """
    Check if an image is a "runt" (too small to be used as a wallpaper) and move it to the appropriate folder.

    Args:
        image_path (str): The path to the image file.

    Returns:
        None
    """
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

def rename_files(directory_path):
    """
    Renames all files in the given directory path based on their creation time.
    If a file with the new name exists, it tries the next number in sequence.
    """
    # Function body unchanged

def main():
    # Paths to the directories that will be processed
    base_paths = {
        widescreen_subfolder: widescreen_path,
        portrait_subfolder: portrait_path
    }
    
    # 1. Remove duplicates
    for subfolder, base_path in base_paths.items():
        print(f"Checking for duplicates in {base_path}")
        remove_duplicate_hash(base_path)
    
    # 2. Organize files into correct folders based on their dimensions
    for subfolder, base_path in base_paths.items():
        for subdir, dirs, files in os.walk(base_path):
            for file in files:
                full_file_path = os.path.join(subdir, file)
                if os.path.isfile(full_file_path) and file.lower().endswith(('.png', '.jpg', '.jpeg')):
                    # Only process files if they are not already in a resolution subfolder
                    if subdir == base_path:
                        try:
                            width, height = get_image_dimensions(full_file_path)
                            folder_check(full_file_path, subdir, width, height)
                        except Exception as e:
                            print(f"An error occurred while processing {full_file_path}: {e}")
    
    # 3. Check and handle runts
    for subdir, dirs, files in os.walk(runt_path):
        for file in files:
            full_file_path = os.path.join(subdir, file)
            if os.path.isfile(full_file_path) and file.lower().endswith(('.png', '.jpg', '.jpeg')):
                try:
                    check_runts(full_file_path)
                except Exception as e:
                    print(f"An error occurred while processing runts {full_file_path}: {e}")
                
    # 4. Rename files
    for subfolder, base_path in base_paths.items():
        print(f"Renaming files in {base_path}")
        rename_files(base_path)
    
    print("Wallpaper organization completed.")

if __name__ == "__main__":
    main()
