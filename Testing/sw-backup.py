'''
Program: Cisco Backup Automation.
Author: Taylor Goodspeed
Date: 10/30/2023
Version: 0.0

'''
# import modules
from netmiko import ConnectHandler
from datetime import datetime
import os
import sys




# list of DTCC SWITCHES

# configuration of Cisco Switches
devices = [
    { # core 11
        'device_type': 'cisco_ios',
        'host': 'switch_ip_1',
        'username': 'username_1',
        'password': 'password_1',
        'secret': 'enable_password_1',  # if required
    },

    { # core 22
        'device_type': 'cisco_ios',
        'host': 'switch_ip_1',
        'username': 'username_1',
        'password': 'password_1',
        'secret': 'enable_password_1',  # if required
    },

    { # R1SW41
        'device_type': 'cisco_ios',
        'host': 'switch_ip_1',
        'username': 'username_1',
        'password': 'password_1',
        'secret': 'enable_password_1',  # if required
    },

    { # R4SW44 RM219
        'device_type': 'cisco_ios',
        'host': 'switch_ip_1',
        'username': 'username_1',
        'password': 'password_1',
        'secret': 'enable_password_1',  # if required
    },

    { # R3 Netlab IPMI
        'device_type': 'cisco_ios',
        'host': 'switch_ip_1',
        'username': 'username_1',
        'password': 'password_1',
        'secret': 'enable_password_1',  # if required
    },

    { # r3 Netlab
        'device_type': 'cisco_ios',
        'host': 'switch_ip_1',
        'username': 'username_1',
        'password': 'password_1',
        'secret': 'enable_password_1',  # if required
    },

    { # R4 SW 42 Net 41
        'device_type': 'cisco_ios',
        'host': 'switch_ip_1',
        'username': 'username_1',
        'password': 'password_1',
        'secret': 'enable_password_1',  # if required
    },

    { # R7 SW 110
        'device_type': 'cisco_ios',
        'host': 'switch_ip_1',
        'username': 'username_1',
        'password': 'password_1',
        'secret': 'enable_password_1',  # if required
    },

    { # MGMT SW
        'device_type': 'cisco_ios',
        'host': 'switch_ip_1',
        'username': 'username_1',
        'password': 'password_1',
        'secret': 'enable_password_1',  # if required
    },

    { # 112 SW
        'device_type': 'cisco_ios',
        'host': 'switch_ip_1',
        'username': 'username_1',
        'password': 'password_1',
        'secret': 'enable_password_1',  # if required
    },


]


# variables

backup_location = '/var/lib/tftpd'




def osCheck():
    """
    Checks if the operating system is Linux. If not, prints an error message and exits the program.
    """
    if 'linux' not in sys.platform:
        print('this code is intended to run on linux')
        sys.exit(1)

# verify backup directory exists


def verify_backup_dir(directory_target):
    """
    Verify if the backup directory exists. If it does not exist, create it.

    Args:
    directory_target (str): The path to the backup directory.

    Returns:
    None
    """
    if os.path.exists(directory_target) and os.path.isdir(directory_target):
        print("backup directory exists")
    else:
        try:
            os.makedirs(directory_target)
            print("backup directory did not exist and was created")
        except OSError as e:
            print("encountered an OS error")




def backup_config(device, directory):
    """
    Connects to a network device and backs up its running configuration to a file.

    Args:
        device (dict): A dictionary containing the device's connection details.
        directory (str): The directory where the backup file will be saved.

    Returns:
        None
    """
    # connect to the device to be backed up
    net_connect = ConnectHandler(**device)

    if 'secret' in device:
        net_connect.enable()

    # get the current config
    running_config = net_connect.send_command('show running-config')

    # define the filename of the backup config
    current_time = datetime.now().strftime('%Y-%m-%d')
    filename = f"{device['host']}-{current_time}.config"
    backup_path = os.path.join(directory, filename)

    # write the configuration to the backup file
    with open(backup_path, 'w') as file:
        file.write(running_config)
        print(f"Config for {device['host']} at {backup_path} created")

    net_connect.disconnect()



def main():
    osCheck()
    verify_backup_dir(backup_location)

    # loop to back up configurations
    for device in devices:
        try:
            backup_config(device, backup_location)
        except Exception as e:
            print(f"Failed to backup configuration for {device['host']}")
            print(e)

if __name__ == "__main__":
    main()

