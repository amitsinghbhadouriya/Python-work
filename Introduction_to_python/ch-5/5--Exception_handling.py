try:
    x = int(input("Enter number: "))
    y = 10 / x
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Division result:", y)
finally:
    print("Program ended")