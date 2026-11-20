# Base class
class Staff:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


# Derived class 1
class Professor(Staff):
    def display_details(self):
        print("Professor Name:", self.name)
        print("Salary:", self.salary)


# Derived class 2
class LabAssistant(Staff):
    def display_details(self):
        print("Lab Assistant Name:", self.name)
        print("Salary:", self.salary)


# Derived class 3
class Administrator(Staff):
    def display_details(self):
        print("Administrator Name:", self.name)
        print("Salary:", self.salary)


# Creating objects
p1 = Professor("Rahul", 60000)
l1 = LabAssistant("Sita", 30000)
a1 = Administrator("Arun", 45000)

# Displaying details
print("Professor Details:")
p1.display_details()

print("\nLab Assistant Details:")
l1.display_details()

print("\nAdministrator Details:")
a1.display_details()
