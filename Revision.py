# 1 - Write a program to get two integer and a float from user and find the smallest number
# 2 - Write a program to get two float from user and find the largest number
# 3 - Write a program to print the even numbers between 10 and 20
# 4 - Write a program to print the odd numbers 15 and 25
# 5 - Write a program to get a character from user
# 6 - Write a program to get a string from user
# 7 - Write a program to get three float from user and find the smallest number.
# 8 - Ask the user for the number of months, days, hours, minutes, and seconds they spent on an activity (like playing or studying). Calculate the total time in seconds.
# 9 - Write a program to calculate the total cost of movie tickets. Ask the user how many adults and children are going, then multiply by the ticket prices (e.g., $10 for adults, $7 for children).
# 10 - Savings Tracker
# Ask the user to input the amount of money saved daily for 10 days.
#
# -> Calculate the total savings and average savings per day.
# -> Display results based on the average:
#   Average ≥ $20: "Excellent Saver!"
#   Average ≥ $10 and < $20: "Good Savings Habits!"
#   Average < $10: "Save More Consistently!"
# 11 -add a data into set
# 12 - Remove  a data from set
# 13 - Join 2 set using union function
# 14 - Print the common data in two sets
# 15 - Access an item in dictionary
# 16 - Add an item into dictionary
# 17 - Delete an item from dictionary
# 18 - Change an item from dictionary
# 19 - Looping through dictionary
# 20 - Copy the dictionary
# 21 - Write a program to add a data into the tuple
# 22 - Write a program to remove the mango from tuple
# 23 - Write a program to remove the 3rd index data from tuple
# 24 - Write a program to find the sum of even numbers between a range
# 25 - Write a program to create a oops for the following details :
#       -> Classes - 6
#       ->  3 attributes for each class
#        ->  4 object for each class
# 26 - Write a program to show an example for single, multiple and multi - level inheritance
# 27 - Write a program to show an example for polymorphism and encapsulation

#Question1
# a = int(input("Enter the first integer: "))
# b = int(input("Enter the second integer: "))
# c = float(input("Enter a float: "))
#
# if a < b and a < c:
#     print("a is the smallest")
# elif b < c and b < a:
#     print("b is the smallest")
# else:
#     print("c is the smallest")


#Question2
# a = float(input("Enter a float"))
# b = float(input("Enter another float"))
#
# if a > b:
#     print("a is the largest")
# else:
#     print("b is the largest")



#Question3
# for i in range(10, 21):
#     if i % 2 == 0:
#         print(i)
# #
#
#
##Question4
# for i in range(15, 26):
#     if i % 2 != 0:
#         print(i)
#

#
##Question5
# ch = input("Enter a character: ")
# print("Character entered:", ch)


#
##Question6
# text = input("Enter a string: ")
# print("String entered:", text)
#
#
##Question7
# a = float(input("Enter the first float: "))
# b = float(input("Enter the second integer: "))
# c = float(input("Enter a float: "))
#
# if a < b and a < c:
#     print("a is the smallest")
# elif b < c and b < a:
#     print("b is the smallest")
# else:
#     print("c is the smallest")
#
##Question8

# months = int(input("Months: ")) * 30 * 24 * 60 * 60
# days = int(input("Days: ")) * 24 * 60 * 60
# hours = int(input("Hours: ")) * 60 * 60
# minutes = int(input("Minutes: ")) * 60
# seconds = int(input("Seconds: "))
#
# total = months + days + hours + minutes + seconds
# print("Total seconds:", total)

# Question9
# adults = int(input("Adults: "))
# children = int(input("Children: "))
#
# total = adults * 10 + children * 7
# print("Total cost: $", total)
#

# Question10
# total = 0
# for i in range(10):
#     amount = float(input("Day " + str(i+1) + " savings: "))
#     total += amount
#
# average = total / 10
# print("Total saved:", total)
# print("Average per day:", average)
#
# if average >= 20:
#     print("Excellent Saver!")
# elif average >= 10:
#     print("Good Savings Habits!")
# else:
#     print("Save More Consistently!")


#Question11
# my_set = set()
# my_set.add("apple")
# print(my_set)


#Question12
# my_set = {"apple", "banana"}
# my_set.remove("banana")
# print(my_set)


#Question13
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# union_set = set1.union(set2)
# print("Union of sets:", union_set)
#
# #Question14
# common_elements = set1.intersection(set2)
# print("Common elements:", common_elements)

# #Question15
# my_dict = {"name": "Alice", "age": 25}
# print("Access 'name':", my_dict["name"])
#
# #Question16
# my_dict["city"] = "New York"
# print("After adding 'city':", my_dict)
#
# #Question17
# print("After deleting 'age':", my_dict)
#
# #Question18
# my_dict["name"] = "Bob"
# print("After changing 'name':", my_dict)
#
# #Question19
# print("Looping through dictionary:")
# for key, value in my_dict.items():
#     print(key, ":", value)
#Question 20
# print("20 - Copy the Dictionary")
# original_dict = {'a': 1, 'b': 2, 'c': 3}
# copied_dict = original_dict.copy()
# print("Copied Dictionary:", copied_dict)
# print("-" * 50)
#
# #Question21
# print("21 - Add Data into the Tuple")
# original_tuple = (1, 2, 3)
# new_data = (4,)  # Adding element 4
# updated_tuple = original_tuple + new_data
# print("Updated Tuple:", updated_tuple)
# print("-" * 50)
#
# Question22
# print("22 - Remove 'mango' from the Tuple")
# fruits = ("apple", "banana", "mango", "orange")
# fruits_list = list(fruits)
# fruits_list.remove("mango")
# updated_fruits = tuple(fruits_list)
# print("Tuple after removing 'mango':", updated_fruits)
# print("-" * 50)
#
#Question23
# print("23 - Remove the 3rd Index Data from the Tuple")
# data = (10, 20, 30, 40, 50)
# data_list = list(data)
# del data_list[3]

#Question24
# start = 1
# end = 20
# even_sum = sum(i for i in range(start, end + 1) if i % 2 == 0)
# print("Sum of even numbers:", even_sum)



#Question25
# class Car:
#     def __init__(self, model, color, year):
#         self.model = model
#         self.color = color
#         self.year = year
#
# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
# class Student:
#     def __init__(self, name, student_id, major):
#         self.name = name
#         self.student_id = student_id
#         self.major = major
#
# class Animal:
#     def __init__(self, species, breed, age):
#         self.species = species
#         self.breed = breed
#         self.age = age
#
# class Employee:
#     def __init__(self, name, employee_id, department):
#         self.name = name
#         self.employee_id = employee_id
#         self.department = department
#
# class Shape:
#     def __init__(self, type, color, area):
#         self.type = type
#         self.color = color
#         self.area = area
#
# # Creating 4 objects for each class
# car1 = Car("Sedan", "Red", 2020)
# car2 = Car("SUV", "Blue", 2022)
# car3 = Car("Hatchback", "Black", 2021)
# car4 = Car("Truck", "White", 2023)
#
# book1 = Book("The Lord of the Rings", "J.R.R. Tolkien", 1200)
# book2 = Book("Pride and Prejudice", "Jane Austen", 400)
# book3 = Book("1984", "George Orwell", 300)
# book4 = Book("To Kill a Mockingbird", "Harper Lee", 300)
#
# student1 = Student("Alice", 12345, "Computer Science")
# student2 = Student("Bob", 67890, "Physics")
# student3 = Student("Charlie", 13579, "Mathematics")
# student4 = Student("Diana", 24680, "Chemistry")
#
# animal1 = Animal("Dog", "Labrador", 3)
# animal2 = Animal("Cat", "Siamese", 5)
# animal3 = Animal("Bird", "Parrot", 2)
# animal4 = Animal("Fish", "Goldfish", 1)
#
# employee1 = Employee("John Doe", 54321, "IT")
# employee2 = Employee("Jane Smith", 98765, "HR")
# employee3 = Employee("Peter Jones", 11223, "Finance")
# employee4 = Employee("Mary Brown", 44556, "Marketing")
#
# shape1 = Shape("Circle", "Green", 25)
# shape2 = Shape("Square", "Yellow", 16)
# shape3 = Shape("Triangle", "Blue", 10)
# shape4 = Shape("Rectangle", "Red", 20)
#
# # You can access the attributes of each object like this:
# print(car1.model)
# print(book2.author)
# print(student3.major)
# print(animal4.age)
# print(employee1.department)
# print(shape2.color)
#
#
#
# Question26
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print("Generic animal sound")
#
# class Dog(Animal):
#     def speak(self):
#         print("Woof!")
#
# Multiple Inheritance
# class Swimmer:
#     def swim(self):
#         print("Swimming")
#
# class Flyer:
#     def fly(self):
#         print("Flying")
#
# class FlyingFish(Swimmer, Flyer):
#     pass
#
# # Multi-level Inheritance
# class Vehicle:
#     def start(self):
#         print("Vehicle started")
#
# class Car(Vehicle):
#     def drive(self):
#         print("Car driving")
#
# class ElectricCar(Car):
#     def charge(self):
#         print("Car charging")
#
# # Example Usage
# if __name__ == "__main__":
#     # Single Inheritance
#     dog = Dog("Buddy")
#     dog.speak()
#
#     # Multiple Inheritance
#     flying_fish = FlyingFish()
#     flying_fish.swim()
#     flying_fish.fly()
#
#     # Multi-level Inheritance
#     electric_car = ElectricCar()
#     electric_car.start()
#     electric_car.drive()
#     electric_car.charge()
#Question27
# #class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance  # Private attribute
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#
#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Insufficient balance or invalid amount.")
#
#     def get_balance(self):
#         return self.__balance
#
# # Example usage
# account = BankAccount(1000)
# account.deposit(500)
# account.withdraw(200)
# print("Current balance:", account.get_balance())


# Question27
#
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         pass
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
#         return "Tweet!"
#
# def animal_sound(animal):
#     print(f"{animal.name} says {animal.speak()}")
#
# dog = Dog("Buddy")
# cat = Cat("Whiskers")
# bird = Bird("Tweety")
#
# animal_sound(dog)
# animal_sound(cat)
# animal_sound(bird)

#Question28
# class Person:
#     def greet(self):
#         return "Hello from Person"
#
# class Employee(Person):
#     def greet(self):
#         return "Hello from Employee"
#
# class Manager(Employee):
#     def greet(self):
#         return "Hello from Manager"
#
#
# p = Person()
# e = Employee()
# m = Manager()
#
# print(p.greet())  # Output: Hello from Person
# print(e.greet())  # Output: Hello from Employee
# print(m.greet())  # Output: Hello from Manager

#Question 29
# class EducationInstitution:
#     def info(self):
#         return "This is an educational institution"
#
# class School(EducationInstitution):
#     def info(self):
#         return "This is a school"
# class HighSchool(School):
#     def info(self):
#         return "This is a high school"
# hs = HighSchool()
# print(hs.info())



#Question30
# class Appliance:
#     def operate(self):
#         return "Appliance is operating"
#
# class WashingMachine(Appliance):
#     def operate(self):
#         return "Washing Machine is running"
#
# class SmartWasher(WashingMachine):
#     def operate(self):
#         return "Smart Washer runs with AI control"
# sw = SmartWasher()
# print(sw.operate())

#
#
#
