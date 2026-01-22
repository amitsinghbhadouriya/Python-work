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