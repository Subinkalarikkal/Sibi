class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Bird(Animal):
    def speak(self):
        return "Chirp!"

def animal_speak(animal: Animal):
    print(animal.speak())

animals = [Dog(), Cat(), Bird()]

for a in animals:
    animal_speak(a)