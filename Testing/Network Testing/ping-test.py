import os

hostname = "8.8.8.8"  # Google's public DNS server
response = os.system("ping -c 1 " + hostname)

if response == 0:
    print(f'{hostname} is up.')
else:
    print(f'{hostname} is down.')
