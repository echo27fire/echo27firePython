import os
import shutil
from PIL import Image
from datetime import datetime

def get_image_dimensions(image_path):
    with Image.open(image_path) as img:
        return img.size

def main():
    src_dir = r'C:\Users\echo2\OneDrive\Pictures\Wallpapers'
    dest_dir = r'C:\Users\echo2\OneDrive\Pictures\Wallpapers_Portrait\111_Landing'
    file_list = []

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    # Scan and move files based on dimensions
    for root, _, files in os.walk(src_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                src_file_path = os.path.join(root, file)

                try:
                    width, height = get_image_dimensions(src_file_path)

                    if height > width:
                        dest_file_path = os.path.join(dest_dir, file)
                        counter = 1
                        while os.path.exists(dest_file_path):
                            filename, file_extension = os.path.splitext(file)
                            dest_file_path = os.path.join(dest_dir, f"{filename}_{counter}{file_extension}")
                            counter += 1

                        shutil.move(src_file_path, dest_file_path)
                        print(f"Moved: {src_file_path} to {dest_file_path} (Dimensions: {width}x{height})")

                except Exception as e:
                    print(f"Could not open image {src_file_path}: {e}")

    # Move and rename files
    for directory_path in [src_dir, dest_dir]:
        for root, _, files in os.walk(directory_path):
            for file in files:
                if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                    full_file_path = os.path.join(root, file)

                    try:
                        width, height = get_image_dimensions(full_file_path)
                    except Exception as e:
                        print(f"Error reading {full_file_path}: {e}")
                        continue

                    target_dir = os.path.join(root, str(width) if width > height else str(height))
                    last_element = os.path.basename(os.path.normpath(root))

                    if last_element.isdigit() and int(last_element) == (width if width > height else height):
                        continue

                    if not os.path.exists(target_dir):
                        os.makedirs(target_dir)

                    target_file_path = os.path.join(target_dir, file)

                    try:
                        shutil.move(full_file_path, target_file_path)
                        print(f"Moved {file} to {target_dir}")

                        file_stat = os.stat(target_file_path)
                        creation_time = file_stat.st_ctime
                        file_list.append((creation_time, target_file_path))

                    except Exception as e:
                        print(f"Error moving {file}: {e}")

        # Sort and rename files
        file_list.sort(key=lambda x: x[0])
        counter = 0
        for creation_time, full_path in file_list:
            counter_str = str(counter).zfill(5)
            two_levels_up = os.path.basename(os.path.dirname(os.path.dirname(full_path)))
            original_file_name, file_extension = os.path.splitext(os.path.basename(full_path))
            new_file_name = f"{counter_str}_{two_levels_up}{file_extension}"
            new_full_path = os.path.join(os.path.dirname(full_path), new_file_name)
            os.rename(full_path, new_full_path)
            print(f"Renamed: {full_path} -> {new_full_path}")
            counter += 1

if __name__ == "__main__":
    main()
