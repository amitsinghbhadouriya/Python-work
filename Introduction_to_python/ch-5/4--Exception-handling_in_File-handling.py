try:
    file = open(r"test.txt","r")
    print(file.read())
except FileNotFoundError:
    print("File not found")
finally:
    file.close()