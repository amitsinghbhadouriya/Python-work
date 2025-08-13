# Dictionaries
dict = {
    "name" : "Amit",
    "age" : 19, 
    "cgpa" : 8.9 
}
print(dict)
print(dict["age"])

# type of dictionaries
print(type(dict)) 

# Nested dictionaries
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