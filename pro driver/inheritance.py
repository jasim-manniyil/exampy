class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name} from the Parent class.")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Initialize the parent class's name attribute
        self.age = age

    def greet(self):
        print(f"Hello, I am {self.name}, {self.age} years old, from the Child class.")

# Create an instance of the Parent class
parent_instance = Parent("Alice")
parent_instance.greet()  # Output: Hello, I am Alice from the Parent class.

# Create an instance of the Child class
child_instance = Child("Bob", 10)
child_instance.greet()  # Output: Hello, I am Bob, 10 years old, from the Child class.
