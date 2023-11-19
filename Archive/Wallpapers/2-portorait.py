import os
import shutil
from PIL import Image

def scan_and_move_directory(src_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                src_file_path = os.path.join(root, file)
                
                try:
                    with Image.open(src_file_path) as img:
                        width, height = img.size
                        print(f"Processing: {src_file_path} (Dimensions: {width}x{height})")  # Debugging line
                        if height > width:
                            dest_file_path = os.path.join(dest_dir, file)
                            
                            counter = 1
                            while os.path.exists(dest_file_path):
                                filename, file_extension = os.path.splitext(file)
                                dest_file_path = os.path.join(dest_dir, f"{filename}_{counter}{file_extension}")
                                counter += 1

                            shutil.move(src_file_path, dest_file_path)
                            print(f"Moved: {src_file_path} to {dest_file_path} (Dimensions: {width}x{height})")
                        else:
                            print(f"Skipped: {src_file_path} is not a portrait image.")  # Debugging line
                except Exception as e:
                    print(f"Could not open image {src_file_path}: {e}")

if __name__ == "__main__":
    src_dir = r'C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\Widescreen'
    dest_dir = r'C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\Portorait\\111_Landing'
    scan_and_move_directory(src_dir, dest_dir)
