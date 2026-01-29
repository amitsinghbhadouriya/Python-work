from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):
    
    @abstractmethod
    def start_engine(self):
        pass  # No implementation, just declaration
    
    def stop_engine(self):
        print("Engine stopped")  # Regular method

# Subclass
class Car(Vehicle):
    
    def start_engine(self):
        print("Car engine started")

class Bike(Vehicle):
    
    def start_engine(self):
        print("Bike engine started")

# Using the classes
my_car = Car()
my_car.start_engine()  # Output: Car engine started
my_car.stop_engine()   # Output: Engine stopped

my_bike = Bike()
my_bike.start_engine()  # Output: Bike engine started
