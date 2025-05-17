while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is: {result}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        continue  

    another_calculation = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if another_calculation != 'yes':
        break  
