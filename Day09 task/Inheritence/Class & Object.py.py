
class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Marks:", self.marks)
        print("-------------------")


# Creating three student objects
s1 = Student("Ramesh", 101, 85)
s2 = Student("Sita", 102, 90)
s3 = Student("Arun", 103, 78)

# Displaying student details
s1.display()
s2.display()
s3.display()
