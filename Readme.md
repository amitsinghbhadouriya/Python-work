<h1>Introduction To Python</h1>
<h2>What is Python?</h2>
<p>Python is a simple and easy to understand language which feels like reading simple english. This pseudo code nature of python makes it easy to learn and understandable by beginners.</p>
<p>Python is a Case-Sensitive language.</p>

<h2>Use of Comments?</h2>
<p>Comments are used to write something which to programmer does not want to execute.</p>

<h2>What is Variable?</h2>
<p>A variable is a name given to a memory location in a program.</p>

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

<h2>Keywords in python</h2>
<p>Reserved words in python is called keywords.</p>
<p>like :- and, del, else , as, assert , break , etc.</p>

<h2>What is tokens?</h2>
<p>Tokens are the smallest building blocks of the language — the pieces that the Python interpreter understands when reading and executing your code.
</p>

<h2>Type function</h2>
<p>Type function is used to find the data type of a given variable in python.</p>
<pre>
a = 32 
type(a)
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

<h2>Conditional Statements</h2>
<p>Conditional statements are a multiway decision taken by our program due to certain conditions in our code.</p>
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
<ul>
<h3>For loop: </h3>
<p>For loop is used to iterate over a sequence such as a list, tuple, string.<br>It allows to execute a block of code repeatedly.</p>

<h2>What is Strings?</h2>
<p>String is a data type in python. <br> String is a sequence of characters enclosed in quotes.</p>
<b>There are three types of string</b>
<ul>
    <li>Single quoted string</li>
    <li>Double quoted string</li>
    <li>Triple quoted string</li>
</ul>
<h3>Escape Sequence Character</h3>
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

<u>
<h3>String Functions--</h3>
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