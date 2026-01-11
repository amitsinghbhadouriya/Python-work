# positional arguments
def add(a, b):
    print(a + b)
    
result = add(5, 3)  
print(result)
print('\n')

# Key word arguments
def student_info(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

info = student_info(age=20, course="Python", name="Amit")  
print(info)
print('\n')

# Default argument
def greet(name, msg="Hello"):    
    print(msg, name)
    
greeting = greet("Amit")    
print(greeting)
print('\n')

# Variable length arguments
# a. *args
def total(*numbers):
    print(sum(numbers))
    
num = total(1, 2, 3, 4)
print(num)
print('\n')

# b. **kwargs
def details(**info):
    print(info)

det = details(name="Amit", age=20)
print(det)