from PIL import Image
import os
import shutil

# Define directories
root_dir = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\"
runts_directory = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\Runts"
runts_widescreen = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\Runts\\Wide"
runts_portrait = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\Runts\\Port"


def get_image_width(image_path):
    """
    Returns the width of the image located at the given image_path.

    Parameters:
    image_path (str): The path to the image file.

    Returns:
    int: The width of the image.
    """
    with Image.open(image_path) as img:
        return img.width

def get_image_height(image_path):
    """
    Get the height of an image.

    Parameters:
    image_path (str): The path to the image file.

    Returns:
    int: The height of the image.
    """
    with Image.open(image_path) as img:
        return img.height

def verify_runts_dir(directory):
    """
    Verify if the specified directory exists. If it doesn't, create the directory.

    Args:
        directory (str): The path of the directory to be verified/created.

    Returns:
        None
    """
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
            print(f"Runts folder created at {directory}")
        except Exception as e:
            print(f"There has been a failure to create the directory: {e}")

def move_runts(full_file_path, file, dest_folder):
    """
    Move a file to a specified destination folder.

    Args:
        full_file_path (str): The full path of the file to be moved.
        file (str): The name of the file to be moved.
        dest_folder (str): The destination folder where the file will be moved to.

    Returns:
        None

    Raises:
        Exception: If there is an error moving the file.
    """
    try:
        shutil.move(full_file_path, os.path.join(dest_folder, file))
        print(f"Moved {file} to {dest_folder}")
    except Exception as e:
        print(f"Error moving {file}: {e}")

def main():
    """
    Main function that verifies runts directories and moves images based on their dimensions.
    """
    
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
