
# Read employee data from file
file = open("employees.txt", "r")

employees = []

for line in file:
    name, salary = line.split()
    salary = int(salary)
    employees.append((name, salary))

file.close()

# Display employee details
print("Employee Details:")

for name, salary in employees:
    print(name, salary)

# Find highest salary employee
highest = max(employees, key=lambda x: x[1])

print("\nHighest Salary Employee:")
print("Name:", highest[0])
print("Salary:", highest[1])

# Append new employee record
file = open("employees.txt", "a")

name = input("\nEnter new employee name: ")
salary = int(input("Enter new employee salary: "))

file.write(name + " " + str(salary) + "\n")

file.close()

print("New employee added successfully!")
