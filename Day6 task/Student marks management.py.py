# Student Marks Management System

# Tuple: Store three subject names
subjects = ("Python", "Java", "SQL")

# Set: Store unique student names
student_names = set()

# Dictionary: Store student names and marks
students = {}


# Function 1: Add student
def add_student():
    try:
        name = input("Enter student name: ")

        if name in student_names:
            print("Student already exists!")
            return

        marks = []

        for subject in subjects:
            mark = float(input("Enter marks in " + subject + ": "))
            marks.append(mark)

        students[name] = marks
        student_names.add(name)

        print("Student added successfully!")

    except ValueError:
        print("Error: Enter numbers only.")

    except TypeError:
        print("Error: Incorrect data type.")


# Function 2: Recursive function to calculate total
def calculate_total(marks):

    if len(marks) == 0:
        return 0

    return marks[0] + calculate_total(marks[1:])


# Function 3: Display all student records
def display_students():

    if len(students) == 0:
        print("No student records found.")
        return

    for name, marks in students.items():

        print("\nStudent Name:", name)

        for i in range(len(subjects)):
            print(subjects[i], ":", marks[i])

        print("Total Marks:", calculate_total(marks))


# Function 4: Calculate average marks
def calculate_average():

    try:
        name = input("Enter student name: ")

        if name not in students:
            raise NameError("Student name does not exist!")

        marks = students[name]

        if not isinstance(marks, list):
            raise TypeError("Marks must be a list.")

        total = calculate_total(marks)

        average = total / len(marks)

        print("Student Name:", name)
        print("Total Marks:", total)
        print("Average Marks:", average)

    except NameError as e:
        print("Error:", e)

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    except TypeError as e:
        print("Error:", e)


# Main menu
while True:

    print("\n===== STUDENT MARKS MANAGEMENT =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Calculate Average Marks")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_student()

        elif choice == 2:
            display_students()

        elif choice == 3:
            calculate_average()

        elif choice == 4:
            print("Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")

    except ValueError:
        print("Please enter a valid menu number.")
