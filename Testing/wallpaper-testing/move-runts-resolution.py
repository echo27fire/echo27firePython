import os
from PIL import Image
import shutil

def get_image_dimensions(path):
    try:
        with Image.open(path) as img:
            return img.size  # Returns a tuple of (width, height) of the image
    except IOError:
        print(f"Cannot open {path}")
        return None

def is_widescreen_image(width, height):
    return width > height

def sort_into_resolution_folder(file, base_path):
    dimensions = get_image_dimensions(file)
    if dimensions is None:
        return

    width, height = dimensions
    resolution_directory = str(width if is_widescreen_image(width, height) else height)
    current_path = os.path.dirname(file)

    if os.path.basename(current_path).isdigit():
        return
    
    correct_path = os.path.join(base_path, resolution_directory)
    
    if not os.path.exists(correct_path):
        os.makedirs(correct_path)
    
    target_path = os.path.join(correct_path, os.path.basename(file))
    
    try:
        shutil.move(file, target_path)
        print(f"Moved {file} to {target_path}")
    except Exception as e:
        print(f"Error moving {file} to {target_path}: {e}")

def main():
    print("Starting to sort images into resolution folders within Runts")
    runts_path = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\Runts"
    port_runts = os.path.join(runts_path, "Port")
    wide_runts = os.path.join(runts_path, "Wide")
    
    for base_path in [wide_runts, port_runts]:
        print(f"Sorting in {base_path}")
        for root, dirs, files in os.walk(base_path):
            for file in files:
                full_file_path = os.path.join(root, file)
                print(f"Processing {full_file_path}")
                sort_into_resolution_folder(full_file_path, base_path)

    print("Sorting images, complete")
                
if __name__ == "__main__":
    main()
