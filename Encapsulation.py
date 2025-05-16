class Student:
    def __init__(self, name, age, grade):
        print(name, age, grade)


class Teacher:
    def __init__(self, name, subject, years):
        print(name, subject, years)


class Book:
    def __init__(self, title, author, pages):
        print(title, author, pages)


class Car:
    def __init__(self, brand, model, year):
        print(brand, model, year)


class Animal:
    def __init__(self, type, color, sound):
        print(type, color, sound)


class Building:
    def __init__(self, name, floors, city):
        print(name, floors, city)


# Create 4 objects for each
Student("Ali", 12, "6th")
Student("Sara", 13, "7th")
Student("John", 11, "5th")
Student("Emma", 14, "8th")

Teacher("Khan", "Math", 5)
Teacher("Ayesha", "English", 3)
Teacher("Lee", "Science", 4)
Teacher("Ana", "History", 6)

Book("Book A", "Author 1", 100)
Book("Book B", "Author 2", 200)
Book("Book C", "Author 3", 150)
Book("Book D", "Author 4", 120)

Car("Toyota", "Corolla", 2020)
Car("Honda", "Civic", 2021)
Car("Ford", "Focus", 2019)
Car("BMW", "X3", 2022)

Animal("Cat", "White", "Meow")
Animal("Dog", "Brown", "Bark")
Animal("Cow", "Black", "Moo")
Animal("Bird", "Green", "Tweet")

Building("Tower A", 10, "Lahore")
Building("Tower B", 15, "Karachi")
Building("Plaza X", 8, "Islamabad")
Building("Mall Y", 12, "Multan")



class Parent:
    def show(self): print("Parent")
class Child(Parent): pass
Child().show()

# Multiple Inheritance
class A:
    def showA(self): print("A")
class B:
    def showB(self): print("B")
class C(A, B): pass
C().showA(); C().showB()

# Multilevel Inheritance
class Grandparent:
    def showGP(self): print("Grandparent")
class Parent(Grandparent): pass
class Child(Parent): pass
Child().showGP()


# Encapsulation
class Car:
  def __init__(self, brand, model):
    self.__brand = brand
    self.__model = model

  def get_brand(self): return self.__brand

  def show(self): print(self.__brand, self.__model)


# Polymorphism: Method Overriding
class ElectricCar(Car):
  def show(self): print(self.get_brand(), "Electric")


class GasCar(Car):
  def show(self): print(self.get_brand(), "Gas")


# Create objects
car = Car("Toyota", "Corolla")
car.show()

electric_car = ElectricCar("Tesla", "Model S")
electric_car.show()

gas_car = GasCar("Ford", "Mustang")
gas_car.show()



