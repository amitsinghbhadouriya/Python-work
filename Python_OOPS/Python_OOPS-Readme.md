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
<p>Encapsulation means binding data and methods together and restricting access.</p>
<h4>Benefits :</h4>
<ul>
    <li>Code reusability</li>
    <li>Faster development</li>
</ul>
<h4>Syntax :</h4>
<pre>
class Child(Parent):
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

<h2>Polymorphism</h2>
<p>Polymorphism means same function name, different behavior.</p>
<p>Example :</p>
<pre>
print(len("Hello"))
print(len([1,2,3]))
</pre>

<h3>Method Overloading</h3>
<p>Same method name, different parameters.<br>
(Python supports it using default arguments.)</p>
<pre>
def add(a=0, b=0):
    return a + b
</pre>

<h3>Method Overriding</h3>
<p>Child class redefines parent class method.</p>
<pre>
class Parent:
    def show(self):
        print("Parent")
class Child(Parent):
    def show(self):
        print("Child")
</pre>

<h2>Abstraction</h2>
<p>Abstraction hides internal implementation and shows only necessary details.</p>
<h4>Achieved using:</h4>
<ul>
    <li>Abstract class</li>
    <li>Abstract method</li>
</ul>
<h3>Abstract Class</h3>
<p>A class that contains at least one abstract method.<br>Uses abc module.</p>
<pre>
from abc import ABC, abstractmethod
</pre>
<h3>Abstract Method</h3>
<p>A method with no body.</p>
<pre>
@abstractmethod
def show(self):
    pass
</pre>

<h2>self Keyword</h2>
<p>Refers to current object<br>Used to access instance variables</p>

<h2>super() Function</h2>
<p>Used to call parent class methods.</p>
<pre>
super().__init__()
</pre>

<h2>Destructor (__del__)</h2>
<p>Executed when object is destroyed.</p>
<pre>
def __del__(self):
    print("Object destroyed")
</pre>

<h2>Operator Overloading</h2>
<p>Changing meaning of operators using special methods.</p>
<pre>
def __add__(self, other):
    return self.x + other.x
</pre>

<h2>Data Hiding</h2>
<p>Achieved using private variables.</p>
<pre>
self.__password
</pre>






