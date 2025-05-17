import json

def get_favorite_number():
    try:
        with open("favorite_number.json", "r") as file:
            data = json.load(file)
            favorite_number = data.get("favorite_number")

            if favorite_number:
                print(f"I know your favorite number! It's {favorite_number}.")
            else:
                print("No favorite number found in the file.")

    except FileNotFoundError:
        favorite_number = input("What's your favorite number? ")
        data = {"favorite_number": favorite_number}

        with open("favorite_number.json", "w") as file:
            json.dump(data, file)

        print(f"Favorite number {favorite_number} saved to 'favorite_number.json'.")

if __name__ == "__main__":
    get_favorite_number()
