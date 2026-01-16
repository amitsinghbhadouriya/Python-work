# Write a function to print the element of a list in a single line. (list is the parameter)

Countries = ['India', 'US', 'UK', 'Russia', 'Australia', 'South Africa', 'Vietnam']

def print_list(list):
    for item in list:
        print(item, end=" ")
    
print_list(Countries)