# Write a function to find in which line of the file does the word "learning" occur first. Print -1 if word not found

def check_for_line():
    word = "Python"
    data = True
    line_no = 1
    with open(r"Introduction_to_python\ch-5\Questions\practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
            
    return -1

check_for_line()