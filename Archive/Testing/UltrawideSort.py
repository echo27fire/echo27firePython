from PIL import Image
import os
import shutil

# Define the directories where the wallpapers are stored
root_dir = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\Widescreen"
ultrawide_dir = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\UltraWide"

def get_image_resolution(image_path):
    with Image.open(image_path) as img:
        return img.width, img.height

def main():
    # Part 1: Identify and move ultra-wide wallpapers to the UltraWide directory
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                full_file_path = os.path.join(subdir, file)

                try:
                    width, height = get_image_resolution(full_file_path)
                except Exception as e:
                    print(f"Error reading {full_file_path}: {e}")
                    continue

                aspect_ratio = width / height
                ultra_wide_ratio = 21 / 9
                super_ultra_wide_ratio = 32 / 9
                margin_error = 0.17

                if (ultra_wide_ratio * (1 - margin_error) <= aspect_ratio <= ultra_wide_ratio * (1 + margin_error)) or \
                   (super_ultra_wide_ratio * (1 - margin_error) <= aspect_ratio <= super_ultra_wide_ratio * (1 + margin_error)):
                   
                    target_file_path = os.path.join(ultrawide_dir, file)
                    try:
                        shutil.move(full_file_path, target_file_path)
                        print(f"Moved {file} to {ultrawide_dir}")
                    except Exception as e:
                        print(f"Error moving {file}: {e}")

    # Part 2: Organize ultra-wide wallpapers in the UltraWide directory based on their widths
    for subdir, _, files in os.walk(ultrawide_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                full_file_path = os.path.join(subdir, file)
                
                try:
                    width, _ = get_image_resolution(full_file_path)
                except Exception as e:
                    print(f"Error reading {full_file_path}: {e}")
                    continue
                
                target_dir = os.path.join(ultrawide_dir, str(width))

                if os.path.normpath(subdir) == os.path.normpath(target_dir):
                    continue
                
                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)

                target_file_path = os.path.join(target_dir, file)

                try:
                    shutil.move(full_file_path, target_file_path)
                    print(f"Moved {file} to {target_dir}")
                except Exception as e:
                    print(f"Error moving {file}: {e}")

if __name__ == "__main__":
    main()
