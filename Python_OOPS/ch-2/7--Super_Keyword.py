class Parent:
    def display(self):
        print("Parent")

class Child(Parent):
    def display(self):
        super().display()
        print("Child")

c = Child()
c.display()
