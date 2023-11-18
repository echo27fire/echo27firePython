from PIL import Image
import os
import shutil

# Define the root directory where the wallpapers are stored
root_dir = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\Widescreen"
ultrawide_dir = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\UltraWide"

def get_image_resolution(image_path):
    with Image.open(image_path) as img:
        return img.width, img.height

def main():
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                full_file_path = os.path.join(subdir, file)

                # Get the resolution of the image
                try:
                    width, height = get_image_resolution(full_file_path)
                except Exception as e:
                    print(f"Error reading {full_file_path}: {e}")
                    continue
                
                # Check if the image is ultra-wide or super ultra-wide
                aspect_ratio = width / height
                
                ultra_wide_ratio = 21 / 9
                super_ultra_wide_ratio = 32 / 9
                
                margin_error = 0.17

                if (ultra_wide_ratio * (1 - margin_error) <= aspect_ratio <= ultra_wide_ratio * (1 + margin_error)) or \
                   (super_ultra_wide_ratio * (1 - margin_error) <= aspect_ratio <= super_ultra_wide_ratio * (1 + margin_error)):
                   
                    # Prepare target file path
                    target_file_path = os.path.join(ultrawide_dir, file)

                    # Move the file to the UltraWide directory
                    try:
                        shutil.move(full_file_path, target_file_path)
                        print(f"Moved {file} to {ultrawide_dir}")
                    except Exception as e:
                        print(f"Error moving {file}: {e}")
                else:
                    # If the image is not ultra-wide or super ultra-wide, it remains in its original location
                    print(f"Skipped {file} with aspect ratio: {aspect_ratio}")

if __name__ == "__main__":
    main()
