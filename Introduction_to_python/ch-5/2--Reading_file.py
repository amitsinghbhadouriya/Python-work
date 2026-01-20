# Reading from a file
file = open(r"Introduction_to_python\ch-5\sample.txt","r")
content = file.read()
print(content)
file.close()