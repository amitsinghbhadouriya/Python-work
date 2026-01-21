<h1>Introduction To Python</h1>
<h2>What is Python?</h2>
<p>Python is a simple and easy to understand language which feels like reading simple english. This pseudo code nature of python makes it easy to learn and understandable by beginners.</p>

<h2>Features of Python</h2>
<ul>
    <li>Easy to learn and use</li>
    <li>Interpreted language</li>
    <li>High level language</li>
    <li>Case-Sensitive language</li>
    <li>Platform independent</li>
    <li>Open source and free</li>
    <li>Supports multi-programming paradigms</li>
    <li>Rich frameworks and libraries</li>
</ul>

<h2>Application of Python</h2>
<ul>
    <li>Web development</li>
    <li>Data Science and Data analysis</li>
    <li>Artificial Intelligence and Machine Learning</li>
    <li>Automation and Scripting</li>
    <li>Game Development</li>
    <li>Cyber Security and Ethical Hacking</li>
</ul>

<h2>Use of Python</h2>
<ul>
    <li>Creating websites and web applications</li>
    <li>Used in statistics and business analysis</li>
    <li>Building intelligent systems like chatbots</li>
    <li>Automating repetitive tasks</li>
    <li>Used for testing and debugging</li>
    <li>Creating games using libraries like Pygame</li>
    <li>Used in research, calculations, and simulations</li>
</ul>

<h2>Comments?</h2>
<p>Comments are used to write something which to programmer does not want to execute.</p>
<p>There are two types of comments in python.</p>
<ul>
    <li>Single line comment</li>
    <li>Multi line comment</li>
</ul>
<h4>Single line comment :-</h4>
<pre>
# This is a single line comment
</pre>
<h4>Multi line comment :-</h4>
<pre>
''' This is a
    multi line comment '''
</pre>

<h2>Keywords in python</h2>
<p>Reserved words in python is called keywords.</p>
<p>like :-</p>
<pre>and, del, else , as, assert , break , etc.</pre>

<h2>Identifiers in python</h2>
<p>Identifiers are the names used to identify variables, functions, classes, objects, or modules in a program.</p>
<h3>Rules for Identifiers:-</h3>
<ul>
    <li>Must start with a letter (a–z or A–Z) or an underscore (_)</li>
    <li>Cannot start with a number</li>
    <li>Can contain letters, digits, and underscores only</li>
    <li>No spaces allowed</li>
    <li>Case-sensitive (age and Age are different)</li>
    <li>Cannot be a Python keyword (like if, for, class, etc.)</li>
</ul>
<p>Valid Identifiers :-</p>
<pre>name
_age
total_marks
student1
myFunction</pre>
<p>Invalid Identifiers :-</p>
<pre>1name      # starts with a number
total-marks  # contains hyphen
class       # keyword
my name     # space not allowed
</pre>

<h2>Statements</h2>
<p>Statements are instructions written in a program that tell Python what action to perform.</p>

<h2>Indentation</h2>
<p>Python uses indentation instead of braces {}<br/>Indentation defines the block of statements</p>

<h2>What is Variable?</h2>
<p>A variable is a name given to a memory location in a program.</p>
<pre>x = 10
name = "Amit"
</pre>

<h2>What is Data Types?</h2>
<p>A data type defines what kind of value a variable holds and what operations can be performed on it.</p>
<p>There are 5 types of data type.</p>
<ul>
    <li>Integers</li>
    <li>Strings</li>
    <li>Float</li>
    <li>Boolean</li>
    <li>None</li>
</ul>

<h2>What is tokens?</h2>
<p>Tokens are the smallest building blocks of the language — the pieces that the Python interpreter understands when reading and executing your code.
</p>

<h2>Type function</h2>
<p>Type function is used to find the data type of a given variable in python.</p>
<pre>
a = 32 
type(a)
</pre>

<h2>Type Conversion</h2>
<p>Type conversion means changing one data type into another.</p>
<h3>Types of Type Conversion</h3>
<ul>
    <li>Implicit Type Conversion</li>
    <li>Explicit Type Conversion</li>
</ul>
<h4>Implicit Type Conversion :-</h4>
<ul>
    <li>Done automatically by Python</li>
    <li>Converts smaller data type to larger ones</li>
</ul>
<pre>
x = 10      # int
y = 2.5     # float
z = x + y  # result is float
</pre>
<h4>Explicit Type Conversion (Type Casting) :-</h4>
<ul>
    <li>Done manually by the programmer</li>
    <li>Uses built-in functions</li>
</ul>
<pre>
a = int(3.8)      # 3
b = float(5)      # 5.0
c = str(100)      # "100"
d = bool(1)       # True
</pre>

<h2>Input function</h2>
<p>Input function allows the user to take input from the keyword as a string.</p>
<pre>a = input("Enter name: ")</pre>

<h2>Operators in python</h2>
<ul>
    <li>Arithmetic operators :- +, -, *, /, etc.</li>
    <li>Assignment operators :- =, +=, -=, etc.</li>
    <li>Comparison operators :- ==, >, >=, <, <=, !=, etc.</li>
    <li>Logical operators :- and, or, not</li>
</ul>

<h2>Namespaces</h2>
<p>A namespace is a collection of names mapped to objects in Python. Python uses built-in, global, local, and enclosing namespaces to avoid name conflicts.</p>

<h2>Conditional Statements</h2>
<p>Conditional statements are a multi-way decision taken by our program due to certain conditions in our code.</p>
<h4>Syntax:</h4>
<pre>
if(condition1):
    statement1
elif(condition2):
    statement2
else:
    statement3
</pre>

<h2>What is Loops?</h2>
<p>Loops are used to repeat action efficiently.</p>
<p>There are two types of loops in python:</p>
<ul>
    <li>For loop</li>
    <li>While loop</li>
</ul>
<h3>For loop: </h3>
<p>For loop is used to iterate over a sequence such as a list, tuple, string.<br>It allows to execute a block of code repeatedly.</p>
<pre>
a = 4;
for i in range(0, a):
    print(i)
</pre>

<h3>While loop: </h3>
<p>While loop is used to execute a block of statements repeatedly until a given condition is satisfied. When the condition becomes false, the line immediately after the loop in the program is executed.</p>
<pre>
n = int(input("Enter the number: "))
while(n < 5):
    n = n + 1
    print("Hello World")
</pre>

<h3>Break:</h3>
<p>It is used to terminate the loop when encountered.</p>
<pre>
i = 1
while(i <= 8):
    print(i)
    if(i==4):
        break
    i += 1
    
print("loop is ended.")
</pre>

<h3>Continue:</h3>
<p>It is used to terminates execution in the current iteration and continues execution of the loop with the next iteration.</p>
<pre>
i = 1
while(i <= 8):
    if(i==4):
        i += 1
        continue
    print(i)
    i += 1
    
print("loop is ended.")
</pre>

<h3>Range:</h3>
<p>Range functions returns a sequence of numbers, starting from 0 by default, and increments by 1(by default), and stops before a specified number.</p>
<pre>
seq = range(7)
for i in seq:
    print(i)
</pre>    
<pre>
seq2 = range(1,5)
for i in seq2:
    print(i)
</pre>
<pre>
seq3 = range(1,9,2)
for i in seq3:
    print(i)
</pre>

<h2>What is Strings?</h2>
<p>String is a data type in python. <br> String is a sequence of characters enclosed in quotes.</p>
<b>There are three types of string</b>
<ul>
    <li>Single quoted string</li>
    <li>Double quoted string</li>
    <li>Triple quoted string</li>
</ul>

<h3>Single quoted string:</h3>
<pre>
name = 'Amit'
print(name)
</pre>

<h3>Double quoted string:</h3>
<pre>
name = "Amit"
print(name)
</pre>

<h3>Triple quoted string:</h3>
<pre>
name = '''Amit'''
print(name)
</pre>

<u>
<h3>Escape Sequence Character</h3>
</u>
<p>Sequence of character after backslash '\'. <br>Escape sequence character comprises of more than one characters but represents one character when used within the string.</p>
<table>
    <tr>
        <th>ESC</th>
        <th>Meaning</th>
    </tr>
    <tr>
        <td>\n</td>
        <td>New Line</td>
    </tr>
    <tr>
        <td>\t</td>
        <td>Tab</td>
    </tr>
    <tr>
        <td>\'</td>
        <td>Single Quote</td>
    </tr>
    <tr>
        <td>\\</td>
        <td>Backslash</td>
    </tr>
</table>
<pre>
str = "I like python. /nPython is a simple and easy language"
print(str)
</pre>


<h3>String Functions :-</h3>
</u>
<b>Length Function:</b>
<p>This function return the length of the string.</p>
<pre>
a = "Amit"
print(len(a))
</pre>

<b>Concatenation: </b>
<p>Concatenation means adding two strings in a single string.</p>
<pre>
str1 = "Amit"
str2 = "Singh"
str3 = str1 + str2
print(str3)
</pre>

<b>String Count: </b>
<p>Counts the total number of occurence of any character.</p>
<pre>
str = "eurogames"
print(str.count("e"))
</pre>

<b>String Capitalize: </b>
<p>This function capitalize the first character of a given string.</p>
<pre>
str = "eurogames"
print(str.capitalize())
</pre>

<b>String find(word): </b>
<p>This function finds a word and returns the index of first occurence of that word in the string.</p>
<pre>
str = "eurogames"
print(str.find("games"))
</pre>

<b>String Replace: </b>
<p>This function replaces the old word with new word in the entire string.</p>
<pre>
str4 = "I like java."
print(str4.replace("java", "python"))
</pre>

<h3>What is Indexing?</h3>
<p>The index in a string starts from 0 to (length - 1) in python.</p>
<pre>
name = "python"
print(name[3])
</pre>

<h3>What is string slicing?</h3>
<p>A string in python can be sliced for getting a part of the string.</p>
<pre>
a = "I learn python"
print(a[1:8])
</pre>

<h2>What is list?</h2>
<ul>
    <li>List are containers to store a set of values of any data type.</li>
    <li>List are mutable, we can modify, replace and delete items.</li>
    <li>List are ordered. It maintain the order of elements based on how they are added.</li>
    <li>Accessing item in list can be done directly using their position.</li>
</ul>
<pre>
list = ["Amit", 20, 98.4, "Gwalior", "Amity"]
print(list)
print(type(list))   # Check the type of list
print(list[1])      # accessing list using index
print(list[0:3])    # accessing list using slicing
for item in list:   # accessing list using for loop
    print(item)
</pre>

<h3>List Methods</h3>
<b>sort:</b>
<p>It will sort the list in ascending order.</p>
<pre>
list = [2,6,29,5,17,4]
list.sort()
print(list)
</pre>

<b>reverse:</b>
<p>It will reverse the list. </p>
<pre>
list = [2,6,29,5,17,4]
list.reverse()
print(list)
</pre>

<b>append:</b>
<p>It adds an element at the end of the list.</p>
<pre>
list = [2,6,29,5,17,4]
list.append(19)
print(list)
</pre>

<b>insert:</b>
<p>It adds an element at a specific position.</p>
<pre>
list = [2,6,29,5,17,4]
list.insert(1, 23)
print(list)
</pre>

<b>extend:</b>
<p>It adds multiple elements to the end of the list.</p>
<pre>
list = [2,6,29,5,17,4]
list.extend([34, 15, 9])
print(list)
</pre>

<b>pop:</b>
<p>It removes the element at a specific index or the last element if no index is specified.</p>
<pre>
list = [2,6,29,5,17,4]
list.pop(3)
print(list)
</pre>

<b>remove: </b>
<p>It removes the first occurrence of an element.</p>
<pre>
list = [2,6,29,5,17,4]
list.remove(29)
print(list)
</pre>

<h2>What is Tuple?</h2>
<ul>
    <li>A tuple is an immutable ordered collection of elements.</li>
    <li>Tuple can hold element of different data types.</li>
    <li>The main characteristics of tuples are being ordered , heterogeneous and immutable.</li>
    <li>Tuples are similar to lists, but unlike lists, they cannot be changed after their creation </li>
</ul>
<pre>
tuple = (24, 45, 8, 19)
print(tuple)
print(type(tuple))      # type of a tuple
print(tuple[1])         # accessing tuple using indexing
for item in tuple:      # accessing tuple using loop
    print(item)
</pre>

<h3>Nested Tuple</h3>
<pre>
tup1 = ("Amit", 20)
tup2 = (98.4, "Gwalior")
tup3 = (tup1, tup2)
print(tup3)
</pre>

<h3>Tuple Methods</h3>
<b>concatenation:</b>
<p>It adds the two tuple in a single tuple.</p>
<pre>
tup1 = (12, 45)
tup2 = ("Hello", "world")
tup3 = tup1 + tup2
print(tup3)
</pre>

<b>count:</b>
<p>It counts the number of times element occur in the tuple.</p>
<pre>
num = (1, 4, 5, 1, 8, 9, 1, 19, 32, 1)
print(num.count(1))
</pre>

<b>index:</b>
<p>It displays the index position the element placed in it.</p>
<pre>
num = (1, 4, 5, 1, 8, 9, 1, 19, 32, 1)
print(num.index(5))
</pre>

<h2>What is dictionary?</h2>
<p>Dictionary is a collection of key value pairs.</p>
<h3>Properties of dictionaries:</h3>
<ul>
    <li>It is unordered.</li>
    <li>It is mutable.</li>
    <li>It is indexed.</li>
    <li>It can not contain duplicate keys.</li>
</ul>

<pre>
dict = {
    "name" : "Amit",
    "age" : 19, 
    "cgpa" : 8.9 
}
print(dict)
print(dict["age"])
print(type(dict))         # type of dictionaries
</pre>

<h3>Nested Dictionaries</h3>
<p>Nested dictionaries means creating a dictionary inside another dictionary.</p>
<pre>
dict = {
    "name" : "Amit",
    "age" : 19, 
    "cgpa" : 8.9,
    "Course" : "BCA",
    "Subject-Grade" : {
        "WDD" : "O",
        "Maths" : "A+",
        "COF" : "A+",
        "C++" : "A",
        "CO" : "B+"
    }
}
print(dict)
print(dict["Subject-Grade"]["WDD"])     # Accessing value of key present in the dictionary of another dictionary
</pre>

<h3>Dictionary Methods</h3>
<b>Items:</b>
<p>It returns a list of (key, value) tuples.</p>
<pre>
dict = {
    "name" : "Amit",
    "age" : 19, 
    "cgpa" : 8.9 
}
print(dict.items())
</pre>

<b>Keys:</b>
<p>It returns a list containing dictionary's keys.</p>
<pre>
dict = {
    "name" : "Amit",
    "age" : 19, 
    "cgpa" : 8.9 
}
print(dict.keys())
</pre>

<b>Update:</b>
<p>It updates the dictionary with supplied key value pairs.</p>
<pre>
dict = {
    "name" : "Amit",
    "age" : 19, 
    "cgpa" : 8.9 
}
dict.update({"course":"BCA"})
print(dict)
</pre>

<b>Get:</b>
<p>It returns the value of a specified keys.</p>
<pre>
dict = {
    "name" : "Amit",
    "age" : 19, 
    "cgpa" : 8.9 
}
print(dict.get("age"))
</pre>

<b>Pop:</b>
<p>It removes the key and value pairs from the dictionary.</p>
<pre>
dict = {
    "name" : "Amit",
    "age" : 19, 
    "cgpa" : 8.9 
}
print(dict.pop("name"))
print(dict)
</pre>

<h2>What is set?</h2>
<p>Set is a collection of non repetitive elements.</p>
<h3>Properties of sets:</h3>
<ul>
    <li>Sets are unordered.</li>
    <li>Sets are un-indexed.</li>
    <li>There are no way to change items in sets.</li>
    <li>Sets can not contain duplicate values.</li>
</ul>
<pre>
a = {1,2,3,4}
print(a)
print(type(a))       # Accessing the type of a set
</pre>

<h3>Creating a set using a set function</h3>
<pre>
set1 = set()
print(set1)
set1 = set("hello world")
print(set1)
</pre>

<h3>Creating a set with the help of a list</h3>
<pre>
set1 = set(["Hello", "World", "Hello"])
print(set1)
</pre>

<h3>Creating a set with the help of a tuple</h3>
<pre>
tup = ("Hello", "World", "Hello")
print(set(tup))
</pre>

<h3>Set Methods:</h3>
<b>length:</b>
<p>This method counts the number of element present in the set.</p>
<pre>
s = [4,1,3,8,5,2,9,6]
print(len(s)) 
</pre>

<b>union:</b>
<p>It adds the element in the last of the set if the element is not present in the set.</p>
<pre>
s = [4,1,3,8,5,2,9,6]
s = set(s)
s = s.union({12, 45})
print(s)
</pre>

<b>Intersection:</b>
<p>It displays the elements that are present in both the set and the values given by the user.</p>
<pre>
s = [4,1,3,8,5,2,9,6]
s = set(s)
s = s.intersection({9, 3})
print(s)
</pre>

<b>remove:</b>
<p>It removes the specified element from the set.</p>
<pre>
s = [4,1,3,8,5,2,9,6]
s.remove(3)  
print(s)
</pre>

<b>clear:</b>
<p>It removes all elements from the set, making it an empty set.</p>
<pre>
s = [4,1,3,8,5,2,9,6]
s.clear()  
print(s)
</pre>

<h2>Functions</h2>
<p>A function is a block of reusable code that performs a specific task.</br>It helps in code reusability, readability, and modularity.</p>
<h3>Defining a function :-</h3>
<p>A function is defined using the def keyword.</p>
<pre>
def function_name(parameters):
    statements
    return value
</pre>
<p>Example :</p>
<pre>
def add(a, b):
    return a + b
</pre>
<h3>Calling a function :-</h3>
<p>Calling a function means executing the function to perform the task defined inside it.</p>
<pre>
function_name(arguments)
</pre>
<p>Example :</p>
<pre>
result = add(5, 3)
print(result)
</pre>
<h3>Types of Function</h3>
<ul>
    <li>Built-in Functions</li>
    <li>User-Defined Functions</li>
</ul>
<h4>Built-in Functions :-</h4>
<p>Already provided by Python.</p>
<pre>print(), len(), type(), input()</pre>
<h4>Used-Defined Functions :-</h4>
<p>Created by the programmer.</p>
<pre>
def greet():
    print("Hello")
</pre>
<h3>Function Arguments</h3>
<p>Function arguments are the values passed to a function when it is called.<br>They allow functions to work with different data.</p>
<pre>
def add(a, b):
    print(a + b)
add(5, 3)
</pre>
<h4>Types of Arguments :-</h4>
<ul>
    <li>Positional Arguments</li>
    <li>Keyword Arguments</li>
    <li>Default Arguments</li>
    <li>Variable-Length Arguments</li>
</ul>
<h4>Positional Arguments :</h4>
<p>Passed in the same order as parameters</p>
<pre>
def add(a, b):
    print(a + b)
add(5, 3)
</pre>
<h4>Keyword Arguments :</h4>
<p>Passed using parameter names</p>
<pre>
add(b=3, a=5)
</pre>
<h4>Default Arguments :</h4>
<p>Provide default values to parameters</p>
<pre>
def greet(name, msg="Hello"):
    print(msg, name)
greet("Amit")
</pre>
<h4>Variable-Length Arguments :</h4>
<p>Used when the number of arguments is not fixed.</p>
<ol>
    <li>*args (Non-keyword arguments) -</li>
    <pre>
    def total(*numbers):
        print(sum(numbers))
    total(1, 2, 3, 4)
    </pre>
    <li>**kwargs (Keyword arguments) -</li>
    <pre>
    def details(**info):
        print(info)
    details(name="Amit", age=20)
    </pre>
</ol>
<h3>Anonymous Function</h3>
<p>An anonymous function is a function without a name.
In Python, anonymous functions are created using the lambda keyword.</p>
<b>Syntax :-</b>
<pre>lambda arguments: expression</pre>
<p>Example:</p>
<pre>
square = lambda x: x * x
print(square(5))
</pre>
<h2>Recursion</h2>
<p>Recursion is a process in which a function calls itself to solve a problem.</p>
<h4>Parts of Recursive Function :</h4>
<ul>
    <li>Base Case -> condition to stop recursion</li>
    <li>Recursive Case -> function calls itself</li>
</ul>
<p>Example:-</p>
<pre>
def factorial(n):
    if n == 0 or n == 1:      # base case
        return 1
    else:
        return n * factorial(n - 1)  # recursive call

print(factorial(5))
</pre>
<h2>Pass Statement</h2>
<p>The pass statement is a null statement in Python.<br>It does nothing and is used when a statement is syntactically required but no action is needed.</p>
<h4>Why <u>Pass</u> is used :</hr>
<ul>
    <li>To create empty blocks of code</li>
    <li>To avoid errors when code is incomplete</li>
    <li>Used as a placeholder</li>
</ul>
<p>Example:-</p>
<pre>
def my_function():
    pass
</pre>
<h2>Global variable</h2>
<p>A global variable is a variable that is defined outside all functions and can be accessed anywhere in the program.</p>
<pre>
x = 10   # global variable
def show():
    print(x)

show()
print(x)
</pre>
<h2>Local variable</h2>
<p>A local variable is a variable that is declared inside a function and can be used only within that function.</p>
<pre>
def show():
    x = 10   # local variable
    print(x)
show()
</pre>
<h2>Non local variable</h2>
<p>A nonlocal variable is a variable that is defined in an enclosing (outer) function and is accessed or modified inside a nested (inner) function.<br>-> It is neither local nor global.</p>
<h4>Why <u>nonlocal</u> is used :</h4>
<ul>
    <li>To modify a variable from the outer function</li>
    <li>Used in nested functions</li>
</ul>
<pre>
def outer():
    x = 10   # nonlocal variable

    def inner():
        nonlocal x
        x = x + 5
        print("Inner:", x)

    inner()
    print("Outer:", x)

outer()
</pre>

<h2>Exception Handling</h2>
<p>Exception handling is a way to handle runtime errors in a program so that the program does not crash. <br>Python provides try, except, else, finally blocks to handle exceptions.</p>
<h3>What is an Exception?</h3>
<ul>
    <li>An exception is an error that occurs during program execution.</li>
    <li>Example: division by zero, file not found, invalid input.</li>
</ul>
<pre>
x = 5 / 0  # ZeroDivisionError
</pre>
<h3>Advantages </h3>
<ul>
    <li>Prevents program crash</li>
    <li>Provides user-friendly error messages</li>
    <li>Helps in debugging</li>
    <li>Allows controlled execution</li>
</ul>
<h3>try, except, else, finally blocks </h3>
<ul>
    <li><b>Try :</b> The try block is used to wrap the code that might cause an exception.</li>
    <li><b>Except :</b> Handles exceptions raised in the try block..</li>
    <li><b>else :</b> Executes only if no exception occurs in the try block..</li>
    <li><b>Finally :</b> Always executes, whether an exception occurs or not..</li>
</ul>
<p>Ex :</p>
<pre>
try:
    x = int(input("Enter number: "))
    y = 10 / x
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Division result:", y)
finally:
    print("Program ended")
</pre>
<h3>Common Types of Exceptions :</h3>
<table>
    <tr>
        <th>Exception</th>
        <th>Cause</th>
    </tr>
    <tr>
        <td>ZeroDivisionError</td>
        <td>Division by zero</td>
    </tr>
    <tr>
        <td>FileNotFoundError</td>
        <td>File does not exist</td>
    </tr>
    <tr>
        <td>ValueError</td>
        <td>Wrong data type</td>
    </tr>
    <tr>
        <td>TypeError</td>
        <td>Unsupported operation between types</td>
    </tr>
    <tr>
        <td>IndexError</td>
        <td>Index out of range</td>
    </tr>
    <tr>
        <td>KeyError</td>
        <td>Dictionary key not found</td>
    </tr>
    <tr>
        <td>NameError</td>
        <td>Variable not defined</td>
    </tr>
</table>
<h3>Raising Exceptions </h3>
<p>We can manually raise an exception using raise.</p>
<pre>
x = -5
if x < 0:
    raise ValueError("x cannot be negative")
</pre>
<h3>Multiple Exceptions </h3>
<p>Handle multiple exceptions in one except block using a tuple.</p>
<pre>
try:
    x = int(input("Enter number: "))
    y = 10 / x
except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero")
</pre>

<h2>File Handling</h2>
<p>File handling is the process of creating, opening, reading, writing, and closing files stored on secondary storage using a program.<br>Python provides built-in functions to handle files easily.</p>
<h3>Types of Files :</h3>
<p>Python mainly works with two types of files.</p>
<h4>1. Text files</h4>
<ul>
    <li>Store data in readable text form</li>
    <li>Ex:- .txt, .csv, .py</li>
</ul>
<h4>2. Binary files</h4>
<ul>
    <li>Store data in binary (0 and 1) format</li>
    <li>Example: .jpg, .png, .pdf, .mp3</li>
</ul>
<h3>Advantages </h3>
<ul>
    <li>Permanent data storage</li>
    <li>Data sharing</li>
    <li>Easy backup</li>
    <li>Large data handling</li>
</ul>
<h3>Disadvantages </h3>
<ul>
    <li>Slower than memory</li>
    <li>Risk to data corruption</li>
    <li>Needs proper error handling</li>
</ul>
<h3>Opening a File </h3>
<p>A file is opened using the open() function.</p>
<p>Syntax :</p>
<pre>
file_object = open("filename", "mode")
</pre>
<p>Ex:</p>
<pre>
file = open("example.txt", "r")
</pre>
<h4>File modes :-</h4>
<p>File mode defines the purpose for which a file is opened.</p>
<table>
    <tr>
        <th>Mode</th>
        <th>Meaning</th>
    </tr>
    <tr>
        <td>r</td>
        <td>Read only (default)</td>
    </tr>
    <tr>
        <td>w</td>
        <td>Write (Creates and overwrites file)</td>
    </tr>
    <tr>
        <td>a</td>
        <td>Append data</td>
    </tr>
    <tr>
        <td>x</td>
        <td>Create new file</td>
    </tr>
    <tr>
        <td>r+</td>
        <td>Read and write</td>
    </tr>
    <tr>
        <td>w+</td>
        <td>Write and read</td>
    </tr>
    <tr>
        <td>a+</td>
        <td>Append and read</td>
    </tr>
    <tr>
        <td>rb</td>
        <td>Read binary</td>
    </tr>
    <tr>
        <td>wb</td>
        <td>Write binary</td>
    </tr>
    <tr>
        <td>ab</td>
        <td>Append binary</td>
    </tr>
</table>
<h3>Reading From a File </h3>
<pre>
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()
</pre>
<table>
    <tr>
        <th>Method</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>read()</td>
        <td>Reads entire file</td>
    </tr>
    <tr>
        <td>read(n)</td>
        <td>Reads n characters</td>
    </tr>
    <tr>
        <td>readline()</td>
        <td>Reads one line</td>
    </tr>
    <tr>
        <td>readlines()</td>
        <td>Reads all lines as a list</td>
    </tr>
</table>
<h3>Writing to a file </h3>
<pre>
file = open("example.txt", "w")
file.write("Hello Python")
file.close()
</pre>
<table>
    <tr>
        <th>Method</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>write()</td>
        <td>Writes a string</td>
    </tr>
    <tr>
        <td>writelines()</td>
        <td>Writes multiple lines</td>
    </tr>
</table>
<p>Write() does not add new line automatically</p>
<h3>Closing a file </h3>
<p>Closing a file means releasing the file resource after performing read or write operations.</p>
<p>Syntax :</p>
<pre>
file.close()
</pre>
<h3>With statement </h3>
<p>The with statement is used for resource management, especially file handling.<br>
It ensures that a file is automatically closed after its block of code is executed, even if an error occurs.</p>
<p>Syntax :</p>
<pre>
with open("filename", "mode") as file_variable:
</pre>
<p>Ex :</p>
<pre>
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
</pre>
<h3>Exception handling in File handling </h3>
<p>Used to avoid runtime errors.</p>
<pre>
try:
    file = open("test.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found")
finally:
    file.close()
</pre>
<h4>Common error in file handling :-</h4>
<ul>
    <li>File not found error</li>
    <li>Permission error</li>
    <li>Forgetting to close file</li>
    <li>Wrong mode usage</li>
</ul>






