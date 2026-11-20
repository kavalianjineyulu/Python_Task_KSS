
# Decorator function
def add_bonus(func):
    def wrapper(self):
        bonus = 5000
        final_salary = self.salary + bonus

        print("Employee Name:", self.name)
        print("Original Salary:", self.salary)
        print("Bonus Added:", bonus)

        return func(self, final_salary)

    return wrapper


# Employee class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @add_bonus
    def display_salary(self, final_salary):
        print("Final Salary:", final_salary)


# Create object
emp1 = Employee("Ramesh", 30000)

# Display salary with bonus
emp1.display_salary()
