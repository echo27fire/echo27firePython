'''
Program: Move Portrait wallpapers to a new folder
Author: Taylor Goodspeed
'''

import os
from PIL import Image
import shutil

def get_image_dimensions(path):
    with Image.open(path) as img:
        return img.size  # Returns a tuple of (width, height) of the image

def move_portrait_images(source_path, destination_path):
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)
        
    for root, dirs, files in os.walk(source_path):
        for file in files:
            try:
                full_file_path = os.path.join(root, file)
                width, height = get_image_dimensions(full_file_path)
                if width < height:
                    shutil.move(full_file_path, destination_path)
                    print(f"Moved {file} to {destination_path}")
                else:
                    print(f"{file} is not a portrait image")
            except Exception as e:
                print(f"Error processing {file}: {e}")

def main():
    """
    Move portrait images from the widescreen landing directory to the portrait landing directory.
    """
    # Define directories
    root_wallpaper = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\"  # Root directory for wallpapers
    widescreen_landing = os.path.join(root_wallpaper, "Widescreen\\111_Landing")  # Directory where images are saved typically
    portraits_landing = os.path.join(root_wallpaper, "Portrait\\111_Landing")  # Directory where portrait images are moved to
    
    move_portrait_images(widescreen_landing, portraits_landing)

if __name__ == "__main__":
    main()
