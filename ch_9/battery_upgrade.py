class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")

class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        else:
            range = 0
        print(f"This car can go approximately {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size != 65:
            print("Upgrading the battery to 65 kWh.")
            self.battery_size = 65
        else:
            print("The battery is already upgraded to 65 kWh.")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

# Create an electric car with the default battery size (75 kWh)
my_electric_car = ElectricCar("Tesla", "Model S", 2023)

# Get the range of the car before upgrading the battery
print("Before upgrading the battery:")
my_electric_car.battery.get_range()

# Upgrade the battery to 65 kWh
my_electric_car.battery.upgrade_battery()

# Get the range of the car after upgrading the battery
print("\nAfter upgrading the battery:")
my_electric_car.battery.get_range()   
