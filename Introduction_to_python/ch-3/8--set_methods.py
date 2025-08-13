# Start with a list
s = [4,1,3,8,5,2,9,6]

# 1. length
print(len(s)) 

# Convert to set
s = set(s)

# 2. union
s = s.union({12, 45})
print("After union:", s)

# 3. intersection 
s = s.intersection({9, 3})
print("After intersection:", s)

# 4. remove
s.remove(3)  
print("After remove:", s)

# 5. clear
s.clear()
print("After clear:", s)
