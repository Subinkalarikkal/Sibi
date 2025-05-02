# class Animal:
#     def speak(self):
#         raise NotImplementedError("Subclass must implement abstract method")
#
# class Dog(Animal):
#     def speak(self):
#         return "Woof!"
#
# class Cat(Animal):
#     def speak(self):
#         return "Meow!"
#
# class Bird(Animal):
#     def speak(self):
#         return "Chirp!"
#
# def animal_speak(animal: Animal):
#     print(animal.speak())
#
# animals = [Dog(), Cat(), Bird()]
#
# for a in animals:
#     animal_speak(a)





# class Car:
#     def drive(self):
#         return "The car drives."
#
# class SportsCar(Car):
#     def drive(self):
#         return "The sports car zooms down the highway!"
#
# class ElectricCar(Car):
#     def drive(self):
#         return "The electric car glides silently."
#
# class Truck(Car):
#     def drive(self):
#         return "The truck rumbles down the road with a heavy load."
#
# def test_drive(vehicle: Car):
#     print(vehicle.drive())
#
#
# vehicles = [SportsCar(), ElectricCar(), Truck()]
#
#
# for v in vehicles:
#     test_drive(v)





class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def make_animal_speak(animal):
    print(animal.speak())

make_animal_speak(Dog())
make_animal_speak(Cat())
