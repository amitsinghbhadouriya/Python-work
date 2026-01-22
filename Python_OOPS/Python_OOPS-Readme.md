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
<p>A class is a blueprint or template used to create objects.<br>It defines data (variables) and behavior (methods).</p>
<p>Syntax:</p>
<pre>
class Student:
    pass
</pre>

<h2>Object</h2>
<p>An object is an instance of a class.<br>
It represents a real-world entity.</p>
<pre>
s1 = Student()
</pre>

<h2>__init__() Constructor</h2>
<p>A constructor is a special method that is automatically executed when an object is created.</p>
<h4>Purpose:</h4>
<p>Initialize object data</p>
<pre>
class Student:
    def __init__(self, name):
        self.name = name
</pre>

<h2>Instance Variables</h2>
<p>Variables that belong to individual objects.</p>
<pre>
self.name = name
</pre>

<h2>Class Variables</h2>
<p>Variables that are shared by all objects of a class.</p>
<pre>
class Student:
    college = "ABC College"
</pre>

<h2>Methods</h2>
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

<h2>Encapsulation</h2>
<p>Encapsulation means binding data and methods together and restricting access.</p>
<h3>Access Modifiers :</h3>
<table>
    <tr>
        <th>Type</th>
        <th>Syntax</th>
    </tr>
    <tr>
        <td>Public</td>
        <td>name</td>
    </tr>
    <tr>
        <td>Protected</td>
        <td>_name</td>
    </tr>
    <tr>
        <td>Private</td>
        <td>__name</td>
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