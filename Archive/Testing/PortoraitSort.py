from PIL import Image  # Import the PIL library for image handling
import os  # Import the os library for directory and file manipulation
import shutil  # Import the shutil library for high-level file operations

# Define the root directory path
root_dir = "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\Portorait"

# Function to get the height of an image
def get_image_height(image_path):
    with Image.open(image_path) as img:  # Open the image
        return img.height  # Return the height of the image

# Function to rename files
def rename_files(directory_path):
    file_list = []
    
    # Walk through directories and collect file information
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            full_path = os.path.join(root, file)
            file_stat = os.stat(full_path)
            creation_time = file_stat.st_ctime  # Get file creation time
            file_list.append((creation_time, full_path))
    
    # Sort the list of files by creation time
    file_list.sort(key=lambda x: x[0])
    
    counter = 0  # Initialize a counter
    # Loop through each file to rename it
    for creation_time, full_path in file_list:
        counter_str = str(counter).zfill(5)  # Pad counter with leading zeros
        two_levels_up = os.path.basename(os.path.dirname(os.path.dirname(full_path)))
        original_file_name, file_extension = os.path.splitext(os.path.basename(full_path))
        new_file_name = f"{counter_str}_{two_levels_up}{file_extension}"
        new_full_path = os.path.join(os.path.dirname(full_path), new_file_name)
        os.rename(full_path, new_full_path)  # Rename the file
        print(f"Renamed: {full_path} -> {new_full_path}")  # Log the rename action
        counter += 1  # Increment counter

# Function to scan and move portrait images to a specific directory
def scan_and_move_directory(src_dir, dest_dir):
    if not os.path.exists(dest_dir):  # Create destination directory if it doesn't exist
        os.makedirs(dest_dir)
    
    # Walk through source directory and find image files
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                src_file_path = os.path.join(root, file)
                
                try:
                    with Image.open(src_file_path) as img:  # Open image file
                        width, height = img.size  # Get image dimensions
                        # Check if image is portrait (height > width)
                        if height > width:
                            dest_file_path = os.path.join(dest_dir, file)
                            
                            counter = 1  # Initialize a counter for file naming
                            # Check if destination file already exists
                            while os.path.exists(dest_file_path):
                                filename, file_extension = os.path.splitext(file)
                                dest_file_path = os.path.join(dest_dir, f"{filename}_{counter}{file_extension}")
                                counter += 1  # Increment counter
                            
                            shutil.move(src_file_path, dest_file_path)  # Move the file
                            print(f"Moved: {src_file_path} to {dest_file_path}")  # Log the move action
                        else:
                            print(f"Skipped: {src_file_path} is not a portrait image.")  # Log skipped files
                except Exception as e:
                    print(f"Could not open image {src_file_path}: {e}")  # Log errors related to image opening

# Main function
def main():
    # ... existing sorting and renaming code ...
    # Your existing code for sorting and renaming in root_dir goes here
    
    # Additional code to move portrait images from widescreen to portrait folder
    src_dir = r'C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\Widescreen'
    dest_dir = r'C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers\\Portorait\\111_Landing'
    scan_and_move_directory(src_dir, dest_dir)  # Call the scan and move function

# Entry point of the program
if __name__ == "__main__":
    main()  # Run the main function
