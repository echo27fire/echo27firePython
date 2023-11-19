from PIL import Image
import os
import shutil

# Define the directory where the ultra-wide wallpapers are stored
root_dir = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\UltraWide"

def get_image_width(image_path):
    with Image.open(image_path) as img:
        return img.width

def main():
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                full_file_path = os.path.join(subdir, file)

                # Get the width of the image
                try:
                    width = get_image_width(full_file_path)
                except Exception as e:
                    print(f"Error reading {full_file_path}: {e}")
                    continue
                
                # Prepare target directory
                target_dir = os.path.join(root_dir, str(width))

                # Skip if the image is already in the correct resolution folder
                if os.path.normpath(subdir) == os.path.normpath(target_dir):
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
