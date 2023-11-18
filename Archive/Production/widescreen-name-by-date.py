import os
from datetime import datetime

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
        original_file_name, file_extension = os.path.splitext(os.path.basename(full_path))
        new_file_name = f"{counter_str}_{two_levels_up}{file_extension}"
        new_full_path = os.path.join(os.path.dirname(full_path), new_file_name)

        try:
            os.rename(full_path, new_full_path)
            print(f"Renamed: {full_path} -> {new_full_path}")
        except Exception as e:
            print(f"Failed to rename {full_path} -> {new_full_path} due to {str(e)}")

            # Attempt to rename the offending file to a temporary name
            try:
                temp_name = os.path.join(os.path.dirname(full_path), f"TEMP_{original_file_name}{file_extension}")
                os.rename(new_full_path, temp_name)
                print(f"Temporarily renamed offending file: {new_full_path} -> {temp_name}")

                # Attempt to rename the original file again
                os.rename(full_path, new_full_path)
                print(f"Successfully renamed original file after error handling: {full_path} -> {new_full_path}")

                # Rename the offending file back to its new name
                os.rename(temp_name, new_full_path)
                print(f"Renamed offending file back to new name: {temp_name} -> {new_full_path}")
            except Exception as e:
                print(f"Failed to handle error properly: {str(e)}")

        counter += 1

if __name__ == "__main__":
    directory_path = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers - Copy\\Widescreen"
    rename_files(directory_path)
