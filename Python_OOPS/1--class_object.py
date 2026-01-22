# Define a class
class Person:
    def __init__(self, name, age):   
        self.name = name             # Attribute
        self.age = age               # Attribute

    # Method
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create objects of the class
person1 = Person("Amit", 20)
person2 = Person("Palak", 19)

# Access attributes
print(person1.name)  
print(person2.age)   

# Call methods
person1.greet()      
person2.greet()     
