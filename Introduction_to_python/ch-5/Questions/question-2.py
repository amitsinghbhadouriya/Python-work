with open(r"Introduction_to_python\ch-5\Questions\practice.txt","r") as f:
    data = f.read()
    
data.replace("Python", "Java")
print(data)