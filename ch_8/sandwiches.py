def make_sandwich(*items):
    print("Creating a sandwich with the following items:")
    for item in items:
        print("- " + item)
    print("Sandwich is ready!\n")

make_sandwich("Turkey", "Lettuce", "Tomato", "Mayonnaise")
make_sandwich("Ham", "Swiss cheese", "Mustard")
make_sandwich("Chicken", "Bacon", "Avocado", "Ranch dressing", "Pickles")
