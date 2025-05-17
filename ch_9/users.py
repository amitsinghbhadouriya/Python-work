class User:
    def __init__(self, first_name, last_name, age, email, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.city = city

    def describe_user(self):
        print(f"User Information:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"City: {self.city}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome to our platform.")

# Create several instances representing different users
user1 = User("John", "Doe", 30, "john.doe@example.com", "New York")
user2 = User("Alice", "Smith", 25, "alice.smith@example.com", "Los Angeles")
user3 = User("Bob", "Johnson", 40, "bob.johnson@example.com", "Chicago")

# Call both methods for each user
user1.describe_user()
user1.greet_user()
print()

user2.describe_user()
user2.greet_user()
print()

user3.describe_user()
user3.greet_user()
