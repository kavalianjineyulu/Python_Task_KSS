# Open file in read mode
file = open("employees.txt", "r")

employees = []

print("Employee Details:")
print("----------------------")

# Read employee data
for line in file:
    name, salary = line.split()
    salary = int(salary)

    employees.append((name, salary))

    print("Name:", name, "Salary:", salary)

file.close()

# Find employee with highest salary
if employees:
    highest = max(employees, key=lambda x: x[1])

    print("----------------------")
    print("Highest Salary Employee:")
    print("Name:", highest[0])
    print("Salary:", highest[1])
else:
    print("No employee records found.")

# Add new employee
print("\nEnter New Employee Details:")
new_name = input("Enter employee name: ")
new_salary = int(input("Enter employee salary: "))

# Append employee details to file
file = open("employees.txt", "a")
file.write(new_name + " " + str(new_salary) + "\n")
file.close()

print("New employee added successfully!")
