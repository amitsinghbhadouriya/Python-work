# Dictionary methods

dict = {
    "name" : "Amit",
    "age" : 19, 
    "cgpa" : 8.9 
}
print(dict)

# 1. updating dictionary
dict["age"] = 20
print(dict)

# 2. Adding new value
dict["college"] = "Amity"
print(dict)

# 3. Removing key and value from the dictionary
print(dict.pop("name"))
print(dict)

# 4. Access items of a dictionary with their key
print(dict.items())

# 5. Access the keys of a dictionary
print(dict.keys())

# 6. update the dictionary
dict.update({"course":"BCA"})
print(dict)

# 7. Access the single value of a key
print(dict.get("age"))