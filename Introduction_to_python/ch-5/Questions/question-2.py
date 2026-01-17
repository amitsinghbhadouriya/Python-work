with open(r"Introduction_to_python\ch-5\Questions\practice.txt","r") as f:
    data = f.read()
    
new_data = data.replace("Python", "Java")
print(new_data)