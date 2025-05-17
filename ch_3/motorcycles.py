motorcycles = ['honda', 'yahama', 'suzuki']
print(motorcycles)


# motorcycles[0] = 'ducati'
# print(motorcycles)

# .append method
motorcycles.append('ducati')
print(motorcycles)



motorcycles = []
motorcycles.append('honda')
motorcycles.append('ducati')
motorcycles.append('yahama')
print(motorcycles)



# .insert method
motorcycles = ['honda', 'yahama', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)


# del method
motorcycles = ['honda', 'yahama', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)
del motorcycles[1]
print(motorcycles)



# pop method 
motorcycles = ['honda', 'yahama', 'suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)



motorcycles = ['honda', 'yahama', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")


motorcycles = ['honda', 'yahama', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}")





# remove method 
motorcycles = ['honda', 'yahama', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)




motorcycles = ['honda', 'yahama', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")


# motorcycle = ['honda', 'yahama', 'suzuki']
# print(motorcycles[3])

motorcycle = ['honda', 'yahama', 'suzuki']
print(motorcycles[-1])


# motorcycles = []
# print(motorcycles[-1])
