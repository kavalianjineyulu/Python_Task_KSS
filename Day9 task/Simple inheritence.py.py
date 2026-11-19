class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
class manager(employee):
    def display_details(self):
        print("employee name:",self.name)
        print("employee salary:",self.salary)
m1 = manager("rahul", 50000)
m1.display_details()
