user_name = input("Please enter your name: ")

with open('guest.txt', 'w') as file:
    file.write(user_name)

print(f"Hello, {user_name}! Your name has been written to 'guest.txt'.")
