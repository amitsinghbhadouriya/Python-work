my_foods = ['pizza', 'falafel', 'carrot cake']

# This does't work:
friend_foods = my_foods
3
# friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are")
print(friend_foods)