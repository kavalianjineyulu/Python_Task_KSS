class student:
    def __init__(self, name, roll_number,marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks
    def display_details(self):
        print("student name:",self.name)
        print("roll_number:",self.roll_number)
        print("marks:",self.marks)
        print("-------------")
student1 = student("anji", 100,99)
student2 = student("ashok",99,98)
student3 = student("anil",95,94)
student1.display_details()
student2.display_details()
student3.display_details()
