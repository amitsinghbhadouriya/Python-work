foods = ("palak paneer", "rice", "roti", "dal makhni", "salad")
for food in foods:
    print(food)

# foods["rice"] = "custard" --> Throws an error


foods = ("palak paneer", "rice", "roti", "dal makhni", "salad")
print("Original foods:")
for food in foods:
    print(food)

foods = ["palak paneer", "rice", "roti", "custard", "chicken"]
print("\nModified foods:")
for food in foods:
    print(food)