import os
from PIL import Image
import shutil

def get_image_dimensions(path):
    with Image.open(path) as img:
        return img.size  # Returns a tuple of (width, height) of the image

def folder_name_check(file_path, is_widescreen, widescreen_path, portrait_path):
    try:
        width, height = get_image_dimensions(file_path)
        base_path = widescreen_path if is_widescreen else portrait_path
        resolution_folder = str(width if is_widescreen else height)
        current_dir = os.path.dirname(file_path)
        
        if current_dir == base_path or os.path.basename(current_dir).isdigit():
            return
        
        correct_path = os.path.join(current_dir, resolution_folder)
        
        if not os.path.exists(correct_path):
            os.makedirs(correct_path)
            
        target_path = os.path.join(correct_path, os.path.basename(file_path))
        
        shutil.move(file_path, target_path)
        print(f"Moved {file_path} to {target_path}")
    
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def rename_files(directory_path):
    file_list = []
    
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            full_file_path = os.path.join(root, file)
            file_statistics = os.stat(full_file_path)
            creation_time = file_statistics.st_ctime
            file_list.append((creation_time, full_file_path))
    
    file_list.sort(key=lambda x: x[0])
    counter = 0

    for creation_time, full_file_path in file_list:
        file_counter_str = str(counter).zfill(5)
        two_dirs_up = os.path.basename(os.path.dirname(os.path.dirname(full_file_path)))
        original_file_name, file_extension = os.path.splitext(os.path.basename(full_file_path))
        new_file_name = f"{file_counter_str}_{two_dirs_up}{file_extension}"
        new_full_path = os.path.join(os.path.dirname(full_file_path), new_file_name)

        try:
            os.rename(full_file_path, new_full_path)
            print(f"Renamed: {full_file_path} -> {new_full_path}")
        except Exception as e:
            print(f"Failed to rename {full_file_path} -> {new_full_path} due to {str(e)}")

        counter += 1

def main():
    root_path = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\"
    widescreen_path = os.path.join(root_path, "Widescreen")
    portrait_path = os.path.join(root_path, "Portrait")
    
    for is_widescreen, base_path in [(True, widescreen_path), (False, portrait_path)]:
        for subdir, dirs, files in os.walk(base_path):
            if subdir == base_path:
                continue
            
            if not any(folder.isdigit() for folder in subdir.replace(base_path, '').split(os.sep)):
                for file in files:
                    if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                        full_file_path = os.path.join(subdir, file)
                        folder_name_check(full_file_path, is_widescreen, widescreen_path, portrait_path)

if __name__ == "__main__":
    main()
