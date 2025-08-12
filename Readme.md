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