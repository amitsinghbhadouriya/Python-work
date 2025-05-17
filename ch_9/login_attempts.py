class User:
    def __init__(self, first_name, last_name, age, email, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.city = city
        self.login_attempts = 0  # New attribute for login attempts

    def describe_user(self):
        print(f"User Information:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"City: {self.city}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome to our platform.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

# Create an instance of the User class
user = User("John", "Doe", 30, "john.doe@example.com", "New York")

# Call increment_login_attempts() several times
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# Print the value of login_attempts
print(f"Login Attempts: {user.login_attempts}")

# Call reset_login_attempts()
user.reset_login_attempts()

# Print login_attempts again to verify it was reset to 0
print(f"Login Attempts after reset: {user.login_attempts}")
