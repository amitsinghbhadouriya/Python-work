try:
    x = int(input("Enter number: "))
    y = 10 / x
except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero")