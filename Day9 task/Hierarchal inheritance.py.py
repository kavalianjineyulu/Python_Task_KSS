
# Parent class
class Staff:

    def __init__(self, name, staff_id, salary):
        self.name = name
        self.staff_id = staff_id
        self.salary = salary

    def display_details(self):
        print("Name:", self.name)
        print("Staff ID:", self.staff_id)
        print("Salary:", self.salary)


# Child class 1
class Professor(Staff):

    def __init__(self, name, staff_id, salary, subject):
        super().__init__(name, staff_id, salary)
        self.subject = subject

    def display(self):
        print("\nProfessor Details:")
        self.display_details()
        print("Subject:", self.subject)


# Child class 2
class LabAssistant(Staff):

    def __init__(self, name, staff_id, salary, lab_name):
        super().__init__(name, staff_id, salary)
        self.lab_name = lab_name

    def display(self):
        print("\nLab Assistant Details:")
        self.display_details()
        print("Lab Name:", self.lab_name)


# Child class 3
class Administrator(Staff):

    def __init__(self, name, staff_id, salary, department):
        super().__init__(name, staff_id, salary)
        self.department = department

    def display(self):
        print("\nAdministrator Details:")
        self.display_details()
        print("Department:", self.department)


# Creating objects
p = Professor("Ravi", 101, 50000, "Python")
l = LabAssistant("Kiran", 102, 30000, "Computer Lab")
a = Administrator("Suresh", 103, 40000, "Accounts")

# Display information
p.display()
l.display()
a.display()
