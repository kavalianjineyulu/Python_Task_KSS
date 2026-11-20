class Result:

    def calculate_result(self, sub1, sub2, sub3=None):

        if sub3 is None:
            total = sub1 + sub2
            print("Total Marks (2 Subjects):", total)
            print("Average:", total / 2)

        else:
            total = sub1 + sub2 + sub3
            print("Total Marks (3 Subjects):", total)
            print("Average:", total / 3)


# Creating object
r1 = Result()

# Calculating result using 2 subjects
r1.calculate_result(80, 90)

# Calculating result using 3 subjects
r1.calculate_result(80, 90, 85)
