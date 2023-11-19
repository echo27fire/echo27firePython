''' 
Program: docker backup
Author:
Date:
'''

''' 
Use Case:
This program aims to backup docker containers on a server as well as any volumes and other associated files/data.
'''
import os
import zipfile
import shutil
import docker
from zipfile import ZipFile
from datetime import datetime

#path debugger
import sys
print("Using python interpret at :", sys.executable)

def volume_backup(paths, output_file):
    volume_path = "/var/lib/docker/volumes/"  # The path to the docker volumes to back up
    date_str = datetime.now().strftime("%Y-%m-%d")  # Set the date for the backup archive

    # Extract directory and filename from output_file
    output_dir, filename = os.path.split(output_file)
    if not filename:
        raise ValueError("Filename is missing in the output_file path")

    output_filename_with_date = f"{date_str}_{filename}"
    final_output_path = os.path.join(output_dir if output_dir else ".", output_filename_with_date)
    
    with ZipFile(final_output_path, 'w') as archive:
        for path in paths:
            for root, dirs, files in os.walk(path):
                for file in files:
                    archive.write(os.path.join(root, file), 
                                  os.path.relpath(os.path.join(root, file), 
                                  os.path.join(path, '..')))
    
    #shutil.make_archive(final_output_path, 'zip', volume_path)

    # When ready to use, call volume_backup with the desired output file name
    # Example: volume_backup("docker_backup")

def get_containers():

    client = docker.from_env()
    containers = client.containers.list(all=True)
    mount_points = []
    
    for container in containers:
        try:
            print(f"Name: {container.name} ID: {container.id} Image: {', '.join(container.image.tags)} Status: {container.status}")
            container_information = client.api.inspect_container(container.id)
            mounts = container_information.get("Mounts", [])
            
            if mounts:
                for mount in mounts:
                    print(f" SOURCE MOUNT: {mount['Source']}")
                    print(f" DESTINATION MOUNT: {mount['Destination']}")
                    mount_points.append(mount['Source'])
            else:
                print(f"{container.name} has no custom storage locations and is using the default storage location")
            print("\n")
        except Exception as e:
            print(f"Error processing container {container.name}: {e}")

    return mount_points

def stop_containers(containers):
    for container in containers:
        try:
            client.api.stop(container)
            print(f"Container {container} has been stopped")
        except Exception as e:
            print(f"Error stopping container {container}: {e}")

def start_containers(containers):
    for container in containers:
        try:
            client.api.start(container)
        except Exception as e:
            print(f"Error starting container {container}: {e}")

# Example usage
containers = get_containers()
stop_containers(containers)


