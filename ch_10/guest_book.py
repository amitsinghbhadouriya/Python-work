guest_list = []

while True:
    user_name = input("Please enter your name (or 'q' to quit): ")
    
    if user_name.lower() == 'q':
        break
    
    guest_list.append(user_name)

with open('guest_book.txt', 'w') as file:
    for name in guest_list:
        file.write(name + '\n')

print("Names have been recorded in 'guest_book.txt'.")
