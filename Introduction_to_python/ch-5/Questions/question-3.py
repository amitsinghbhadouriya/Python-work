# Search if the word "learning" exists in the file or not.

word = "learning"
with open(r"Introduction_to_python\ch-5\Questions\practice.txt") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("Found")
    else:
        print("not found")