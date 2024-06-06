from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

# Create instances of the subclasses
dog = Dog()
cat = Cat()

# Call the make_sound method
print(dog.make_sound())  # Output: Woof
print(cat.make_sound())  # Output: Meow

# Attempting to instantiate the abstract class will result in an error
try:
    animal = Animal()
except TypeError as e:
    print(e)  # Output: Can't instantiate abstract class Animal with abstract method make_sound
