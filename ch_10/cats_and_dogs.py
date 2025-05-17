with open('cats.txt', 'w') as cat_file:
    cat_file.write("Whiskers\nFluffy\nMittens")

with open('dogs.txt', 'w') as dog_file:
    dog_file.write("Buddy\nRex\nLuna")

try:
    with open('cats.txt', 'r') as cat_file:
        cat_contents = cat_file.read()
        print("Contents of cats.txt:")
        print(cat_contents)

    with open('dogs.txt', 'r') as dog_file:
        dog_contents = dog_file.read()
        print("\nContents of dogs.txt:")
        print(dog_contents)

    with open('birds.txt', 'r') as bird_file:
        bird_contents = bird_file.read()
        print("\nContents of birds.txt:")
        print(bird_contents)

except FileNotFoundError as e:
    print(f"File not found: {e.filename}")

import shutil
shutil.move('cats.txt', 'new_location/cats.txt')

try:
    with open('cats.txt', 'r') as cat_file:
        cat_contents = cat_file.read()
        print("\nContents of cats.txt:")
        print(cat_contents)

except FileNotFoundError as e:
    print(f"File not found: {e.filename}")
