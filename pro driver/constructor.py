class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def display(self):
        print("Id",self.id)
        print("Name",self.name)

emp1 = Employee(1, "john")
emp2 = Employee(2, "Anu")
emp1.display()