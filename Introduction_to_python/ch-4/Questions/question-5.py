# Write a recursive function to calculate the sum of first n natural numbers.

num = int(input("Enter a number: "))
def cal_sum(n):
    if(n==0):
        return 0
    return cal_sum(n-1) + n
    
sum = cal_sum(num)
print(sum)