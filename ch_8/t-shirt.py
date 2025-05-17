def make_shirt(size, message):
    print(f"Creating a {size} shirt with the message: '{message}'")

# Calling the function using positional arguments
make_shirt("Medium", "Hello, World!")

# Calling the function using keyword arguments
make_shirt(size="Large", message="Python Lover")







def make_shirt(size='large', message='I love Python'):
    print(f"Creating a {size} shirt with the message: '{message}'")

make_shirt()

make_shirt(size='Medium')

make_shirt(size="Small", message="Keep Calm and Code On")