import json

try:
    with open("favorite_number.json", "r") as file:
        data = json.load(file)
        favorite_number = data.get("favorite_number")
        if favorite_number is not None:
            print(f"I know your favorite number! It's {favorite_number}")
        else:
            print("Your favorite number has not been saved.")
except FileNotFoundError:
    print("No favorite number has been saved yet.")
