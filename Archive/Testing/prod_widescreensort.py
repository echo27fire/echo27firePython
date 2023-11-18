import os
import shutil
from PIL import Image
from collections import defaultdict

# Define root path
root_path = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\Widescreen"

# 111_Landing folder
landing_folder = os.path.join(root_path, "111_Landing")

# Make sure 111_Landing exists
if not os.path.exists(landing_folder):
    os.makedirs(landing_folder)

# Initialize a dictionary to hold files with their creation time
file_creation_times = defaultdict(list)

# Function to move image to folder based on its width
def move_image(image_path, width):
    parent_dir = os.path.dirname(image_path)
    correct_folder = os.path.join(parent_dir, str(width))

    # If the image is in the right folder, skip
    if os.path.basename(parent_dir) == str(width):
        return image_path

    # Otherwise, create folder if it doesn't exist
    if not os.path.exists(correct_folder):
        os.makedirs(correct_folder)

    # Move the file
    new_path = os.path.join(correct_folder, os.path.basename(image_path))
    shutil.move(image_path, new_path)
    return new_path

# Traverse the directory
for foldername, _, filenames in os.walk(root_path):
    for filename in filenames:
        if filename.lower().endswith(('png', 'jpg', 'jpeg')):
            full_path = os.path.join(foldername, filename)

            # Check if the image is in the root directory
            if foldername == root_path:
                shutil.move(full_path, os.path.join(landing_folder, filename))
                continue

            # Open the image to get its dimensions
            with Image.open(full_path) as img:
                width, _ = img.size

            # Update full_path after moving
            full_path = move_image(full_path, width)

            # Record the creation time and new full path
            creation_time = os.path.getctime(full_path)
            file_creation_times[creation_time].append(full_path)

# Sort files by creation time and rename
sorted_files = sorted(file_creation_times.items())
count = 0

for _, files in sorted_files:
    for file_path in files:
        # Get the parent subfolder name, excluding the root path
        parent_subfolder_name = file_path.replace(root_path, '').split(os.sep)[1]
        
        new_name = f"{count:04d}_{parent_subfolder_name}{os.path.splitext(file_path)[1]}"
        new_path = os.path.join(os.path.dirname(file_path), new_name)
        os.rename(file_path, new_path)
        count += 1
