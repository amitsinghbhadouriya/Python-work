while True:
    try:
        age = int(input("Please enter your age (or type '0' to exit): "))
        if age == 0:
            break

        if age < 3:
            ticket_price = 0
        elif 3 <= age <= 12:
            ticket_price = 10
        else:
            ticket_price = 15

        print(f"The ticket price for your age {age} is ${ticket_price}.")
    except ValueError:
        print("Please enter a valid age (a positive integer) or '0' to exit.")