class Animal:
    def make_sound(self):
        return "Some generic animal sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

# Creating instances of different animals
generic_animal = Animal()
dog = Dog()
cat = Cat()

# Calling the make_sound method on each instance
print(generic_animal.make_sound())  # Output: Some generic animal sound
print(dog.make_sound())             # Output: Woof
print(cat.make_sound())             # Output: Meow
