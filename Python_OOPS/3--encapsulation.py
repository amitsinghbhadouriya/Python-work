class Student:
    def __init__(self, name, age):
        self.__name = name       # Private attribute
        self.__age = age         # Private attribute

    # Getter method (to access private data)
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    # Setter method (to modify private data)
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age!")

# Creating object
s1 = Student("Amit", 20)

# Accessing private data using getter
print(s1.get_name())
print(s1.get_age())   

# Modifying private data using setter
s1.set_age(21)
print(s1.get_age())   

# Trying to access private attribute directly will fail
# print(s1.__age)     # AttributeError
