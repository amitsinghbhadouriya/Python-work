# Search for a number x in this tuple using loop.
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 25
i = 0

while i < len(nums):
    if(nums[i] == x):
        print("Element found at index: ", i)
        
    i = i + 1