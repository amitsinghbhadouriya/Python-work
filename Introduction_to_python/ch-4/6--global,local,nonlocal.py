x = 10   # global variable

def show():
    x = 10   # local variable
    print(x)

show()
print(x)



def outer():
    x = 10   # nonlocal variable

    def inner():
        nonlocal x
        x = x + 5
        print("Inner:", x)

    inner()
    print("Outer:", x)

outer()