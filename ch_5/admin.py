users = ['suraj', 'akash', 'jeet', 'aman', 'nitin', 'shiva', 'anmol']
admin = 'suraj'

for suraj in users:
    if admin == 'suraj':
        print("Hey admin, would you like to see a status report")
    else:
        print(f"Hello {users}, thank you for logging in again")