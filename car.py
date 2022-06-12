""" Car class """
class Car:
    """
        A simple attempt to represent a car.
    """
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """ Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def increment_odometer(self, mileage):
        """ Set the odometer reading to the given value
            Don't allow rolling back the odometer
        """
        if mileage < 0:
            print("You are not allowed to roll back the odometer:",mileage)
            return
        self.odometer_reading += mileage

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer_reading = 14
my_new_car.read_odometer()
my_new_car.increment_odometer(10)
my_new_car.read_odometer()
my_new_car.increment_odometer(-10)
my_new_car.read_odometer()

class ElectricCar(Car):
    """ Represent aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """ print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kwh battery.")

my_tesla = ElectricCar('tesla', 'model S', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
