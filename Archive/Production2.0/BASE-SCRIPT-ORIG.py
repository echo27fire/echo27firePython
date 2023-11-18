''''
Program: Wallpaper Management
Date: 2023-10-28
Version: 1.0
'''
import os
from PIL import Image
import shutil
import hashlib


# global paths
root_wallpaper = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\"
widescreen_subfolder = "Widescreen"
portorait_subfolder = "Portorait"
runt_subfolder = "Runts"


# joined paths
widescreen_path = os.path.join(root_wallpaper, widescreen_subfolder)
portorait_path = os.path.join(root_wallpaper, portorait_subfolder)
runt_path = os.path.join(root_wallpaper, runt_subfolder)


# functions
def get_image_dimensions(image_path):
    """
    Returns the width and height of an image.

    Args:
        image_path (str): The path to the image.

    Returns:
        tuple: The width and height of the image.
    """
    with Image.open(image_path) as img:
        return img.width, img.height

def get_creation_date(path_to_file):
    """
    Returns the creation date of a file.

    Args:
        path_to_file (str): The path to the file.

    Returns:
        float: The creation date of the file.
    """
    return os.path.getctime(path_to_file)

def calculate_hash(path_to_file):
    """
    Calculates the SHA-256 hash of a file.

    Args:
        path_to_file (str): The path to the file to be hashed.

    Returns:
        str: The SHA-256 hash of the file.
    """
    hash_object = hashlib.sha256()
    with open(path_to_file, "rb") as file:
        while chunk := file.read(4096):
            hash_object.update(chunk)
    return hash_object.hexdigest()

def remove_duplicate_hash(directory):
    """
    Removes duplicate files in a directory based on their SHA-256 hash.

    Args:
        directory (str): The path to the directory.

    Returns:
        None
    """
    hash_map = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_hash(file_path)

            if file_hash not in hash_map:
                hash_map[file_hash] = []

            hash_map[file_hash].append({
                "path": file_path,
                "mtime": os.path.getmtime(file_path)
            })

    for _, file_info_list in hash_map.items():
        if len(file_info_list) > 1:
            file_info_list.sort(key=lambda x: x['mtime'], reverse=True)
            for file_info in file_info_list[1:]:
                print(f"Removing duplicate file: {file_info['path']}")
                os.remove(file_info['path'])

import os
import shutil

def folder_check(file_path, width, height):
    """
    Check if the image file is in the correct folder based on its dimensions.
    If the file is not in the correct folder, move it to the correct folder.

    Args:
        file_path (str): The path of the image file.
        width (int): The width of the image in pixels.
        height (int): The height of the image in pixels.

    Returns:
        None
    """
    # Get the current folder and the parent folder
    current_folder = os.path.basename(os.path.dirname(file_path))
    parent_folder = os.path.dirname(os.path.dirname(file_path))

    # Determine if the image is widescreen or portrait
    if width > height:
        # The correct folder name based on the image width
        correct_folder_name = str(width)
    else:
        # The correct folder name based on the image height
        correct_folder_name = str(height)

    # Check if the file is in the correct folder
    if current_folder == correct_folder_name:
        print(f"File {file_path} is in the correct folder")
    else:
        # The correct folder path
        correct_folder_path = os.path.join(parent_folder, correct_folder_name)
        # Check if the correct folder exists, if not, create it
        if not os.path.exists(correct_folder_path):
            os.makedirs(correct_folder_path)
        # Move the file to the correct folder
        shutil.move(file_path, os.path.join(correct_folder_path, os.path.basename(file_path)))
        print(f"File {file_path} moved to {correct_folder_path}")


def check_runts(image_path):
    """
    Check if the runts folder exists, and create it if it doesn't.
    Then move the image to the appropriate runts folder based on its aspect ratio.

    Args:
        image_path (str): The full path to the image file.

    Returns:
        None
    """
    # paths to place runts
    wide_runts = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\Runts\\Wide"
    port_runts = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\Runts\\Port"
    paths = [wide_runts, port_runts]

    for path in paths:
        if not os.path.exists(path):
            try:
                os.makedirs(path)
                print(f"Runts folder created at {path}")
            except Exception as e:
                print(f"There has been a failure to create the directory: {e}")

    # local function
    def move_runts(full_file_path, file, dest_folder):
        try:
            shutil.move(full_file_path, os.path.join(dest_folder, file))
            print(f"Moved {file} to {dest_folder}")
        except Exception as e:
            print(f"Error moving {file}: {e}")

    # call move_runts here with appropriate arguments
    width, height = get_image_dimensions(image_path)
    
    if width > height and width < 2560 and height < 1440:
        move_runts(image_path, os.path.basename(image_path), wide_runts)
    elif height > width and height < 1920 and width < 1200:
        move_runts(image_path, os.path.basename(image_path), port_runts)
    else:
        print(f"File {image_path} is not a runt")

def get_image_dimensions(image_path):
    """
    Get the dimensions of an image file.

    Args:
        image_path (str): The path to the image file.

    Returns:
        tuple: The width and height of the image in pixels.
    """
    with open(image_path, "rb") as file:
        data = file.read(25)

    if data.startswith(b"\xff\xd8"):
        # JPEG
        width, height = (data[163:165] << 8) + data[166], (data[161:163] << 8) + data[164]
    elif data.startswith(b"\x89PNG\r\n\x1a\n"):
        # PNG
        width, height = (data[16:20][::-1]), (data[20:24][::-1])
        width, height = int.from_bytes(width, byteorder='big'), int.from_bytes(height, byteorder='big')
    else:
        raise ValueError("Unsupported file format")

    return width, height

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
