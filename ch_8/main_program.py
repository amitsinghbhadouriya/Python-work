# main_program.py

# Import approaches
import my_functions
from my_functions import make_car
from my_functions import make_car as mc
import my_functions as mf
from my_functions import *

# Using the imported function
car1 = my_functions.make_car('subaru', 'outback', color='blue', tow_package=True)
print(car1)

car2 = make_car('toyota', 'camry', color='red', sunroof=True)
print(car2)

car3 = mc('ford', 'mustang', color='black')
print(car3)

car4 = mf.make_car('honda', 'accord', color='silver', navigation=True)
print(car4)

car5 = make_car('chevrolet', 'cruze', color='gray', alloy_wheels=True)
print(car5)
