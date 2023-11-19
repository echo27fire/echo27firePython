from PIL import Image
import os
import shutil
from datetime import datetime

# File types for images
valid_extensions = ['.png', '.jpg', '.jpeg']

# Main directories for different types of wallpapers
root_dir = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\"
dir_port = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\Portrait"
dir_ulwd = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\UltraWide"
dir_wide = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\Widescreen"

# Runt directories for smaller images
runts_directory = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\Runts"
runts_widescreen = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\Runts\\Wide"
runts_portrait = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\Runts\\Port"

# Function to get dimensions of an image
def get_dimensions(image_path):
    with Image.open(image_path) as img:
        return img.width, img.height

''' old dimension functions
def get_image_width(image_path):
    with Image.open(image_path) as img:
        return img.width

def get_image_height(image_path):
    with Image.open(image_path) as img:
        return img.height

'''
        
# Function to verify if directories exist, create if not
def verify_directories(*directories):
    for directory in directories:
        if not os.path.exists(directory):
            try:
                os.makedirs(directory)
                print(f"Runts folder created at {directory}")
            except Exception as e:
                print(f"Failed to create directory: {e}")

def move_runts(root_dir, runt_directories):
    verify_directories(*runt_directories)

    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if any(file.lower().endswith(ext) for ext in valid_extensions):
                full_file_path = os.path.join(subdir, file)
                try:
                    img_width, img_height = get_dimensions(full_file_path)
                except Exception as e:
                    print(f"ERROR reading: {full_file_path}: {e}")
                    continue

                if img_width < 2560 or img_height < 1440:
                    dest_folder = None

                    if img_width > img_height:
                        dest_folder = runts_widescreen
                    else:
                        if img_height < 2400 and img_width < 1080:
                            dest_folder = runts_portrait

                    if dest_folder:
                        try:
                            shutil.move(full_file_path, os.path.join(dest_folder, file))
                            print(f"Moved {file} to {dest_folder}")
                        except Exception as e:
                            print(f"Error moving {file}: {e}")

def sort_images(root_dir, dimension='width'):
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(subdir, file)
                
                try:
                    img_width, img_height = get_dimensions(image_path)
                    target_value = img_width if dimension == 'width' else img_height
                    
                    # No need for Portrait or Landscape folders
                    # We create or find the target folder within the current subdirectory
                    target_dir = os.path.join(subdir, str(target_value))
                    
                    # Only use an existing directory; do not create new ones
                    if not os.path.exists(target_dir):
                        print(f"Target directory {target_dir} does not exist. Skipping.")
                        continue

                    target_file_path = os.path.join(target_dir, file)
                    
                    counter = 1
                    while os.path.exists(target_file_path):
                        filename, file_extension = os.path.splitext(file)
                        target_file_path = os.path.join(target_dir, f"{filename}_{counter}{file_extension}")
                        counter += 1

                    if os.path.abspath(image_path) != os.path.abspath(target_file_path):
                        shutil.move(image_path, target_file_path)
                        print(f'Moved {file} to {target_dir}')
                    else:
                        print(f"{file} is already in the correct folder.")
                        
                except Exception as e:
                    print(f'Error reading {image_path}: {e}')

def sort_images_in_subfolders(root_dir):
    for subdir, _, _ in os.walk(root_dir):
        # Skip the root directory itself
        if subdir == root_dir:
            continue
        print(f"Sorting images in {subdir}")
        sort_images(subdir, dimension='width')

def rename_files(directory_path):
    file_list = []

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            full_path = os.path.join(root, file)

            if file.lower().endswith(('.png', '.jpg', '.jpeg')):

                try:
                    with Image.open(full_path) as img:
                        width, height = img.size
                        print(f"Processing: {full_path} (Dimensions: {width}x{height})")  # Debugging line

                        file_stat = os.stat(full_path)
                        creation_time = file_stat.st_ctime
                        two_levels_up = os.path.basename(os.path.dirname(os.path.dirname(full_path)))
                        _, file_extension = os.path.splitext(os.path.basename(full_path))

                        if height > width:
                            new_file_name = f"portrait_{two_levels_up}{file_extension}"
                        else:
                            new_file_name = f"{width}_{two_levels_up}{file_extension}"

                        new_full_path = os.path.join(os.path.dirname(full_path), new_file_name)
                        
                        if new_full_path != full_path:
                            os.rename(full_path, new_full_path)
                            print(f"Renamed: {full_path} -> {new_full_path}")
                            
                except Exception as e:
                    print(f"Could not open image {full_path}: {e}")
                    continue

def id_ultrawide(root_dir, target_dir):
    for subdir, _, files in os.walk(root_dir):  # Removed the extra colon
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(subdir, file)
                try:
                    width = get_image_width(image_path)
                    height = get_image_height(image_path)
                    aspect_ratio = width / height  # Typo corrected from 'aspet_ratio'
                    uw_ratio = 21 / 9
                    super_uw_ratio = 32 / 9
                    margin_of_error = 0.17

                    if(uw_ratio * (1 - margin_of_error) <= aspect_ratio <= uw_ratio * (1 + margin_of_error)) or \
                      (super_uw_ratio * (1 - margin_of_error) <= aspect_ratio <= super_uw_ratio * (1 + margin_of_error)):
                        
                        target_path = os.path.join(target_dir, file)
                        shutil.move(image_path, target_path)
                        print(f"Moved {file} to {target_dir}")  # Typo corrected from 'moved' to 'Moved'
                except Exception as e:
                    print(f"Error reading {image_path}: {e}")

def main():
    runts_directory = os.path.join(root_dir, "Runts")
    runts_widescreen = os.path.join(runts_directory, "Wide")
    runts_portrait = os.path.join(runts_directory, "Port")

    move_runts(root_dir, [runts_directory, runts_widescreen, runts_portrait])

# wide screens
    sort_images(dir_wide, dimension='width')
    rename_files(dir_wide)

# portoraits
    sort_images(dir_port, dimension='height')
    rename_files(dir_port)

# ultrawides
    sort_images(dir_ulwd, dimension='width')
    rename_files(dir_ulwd)


if __name__ == "__main__":
    main()


    