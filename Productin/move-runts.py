from PIL import Image
import os
import shutil

# Define directories
root_dir = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\"
runts_directory = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\Runts"
runts_widescreen = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\Runts\\Wide"
runts_portrait = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\Runts\\Port"


def get_image_width(image_path):
    with Image.open(image_path) as img:
        return img.width

def get_image_height(image_path):
    with Image.open(image_path) as img:
        return img.height

def verify_runts_dir(directory):
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
            print(f"Runts folder created at {directory}")
        except Exception as e:
            print(f"There has been a failure to create the directory: {e}")

def move_runts(full_file_path, file, dest_folder):
    try:
        shutil.move(full_file_path, os.path.join(dest_folder, file))
        print(f"Moved {file} to {dest_folder}")
    except Exception as e:
        print(f"Error moving {file}: {e}")

def main():
    verify_runts_dir(runts_directory)
    verify_runts_dir(runts_widescreen)
    verify_runts_dir(runts_portrait)

    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                full_file_path = os.path.join(subdir, file)
                try:
                    img_width = get_image_width(full_file_path)
                    img_height = get_image_height(full_file_path)
                except Exception as e:
                    print(f"ERROR reading: {full_file_path}: {e}")
                    continue

                if img_width < 3440 or img_height < 1440:
                    if img_width > img_height:
                        move_runts(full_file_path, file, runts_widescreen)
                    else:
                        if img_height < 1920 and img_width < 1200:
                            move_runts(full_file_path, file, runts_portrait)

if __name__ == "__main__":
    main()
