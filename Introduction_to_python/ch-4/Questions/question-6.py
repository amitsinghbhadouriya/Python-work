# Write a recursive function to print all elements in a list.(use list and index as a parameters)

def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)
    
countries = ['india', 'UK', 'US', 'Australia', 'South Africa', 'Vietnam']
print_list(countries)