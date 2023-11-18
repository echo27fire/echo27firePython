from PIL import Image
import os
import shutil

# Define the root directory where the wallpapers are stored
root_dir = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers_Portrait"

def get_image_height(image_path):
    with Image.open(image_path) as img:
        return img.height

def main():
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                full_file_path = os.path.join(subdir, file)

                # Get the height of the image
                try:
                    height = get_image_height(full_file_path)
                except Exception as e:
                    print(f"Error reading {full_file_path}: {e}")
                    continue
                
                # Prepare target directory
                target_dir = os.path.join(subdir, str(height))

                # Extract the last element of the folder path
                last_element = os.path.basename(os.path.normpath(subdir))

                # Skip if the image is already in the correct resolution folder
                if last_element.isdigit() and int(last_element) == height:
                    continue
                
                # Create target directory if it doesn't exist
                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)

                # Prepare target file path
                target_file_path = os.path.join(target_dir, file)

                # Move the file to the target directory
                try:
                    shutil.move(full_file_path, target_file_path)
                    print(f"Moved {file} to {target_dir}")
                except Exception as e:
                    print(f"Error moving {file}: {e}")

if __name__ == "__main__":
    main()
