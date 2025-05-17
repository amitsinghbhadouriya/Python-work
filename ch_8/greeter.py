def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}")

greet_user('jesse')






def display_message():
    print("we were learning functions in python in this chapter")

display_message()







def favorite_book(title):
    print("One of my favorite books is " + title)

favorite_book("Alice in Wonderland")








def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


# This is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    
    f_name = input("First name:")
    if f_name == 'q':
        break

    l_name = input("Last name:")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")