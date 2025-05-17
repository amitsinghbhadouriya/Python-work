import random

# Define a list with numbers and letters
ticket_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Randomly select 4 elements from the list
winning_elements = random.sample(ticket_list, 4)

# Print a message
print("Congratulations! Any ticket matching these 4 elements wins a prize:")
print(winning_elements)










import random

# Define the list containing the series of 10 numbers and 5 letters
ticket_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Define your ticket (you can customize this)
my_ticket = [1, 'A', 3, 'B']

# Initialize a variable to keep track of the number of iterations
num_attempts = 0

# Simulate the lottery drawing until your ticket wins
while True:
    num_attempts += 1
    
    # Randomly select 4 elements from the ticket_list
    winning_elements = random.sample(ticket_list, 4)
    
    # Check if the winning_elements match your ticket
    if winning_elements == my_ticket:
        print("Congratulations! You have a winning ticket!")
        print(f"It took {num_attempts} attempts to win.")
        break
