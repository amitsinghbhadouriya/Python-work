# simple constructor
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("Amit", 20)
print(p1.name)  
print(p1.age)   


# Constructor Without Parameters
class Car:
    def __init__(self):
        self.brand = "Toyota"
        self.model = "Corolla"
c1 = Car()
print(c1.brand)  
print(c1.model)  


# Constructor with default values
class Laptop:
    def __init__(self, brand="Dell", ram="8GB"):
        self.brand = brand
        self.ram = ram
l1 = Laptop()
l2 = Laptop("HP", "16GB")
print(l1.brand, l1.ram) 
print(l2.brand, l2.ram)  