# Base class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


# Derived class
class Manager(Employee):
    def display_details(self):
        print("Employee Name:", self.name)
        print("Employee Salary:", self.salary)


# Creating an object
m1 = Manager("Rahul", 50000)

# Calling the method
m1.display_details()
