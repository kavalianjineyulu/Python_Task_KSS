
class Result:

    def calculate(self, mark1, mark2, mark3=None):

        if mark3 is None:
            total = mark1 + mark2
            average = total / 2

        else:
            total = mark1 + mark2 + mark3
            average = total / 3

        print("Total Marks:", total)
        print("Average Marks:", average)


# Creating object
student = Result()

# Calculate result using two subjects
print("Two Subjects Result:")
student.calculate(80, 90)

print()

# Calculate result using three subjects
print("Three Subjects Result:")
student.calculate(80, 90, 85)
