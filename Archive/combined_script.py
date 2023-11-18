
import os
import shutil
from PIL import Image
from collections import defaultdict

# Define root path
root_path = "C:\Users\echo2\OneDrive\Pictures\Wallpapers\Widescreen"

# Define other destination folders
portrait_landing_folder = "C:\Users\echo2\OneDrive\Pictures\Wallpapers\Portorait\111_Landing"
runts_folder = "C:\Users\echo2\OneDrive\Pictures\Wallpapers\Runts"
runts_port_folder = "C:\Users\echo2\OneDrive\Pictures\Wallpapers\Runts\Port"
runts_wide_folder = "C:\Users\echo2\OneDrive\Pictures\Wallpapers\Runts\Wide"

# Initialize folders
folders_to_init = [portrait_landing_folder, runts_folder, runts_port_folder, runts_wide_folder]
for folder in folders_to_init:
    if not os.path.exists(folder):
        os.makedirs(folder)

# Initialize a dictionary to hold files with their creation time
file_creation_times = defaultdict(list)

# Function to move image to folder based on dimensions
def move_image_to_folder(image_path, dest_folder):
    # Renaming logic not found
    # ...

    shutil.move(image_path, os.path.join(dest_folder, os.path.basename(image_path)))

# Function to sort images into respective folders
def sort_images(src_folder):
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(root, file)
                try:
                    with Image.open(image_path) as img:
                        width, height = img.size

                        # Check if the image is a widescreen image
                        if width > height:
                            if width >= 1920 and height >= 1080:
                                move_image_to_folder(image_path, root_path)
                            else:
                                move_image_to_folder(image_path, runts_wide_folder)

                        # Check if the image is a portrait image
                        else:
                            if width >= 1080 and height >= 1920:
                                move_image_to_folder(image_path, portrait_landing_folder)
                            else:
                                move_image_to_folder(image_path, runts_port_folder)

                except Exception as e:
                    print(f"Error processing {file}: {e}")

# You can now call sort_images with the path of the folder you want to sort
# sort_images("path_to_folder")
