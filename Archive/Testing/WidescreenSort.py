from PIL import Image  # Importing the PIL library for image handling
import os  # Importing os for file and directory operations
import shutil  # Importing shutil for file operations like move
from datetime import datetime  # Importing datetime for date/time operations

# Define directory paths
root_dir = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\Widescreen"
small_res_root_dir = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\WideScreen-Small"

# Function to get the width of an image
def get_image_width(image_path):
    with Image.open(image_path) as img:  # Open the image
        return img.width  # Return the width of the image

# Function to sort images by resolution
def sort_images(root_dir, target_root_dir):
    for subdir, _, files in os.walk(root_dir):  # Walk through all subdirectories and files
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):  # Check for image files
                full_file_path = os.path.join(subdir, file)  # Create full file path

                try:
                    width = get_image_width(full_file_path)  # Get image width
                except Exception as e:
                    print(f"Error reading {full_file_path}: {e}")  # Log errors
                    continue  # Skip to next file

                # Create target directory paths
                relative_path = os.path.relpath(subdir, root_dir)
                last_element = os.path.basename(os.path.normpath(subdir))

                if last_element.isdigit() and int(last_element) == width:
                    continue

                target_dir = os.path.join(target_root_dir, relative_path, str(width))
                
                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)  # Create target directory if it doesn't exist

                target_file_path = os.path.join(target_dir, file)

                try:
                    shutil.move(full_file_path, target_file_path)  # Move file
                    print(f"Moved {file} to {target_dir}")  # Log successful move
                except Exception as e:
                    print(f"Error moving {file}: {e}")  # Log move error

# Function to rename files
def rename_files(directory_path):
    file_list = []

    for root, dirs, files in os.walk(directory_path):  # Walk through directories
        for file in files:
            full_path = os.path.join(root, file)
            file_stat = os.stat(full_path)
            creation_time = file_stat.st_ctime  # Get file creation time
            file_list.append((creation_time, full_path))

    file_list.sort(key=lambda x: x[0])  # Sort files by creation time

    counter = 0

    for creation_time, full_path in file_list:
        counter_str = str(counter).zfill(5)
        two_levels_up = os.path.basename(os.path.dirname(os.path.dirname(full_path)))
        original_file_name, file_extension = os.path.splitext(os.path.basename(full_path))
        new_file_name = f"{counter_str}_{two_levels_up}{file_extension}"
        new_full_path = os.path.join(os.path.dirname(full_path), new_file_name)

        try:
            os.rename(full_path, new_full_path)  # Rename file
            print(f"Renamed: {full_path} -> {new_full_path}")  # Log success
        except Exception as e:
            print(f"Failed to rename {full_path} -> {new_full_path} due to {str(e)}")
            # Handling errors
            # (your existing error-handling code here)

        counter += 1

# Main function
def main():
    sort_images(root_dir, root_dir)  # Sort images in root directory
    sort_images(small_res_root_dir, small_res_root_dir)  # Sort images in small_res_root_dir
    rename_files(root_dir)  # Rename files in root directory

# Entry point of the program
if __name__ == "__main__":
    main()
