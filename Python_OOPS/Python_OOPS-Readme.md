# Python OOPS
<h2>Object Oriented Programming (OOP)</h2>
<p>OOP is a programming approach that organizes code using objects and classes instead of only functions.</p>

<h2>Advantages</h2>
<ul>
    <li>Code reusability</li>
    <li>Better security</li>
    <li>Easy maintenance</li>
    <li>Real-world modeling</li>
</ul>

<h2>Class</h2>
<p>A class is a blueprint or template used to create objects.<br>It defines data (variables) and behavior (methods) of an object.</p>
<p>Syntax:</p>
<pre>
class ClassName:
    # data members
    # member functions
</pre>
<h3>Components of a Class</h3>
<ul>
    <li>Data members (Variables)</li>
    <li>Member Functions (Methods)</li>
</ul>

<h2>Data members (Variables)</h2>
<p>Data members are variables defined inside a class that store data related to an object.</p>
<h3>Types of Variables</h3>
<ul>
    <li>Instance variables</li>
    <li>Class variables</li>
</ul>
<h3>Instance Variables :</h3>
<p>Variables that belong to individual objects.</p>
<pre>
self.name = name
</pre>
<h3>Class Variables :</h3>
<p>Variables that are shared by all objects of a class.</p>
<pre>
class Student:
    college = "ABC College"
</pre>

<h2>Member Functions (Methods)</h2>
<p>Functions defined inside a class.</p>
<h3>Types of Methods</h3>
<ol>
    <li>Instance Method</li>
    <li>Class Method</li>
    <li>Static Method</li>
</ol>
<h3>Instance Method :</h3>
<p>Uses self and works on object data.</p>
<pre>
def show(self):
    print(self.name)
</pre>
<h3>Class Method :</h3>
<p>Works on class variables.<br>
Uses @classmethod.</p>
<pre>
@classmethod
def show_college(cls):
    print(cls.college)
</pre>
<h3>Static Method :</h3>
<p>Does not use self or cls.<br>
Uses @staticmethod.</p>
<pre>
@staticmethod
def add(a, b):
    return a + b
</pre>

<h2>Object</h2>
<p>An object is a real-world entity and an instance of a class.<br>It represents data and behavior defined in the class.</p>
<pre>
s1 = Student()
</pre>
<h4>Characteristics of Objects</h4>
<ul>
    <li>Has identity</li>
    <li>Has state (data)</li>
    <li>Has behavior (methods)</li>
    <li>Occupies memory</li>
</ul>

<h2>Constructor</h2>
<p>A constructor is a special method that is automatically called when a new object of a class is created. <br>Its main purpose is to initialize the attributes of the object. <br>In Python, the constructor method is named __init__().</p>
<p>Syntax :</p>
<pre>
class ClassName:
    def __init__(self, parameters):
        # initialization code
        self.attribute1 = value1
        self.attribute2 = value2
</pre>
<ul>
    <li>__init__ is the constructor method.</li>
    <li>self represents the instance of the class.</li>
    <li>parameters can be used to pass values when creating an object.</li>
</ul>
<h3>Simple Constructor</h3>
<pre>
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("Amit", 22)
print(p1.name)  # Output: Amit
print(p1.age)   # Output: 22
</pre>
<p>Here, __init__ initializes name and age when the object p1 is created.</p>
<h3>Constructor Without Parameters</h3>
<pre>
class Car:
    def __init__(self):
        self.brand = "Toyota"
        self.model = "Corolla"
c1 = Car()
print(c1.brand)  # Output: Toyota
print(c1.model)  # Output: Corolla
</pre>
<p>Key Points :</p>
<ul>
    <li>__init__ is automatically called when an object is created.</li>
    <li>We can have parameters in a constructor to initialize attributes dynamically</li>
    <li>We cannot have multiple constructors like in Java or C++; instead, We can use default values or *args and **kwargs.</li>
</ul>
<h3>Constructor with Default Values</h3>
<pre>
class Laptop:
    def __init__(self, brand="Dell", ram="8GB"):
        self.brand = brand
        self.ram = ram
l1 = Laptop()
l2 = Laptop("HP", "16GB")
print(l1.brand, l1.ram)  # Output: Dell 8GB
print(l2.brand, l2.ram)  # Output: HP 16GB
</pre>

<h2>Destructor</h2>
<p>A destructor is a special method that is automatically called when an object is destroyed or removed from memory.
<br>The destructor method is named __del__().<br>It is mainly used to release resources like files, database connections, or network sockets.</p>
<h4>Syntax:</h4>
<pre>
class ClassName:
    def __del__(self):
        # cleanup code
        pass
</pre>

<h2>self Keyword</h2>
<p>The self keyword represents the current object (instance) of a class.<br>
It is used to access instance variables and instance methods inside a class.</p>
<h4>Syntax:</h4>
<pre>
class ClassName:
    def method(self):
        print("This is a method")
</pre>

<h2>Encapsulation</h2>
<p>Encapsulation is the practice of hiding the internal details of a class (its data and methods) and providing controlled access to them through public methods.</p>
<p>It helps in :</p>
<ul>
    <li>Protecting data from unauthorized access.</li>
    <li>Making code more secure and maintainable.</li>
    <li>Providing a clear interface for interacting with an object.</li>
</ul>
<h3>Access Modifiers :</h3>
<table>
    <tr>
        <th>Type</th>
        <th>Syntax</th>
        <th>Purpose</th>
    </tr>
    <tr>
        <td>Public</td>
        <td>name</td>
        <td>accessible from anywhere.</td>
    </tr>
    <tr>
        <td>Protected</td>
        <td>_name</td>
        <td>intended to be accessed only within the class and its subclasses.</td>
    </tr>
    <tr>
        <td>Private</td>
        <td>__name</td>
        <td>intended to be accessed only within the class itself.</td>
    </tr>
</table>

<h2>Inheritance</h2>
<p>Inheritance is an concept where a child class (derived class) inherits properties and methods from a parent class (base class).</p>
<h4>Benefits :</h4>
<ul>
    <li>Code reusability</li>
    <li>Logical hierarchy</li>
    <li>Easy maintenance</li>
    <li>Faster development</li>
</ul>
<h4>Syntax :</h4>
<pre>
class ParentClass:
    # parent class code
    pass
class ChildClass(ParentClass):
    # child class code
    pass
</pre>
<h3>Types of inheritance</h3>
<ol>
    <li>Single</li>
    <li>Multiple</li>
    <li>Multilevel</li>
    <li>Hierarchial</li>
    <li>Hybrid</li>
</ol>
<h3>Single Inheritance</h3>
<p>One child class inherits from one parent class.</p>
<h4>Structure:</h4>
<pre>
A → B
</pre>
<h4>Syntax:</h4>
<pre>
class Animal:
    def eat(self):
        print("Eating")
class Dog(Animal):
    def bark(self):
        print("Barking")
</pre>
<h3>Multiple Inheritance</h3>
<p>One child class inherits from multiple parent classes.</p>
<h4>Structure:</h4>
<pre>
A   B
 \ /
  C
</pre>
<h4>Syntax:</h4>
<pre>
class Father:
    def skill1(self):
        print("Driving")
class Mother:
    def skill2(self):
        print("Cooking")
class Child(Father, Mother):
    pass
</pre>
<h3>Multilevel Inheritance</h3>
<p>A child class inherits from another child class.</p>
<h4>Structure:</h4>
<pre>
A → B → C
</pre>
<h4>Syntax:</h4>
<pre>
class Grandparent:
    def show1(self):
        print("Grandparent")
class Parent(Grandparent):
    def show2(self):
        print("Parent")
class Child(Parent):
    def show3(self):
        print("Child")
</pre>
<h3>Hierarchial Inheritance</h3>
<p>Multiple child classes inherit from one parent class.</p>
<h4>Structure:</h4>
<pre>
    A
   / \
  B   C
</pre>
<h4>Syntax:</h4>
<pre>
class Shape:
    def draw(self):
        print("Drawing shape")
class Circle(Shape):
    pass
class Square(Shape):
    pass
</pre>
<h3>Hybrid Inheritance</h3>
<p>Combination of two or more inheritance types.</p>
<h4>Structure:</h4>
<pre>
    A
   / \
  B   C
   \ /
    D
</pre>
<h4>Syntax:</h4>
<pre>
class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B, C):
    pass
</pre>
<h3>super() Function</h3>
<p>Used to call parent class methods from a child class.</p>
<h4>Structure:</h4>
<pre>
super().__init__()
</pre>
<h4>Syntax:</h4>
<pre>
class Parent:
    def display(self):
        print("Parent")
class Child(Parent):
    def display(self):
        super().display()
        print("Child")
</pre>
<h3>Method Overriding</h3>
<p>When a child class provides its own implementation of a parent class method.</p>
<pre>
class Parent:
    def show(self):
        print("Parent method")
class Child(Parent):
    def show(self):
        print("Child method")
</pre>
<h3>Advantages of Inheritance</h3>
<ul>
    <li>Code reuse</li>
    <li>Faster development</li>
    <li>Easier maintenance</li>
    <li>Clear structure</li>
</ul>
<h3>Disadvantages of Inheritance</h3>
<ul>
    <li>Tight coupling</li>
    <li>Increased complexity</li>
    <li>Improper use can make code difficult to understand</li>
</ul>

<h2>Polymorphism</h2>
<p>Polymorphism means “many forms.”
<br>polymorphism allows the same function or method name to behave differently depending on the object that is calling it.</p>
<h3>Types of Polymorphism</h3>
<ul>
    <li>Compile-Time Polymorphism</li>
    <li>Runtime Polymorphism</li>
</ul>
<h3>Compile-Time Polymorphism</h3>
<p>Python does not support true compile-time polymorphism, but it is achieved using default arguments or *args.</p>
<p>Example :</p>
<pre>
class Math:
    def add(self, a=0, b=0, c=0):
        return a + b + c
m = Math()
print(m.add(2, 3))
print(m.add(2, 3, 4))
</pre>
<h3>Runtime Polymorphism</h3>
<p>Achieved using method overriding and inheritance.</p>
<p>Example :</p>
<pre>
class Animal:
    def speak(self):
        print("Animal makes a sound")
class Dog(Animal):
    def speak(self):
        print("Dog barks")
class Cat(Animal):
    def speak(self):
        print("Cat meows")
animals = [Dog(), Cat(), Animal()]
for a in animals:
    a.speak()
</pre>

<h2>Method Overloading</h2>
<p>Same method name, different parameters.<br>
(Python supports it using default arguments.)</p>
<pre>
def add(a=0, b=0):
    return a + b
</pre>

<h2>Operator Overloading</h2>
<p>Operator Overloading allows us to give special meaning to operators (+, -, *, ==, etc.) when they are used with user-defined objects (classes).</p>
<h4>Example:</h4>
<pre>
class Number:
    def __init__(self, value):
        self.value = value
    def __add__(self, other):
        return self.value + other.value
n1 = Number(10)
n2 = Number(20)
print(n1 + n2)   
</pre>
<h3>Common Operator Overloading Methods</h3>
<table>
    <tr>
        <th>Operator</th>
        <th>Method</th>
    </tr>
    <tr>
        <td>+</td>
        <td>__add__()</td>
    </tr>
    <tr>
        <td>+</td>
        <td>__add__()</td>
    </tr>
    <tr>
        <td>-</td>
        <td>__sub__()</td>
    </tr>
    <tr>
        <td>*</td>
        <td>__mul__()</td>
    </tr>
    <tr>
        <td>/</td>
        <td>__truediv__()</td>
    </tr>
    <tr>
        <td>==</td>
        <td>__eq__()</td>
    </tr>
    <tr>
        <td><</td>
        <td>__lt__()</td>
    </tr>
    <tr>
        <td>></td>
        <td>__gt__()</td>
    </tr>
    <tr>
        <td><=</td>
        <td>__le__()</td>
    </tr>
    <tr>
        <td>>=</td>
        <td>__ge__()</td>
    </tr>
    <tr>
        <td>!=</td>
        <td>__ne__()</td>
    </tr>
</table>

<h2>Abstraction</h2>
<p>Abstraction is a concept that hides the internal details of how something works and shows only the necessary parts to the user..</p>
<h4>Achieved using:</h4>
<ul>
    <li>Abstract class</li>
    <li>Abstract method</li>
</ul>
<h3>Abstract Class</h3>
<p>An abstract class is a class that cannot be instantiated directly.<br>
It is meant to be inherited by other classes.
</p>
<ul>
    <li>Use it when you want to define a common interface for multiple subclasses.</li>
    <li>Abstract classes can have both regular methods (with implementation) and abstract methods (without implementation).</li>
</ul>
<h3>Abstract Method</h3>
<p>An abstract method is a method that is declared, but contains no implementation.
</p>
<ul>
    <li>Subclasses must override abstract methods.</li>
    <li>Abstract methods are created using the @abstractmethod decorator.</li>
</ul>
<pre>
@abstractmethod
def show(self):
    pass
</pre>

<h2>Data Hiding</h2>
<p>Data Hiding is an OOP concept where the internal details (data/attributes) of a class are hidden from outside access.
</p>
<ul>
    <li>This is done to protect sensitive data from accidental modification.</li>
    <li>Only methods inside the class (or specially designed getter/setter methods) can access or modify these hidden attributes.</li>
</ul>
<pre>
self.__password
</pre>







