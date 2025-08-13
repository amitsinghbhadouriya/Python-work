# Write a program to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary and add one by one. Use subject name as key and marks as value.

dict = {
    
}
x = input("enter wdd grade: ")
dict.update({"Wdd": x})

x = input("enter Math grade: ")
dict.update({"Math": x})

x = input("enter Foc grade: ")
dict.update({"Foc": x})

print(dict)