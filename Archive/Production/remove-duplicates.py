import os
import hashlib

def calculate_hash(file_path):
    hash_object = hashlib.sha256()
    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            hash_object.update(chunk)
    return hash_object.hexdigest()

def remove_duplicates(directory):
    hash_map = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_hash(file_path)
            
            if file_hash not in hash_map:
                hash_map[file_hash] = []
            
            hash_map[file_hash].append({
                "path": file_path,
                "mtime": os.path.getmtime(file_path)
            })
    
    for _, file_info_list in hash_map.items():
        if len(file_info_list) > 1:
            file_info_list.sort(key=lambda x: x['mtime'], reverse=True)
            for file_info in file_info_list[1:]:
                print(f"Removing duplicate file: {file_info['path']}")
                os.remove(file_info['path'])

if __name__ == "__main__":
    directories = [
        "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers"
    ]
    
    for directory in directories:
        remove_duplicates(directory)
