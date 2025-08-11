# Write a program to find the greatest of 3 numbers entered by the user.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int (input("Enter third number: "))
if(a > b and a > c):
    print("a is greater.")
elif(b > a and b > c):
    print("b is greater.")
else:
    print("c is greater.")