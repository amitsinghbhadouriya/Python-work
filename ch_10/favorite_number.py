import json

favorite_number = input("Enter your favorite number: ")

data = {"favorite_number": favorite_number}

with open("favorite_number.json", "w") as file:
    json.dump(data, file)

print("Favorite number saved to 'favorite_number.json'.")
