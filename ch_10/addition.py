while True:
    try:
        # Prompt the user for two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Calculate the sum
        result = num1 + num2

        # Print the result
        print(f"The sum of {num1} and {num2} is: {result}")

        break  # Exit the loop if input and calculation were successful

    except ValueError:
        print("Invalid input. Please enter valid numbers.")

