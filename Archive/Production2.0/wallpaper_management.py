
import os
from PIL import Image
import shutil

root_wallpaper = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\"
widescreen_subfolder = "Widescreen"
portrait_subfolder = "Portrait"

def get_image_dimensions(image_path):
    with Image.open(image_path) as img:
        return img.width, img.height

def is_image_in_correct_resolution_folder(subdir, resolution):
    # Check if the current subdir ends with the resolution
    return subdir.endswith(os.path.sep + resolution)

def move_and_rename_file(file_path, target_folder, base_name):
    # Ensure target folder exists
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # Generate the new file name
    file_extension = os.path.splitext(file_path)[1]
    new_file_name = f"{base_name}_{os.path.basename(file_path)}"
    new_file_path = os.path.join(target_folder, new_file_name)

    # Rename and move the file
    shutil.move(file_path, new_file_path)
    print(f"Moved and renamed {file_path} to {new_file_path}")

def process_images_in_subfolder(subdir, files, is_widescreen):
    for file in files:
        if not file.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue
        
        full_file_path = os.path.join(subdir, file)
        
        try:
            width, height = get_image_dimensions(full_file_path)
        except Exception as e:
            print(f"Error reading {full_file_path}: {e}")
            continue

        resolution_property = width if is_widescreen else height
        resolution_folder_name = str(resolution_property)
        current_folder_name = os.path.basename(subdir)
        
        # Skip processing if the image is already in the correct resolution folder
        if is_image_in_correct_resolution_folder(subdir, resolution_folder_name):
            continue
        
        # Construct the target folder based on the resolution
        target_folder = os.path.join(os.path.dirname(subdir), resolution_folder_name)
        
        # Move and rename the file
        move_and_rename_file(full_file_path, target_folder, current_folder_name)

def main():
    for subfolder in [widescreen_subfolder, portrait_subfolder]:
        base_path = os.path.join(root_wallpaper, subfolder)
        for subdir, dirs, files in os.walk(base_path):
            # Skip the root directory and any resolution-specific subfolders
            if subdir == base_path:
                continue
            if os.path.basename(subdir).isdigit():
                # This is a resolution-specific folder, so we skip it
                continue
            
            process_images_in_subfolder(subdir, files, subfolder == widescreen_subfolder)

    print("Wallpaper processing completed.")

if __name__ == "__main__":
    main()
