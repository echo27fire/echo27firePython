import os
import shutil
from PIL import Image
from datetime import datetime

# Define the directories
root_dir = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\Widescreen"
ultrawide_dir = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\UltraWide"

# Aspect ratios
aspect_ratios = {
    1.0: "1x1",
    1.33: "4x3",
    1.5: "3x2",
    1.77: "16x9",
    2.0: "18x9",
    2.33: "21x9",
    2.5: "5x2",
    2.77: "25x9",
    3.0: "3x1",
}

# Function to get image resolution
def get_image_resolution(image_path):
    with Image.open(image_path) as img:
        return img.width, img.height

# Function to get image aspect ratio
def get_image_aspect_ratio(image_path):
    with Image.open(image_path) as img:
        width, height = img.size
        return round(width / height, 2)

# Function to get image width
def get_image_width(image_path):
    with Image.open(image_path) as img:
        return img.width

# Function to rename files
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
        counter_str = str(counter).zfill(4)
        new_name = f"{counter_str}_{datetime.fromtimestamp(creation_time).strftime('%Y%m%d_%H%M%S')}.jpg"
        os.rename(full_path, os.path.join(directory_path, new_name))
        counter += 1

# Main function
def main():
    # Step 1: Sort wallpapers into ultra-wide and other categories
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                full_file_path = os.path.join(subdir, file)
                width, height = get_image_resolution(full_file_path)
                if width / height >= 2.33:
                    shutil.move(full_file_path, os.path.join(ultrawide_dir, file))
    
    # Step 2: Categorize wallpapers based on their aspect ratio
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                full_file_path = os.path.join(subdir, file)
                aspect_ratio = get_image_aspect_ratio(full_file_path)
                aspect_ratio_folder = aspect_ratios.get(aspect_ratio, "Others")
                destination_folder = os.path.join(root_dir, aspect_ratio_folder)
                os.makedirs(destination_folder, exist_ok=True)
                shutil.move(full_file_path, os.path.join(destination_folder, file))

    # Step 3: Perform operations based on ultra-wide width
    for subdir, _, files in os.walk(ultrawide_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                full_file_path = os.path.join(subdir, file)
                width = get_image_width(full_file_path)
                if width >= 3440:
                    # Perform any operations here. Placeholder for now.
                    pass

    # Step 4: Rename files based on their creation time
    rename_files(root_dir)

# Run the main function
if __name__ == "__main__":
    main()
