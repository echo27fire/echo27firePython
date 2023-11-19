from PIL import Image
import os
import shutil

# Define the root directory where the wallpapers are stored
root_dir = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\Widescreen"

aspect_ratios = {
    1.0: "1x1",
    1.33: "4x3",
    1.5: "3x2",
    1.77: "16x9",
    2.0: "18x9",
    2.33: "21x9",
    2.5: "5x2",
    2.77: "25x9",
    3.0: "3x1",
}

def get_image_aspect_ratio(image_path):
    with Image.open(image_path) as img:
        width, height = img.size
        aspect_ratio = width / height
        return aspect_ratio

def closest_aspect_ratio(aspect_ratio):
    closest_ratio_value = min(aspect_ratios.keys(), key=lambda x: abs(x - aspect_ratio))
    return closest_ratio_value, aspect_ratios[closest_ratio_value]

def main():
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                full_file_path = os.path.join(subdir, file)
                
                # Get the aspect ratio of the image
                try:
                    aspect_ratio = get_image_aspect_ratio(full_file_path)
                except Exception as e:
                    print(f"Error reading {full_file_path}: {e}")
                    continue
                
                # Finding the closest common aspect ratio
                closest_ratio_value, closest_ratio_str = closest_aspect_ratio(aspect_ratio)

                # Fudge factor of 15%
                if abs(closest_ratio_value - aspect_ratio) / aspect_ratio <= 0.15:
                    aspect_ratio_str = closest_ratio_str
                else:
                    aspect_ratio_str = str(round(aspect_ratio, 2)).replace('.', 'x')
                
                # Prepare target directory
                target_dir = os.path.join(subdir, aspect_ratio_str)
                
                # Extract the last element of the folder path
                last_element = os.path.basename(os.path.normpath(subdir))
                
                # Skip if the image is already in the correct resolution folder
                if last_element == aspect_ratio_str:
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
