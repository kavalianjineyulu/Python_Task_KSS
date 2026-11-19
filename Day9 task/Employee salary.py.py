
def bonus_decorator(func):
    def wrapper(self):
        salary = func(self)
        bonus = 5000
        total_salary = salary + bonus
        print("Original Salary:", salary)
        print("Bonus:", bonus)
        print("Total Salary:", total_salary)
    return wrapper


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @bonus_decorator
    def display_salary(self):
        return self.salary


emp = Employee("Rahul", 30000)
print("Employee Name:", emp.name)
emp.display_salary()
