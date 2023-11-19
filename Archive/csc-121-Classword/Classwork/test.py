# Read the charge_accounts.txt file and store the content in a list
try:
    with open('charge_accounts.txt', 'r') as f:
        accounts = [line.strip() for line in f.readlines()]

except FileNotFoundError:
    print("The file charge_accounts.txt was not found.")
    exit()

# Ask the user to enter a charge account number
user_input = input("Enter a charge account number: ")

# Check if the entered number is in the list
if user_input in accounts:
    print("The number is valid.")
else:
    print("The number is invalid.")
