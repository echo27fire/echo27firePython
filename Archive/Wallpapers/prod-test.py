from PIL import Image
import os
import shutil

# Define the root directories
ws_root_dir = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\Widescreen"
pt_root_dir = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\Portrait"
ultrawide_dir = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\UltraWide"


'''
    # Sort and rename widescreen wallpapers
    sort_images(ws_root_dir, ws_root_dir, dimension='width')
    rename_files(ws_root_dir)
    
    # Sort and rename portrait wallpapers
    sort_images(pt_root_dir, pt_root_dir, dimension='height')
    rename_files(pt_root_dir)
    
    # Identify and move ultra-wide wallpapers
    identify_ultrawide(ws_root_dir, ultrawide_dir)
    
    # Sort ultra-wide wallpapers by their width
    sort_images(ultrawide_dir, ultrawide_dir, dimension='width')
'''

# Function to get image dimensions
def get_image_dim(image_path):
    with Image.open(image_path) as img:
        return img.width, img.height

# Function to rename files based on creation time
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
        _, file_extension = os.path.splitext(os.path.basename(full_path))
        new_file_name = f"{counter_str}_{two_levels_up}{file_extension}"
        new_full_path = os.path.join(os.path.dirname(full_path), new_file_name)
        os.rename(full_path, new_full_path)
        print(f"Renamed: {full_path} -> {new_full_path}")
        counter += 1


# Function to sort and move image files
def sort_images(root_dir, target_root_dir, dimension='width'):
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                full_file_path = os.path.join(subdir, file)
                try:
                    width, height = get_image_dim(full_file_path)
                    target_value = width if dimension == 'width' else height
                    target_dir = os.path.join(target_root_dir, str(target_value))
                    if not os.path.exists(target_dir):
                        os.makedirs(target_dir)
                    target_file_path = os.path.join(target_dir, file)
                    shutil.move(full_file_path, target_file_path)
                    print(f"Moved {file} to {target_dir}")
                except Exception as e:
                    print(f"Error reading {full_file_path}: {e}")

# Function to identify and move ultra-wide images
def identify_ultrawide(root_dir, target_dir):
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                full_file_path = os.path.join(subdir, file)
                try:
                    width, height = get_image_dim(full_file_path)
                    aspect_ratio = width / height
                    ultra_wide_ratio = 21 / 9
                    super_ultra_wide_ratio = 32 / 9
                    margin_error = 0.17

                    if (ultra_wide_ratio * (1 - margin_error) <= aspect_ratio <= ultra_wide_ratio * (1 + margin_error)) or \
                       (super_ultra_wide_ratio * (1 - margin_error) <= aspect_ratio <= super_ultra_wide_ratio * (1 + margin_error)):
                        
                        target_file_path = os.path.join(target_dir, file)
                        shutil.move(full_file_path, target_file_path)
                        print(f"Moved {file} to {target_dir}")
                except Exception as e:
                    print(f"Error reading {full_file_path}: {e}")

def main():
    # Sort and rename widescreen wallpapers
    sort_images(ws_root_dir, ws_root_dir, dimension='width')
    rename_files(ws_root_dir)
    
    # Sort and rename portrait wallpapers
    sort_images(pt_root_dir, pt_root_dir, dimension='height')
    rename_files(pt_root_dir)
    
    # Identify and move ultra-wide wallpapers
    identify_ultrawide(ws_root_dir, ultrawide_dir)
    
    # Sort ultra-wide wallpapers by their width
    sort_images(ultrawide_dir, ultrawide_dir, dimension='width')

if __name__ == "__main__":
    main()