import os
import hashlib
import subprocess

def calculate_hash(file_path):
    hash_object = hashlib.sha256()
    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            hash_object.update(chunk)
    return hash_object.hexdigest()

def create_dummy_file(file_info):
    dummy_path = file_info['path']
    with open(dummy_path, 'w') as dummy_file:
        dummy_file.write('')
    os.utime(dummy_path, (file_info['mtime'], file_info['mtime']))
    subprocess.run(["attrib", "+h", dummy_path])

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
                print(f"Replacing file with hidden blank dummy: {file_info['path']}")
                os.remove(file_info['path'])
                create_dummy_file(file_info)

if __name__ == "__main__":
    directories = [
        "C:\\Users\\echo2\\OneDrive\\Pictures\\Wallpapers"
    ]
    
    for directory in directories:
        remove_duplicates(directory)
