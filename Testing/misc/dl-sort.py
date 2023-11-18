import os
import shutil
import hashlib

# List of common archive extensions
archive_extensions = ['.zip', '.tar', '.rar', '.7z', '.gz']

def get_file_hash(file_path):
    """Returns the hash of the file at file_path."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def remove_empty_folders(path):
    """Recursively remove empty folders."""
    for foldername in os.listdir(path):
        folderpath = os.path.join(path, foldername)
        if os.path.isdir(folderpath):
            remove_empty_folders(folderpath)
            if not os.listdir(folderpath):
                print(f"Removing empty folder: {folderpath}")
                os.rmdir(folderpath)

def main():
    source_dir = "C:\\Users\\echo2\\Downloads"
    hash_set = set()

    if not os.path.exists(source_dir):
        print(f"The path {source_dir} does not exist.")
        return

    for root, dirs, files in os.walk(source_dir):
        # Skip folders with names that match archive extensions
        if any(root.endswith(ext) for ext in archive_extensions):
            print(f"Skipping folder: {root}")
            continue

        for filename in files:
            full_file_path = os.path.join(root, filename)

            # Check for duplicate files based on hash
            file_hash = get_file_hash(full_file_path)
            if file_hash in hash_set:
                print(f"Removing duplicate file: {full_file_path}")
                os.remove(full_file_path)
                continue
            else:
                hash_set.add(file_hash)

            # Only consider files (skip directories)
            if os.path.isfile(full_file_path):
                file_extension = os.path.splitext(filename)[1]

                # Create a new folder for the extension if it doesn't exist
                extension_folder = os.path.join(source_dir, file_extension[1:] if file_extension else "NoExtension")
                if not os.path.exists(extension_folder):
                    os.mkdir(extension_folder)

                # Move file to corresponding extension folder
                dest_file_path = os.path.join(extension_folder, filename)
                print(f"Moving {full_file_path} to {dest_file_path}")
                shutil.move(full_file_path, dest_file_path)

    # Remove empty folders
    remove_empty_folders(source_dir)

if __name__ == "__main__":
    main()
