class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is open!")

# Creating an instance of the Restaurant class
restaurant = Restaurant("Sample Restaurant", "Italian")

# Printing individual attributes
print("Restaurant Name:", restaurant.restaurant_name)
print("Cuisine Type:", restaurant.cuisine_type)

# Calling both methods
restaurant.describe_restaurant()
restaurant.open_restaurant()











class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is open!")

# Create three different instances of the Restaurant class
restaurant1 = Restaurant("Restaurant A", "French")
restaurant2 = Restaurant("Restaurant B", "Japanese")
restaurant3 = Restaurant("Restaurant C", "Mexican")

# Call describe_restaurant() for each instance
restaurant1.describe_restaurant()
print()  # Add a newline for clarity
restaurant2.describe_restaurant()
print()
restaurant3.describe_restaurant()
