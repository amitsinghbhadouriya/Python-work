# Tuples
tuple = (24, 45, 8, 19)
print(tuple)

# type of tuple
print(type(tuple))

# access tuple by indexing
print(tuple[1])
print(tuple[3])

# access tuple by slicing
print(tuple[1:len(tuple)])

# access tuple using loop
for item in tuple:
    print(item)
    
# nested tuple
tup1 = ("Amit", 20)
tup2 = (98.4, "Gwalior")
tup3 = (tup1, tup2)
print(tup3)