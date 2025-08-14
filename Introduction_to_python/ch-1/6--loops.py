# For loop

a = int(input("Enter a number: "))
for i in range(0, a):
    print(i)
    
    
# While Loop
n = int(input("Enter the number: "))
while(n < 5):
    n = n + 1
    print("Hello World")
    
# Break
i = 1
while(i <= 8):
    print(i)
    if(i==4):
        break
    i += 1
    
print("loop is ended.")

# Continue
i = 1
while(i <= 8):
    if(i==4):
        i += 1
        continue
    print(i)
    i += 1
    
print("loop is ended.")