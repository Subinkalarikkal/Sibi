class Car:
    def drive(self):
        return "The car drives."

class SportsCar(Car):
    def drive(self):
        return "The sports car zooms down the highway!"

class ElectricCar(Car):
    def drive(self):
        return "The electric car glides silently."

class Truck(Car):
    def drive(self):
        return "The truck rumbles down the road with a heavy load."

def test_drive(vehicle: Car):
    print(vehicle.drive())

# List of different types of cars
vehicles = [SportsCar(), ElectricCar(), Truck()]

# Polymorphic behavior in action
for v in vehicles:
    test_drive(v)
