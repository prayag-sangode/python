# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some generic sound"

# Child class Dog (inherits from Animal)
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Child class Cat (inherits from Animal)
class Cat(Animal):
    def speak(self):
        return "Meow!"

# Polymorphism in action
animals = [Dog("Buddy"), Cat("Kitty"), Animal("Generic")]

for animal in animals:
    print(f"{animal.name} says: {animal.speak()}")
