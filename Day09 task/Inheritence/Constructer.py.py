class Rectangle:
    # Constructor
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Method to calculate and display area
    def calculate_area(self):
        area = self.length * self.width
        print("Area of Rectangle:", area)


# Creating an object
r1 = Rectangle(10, 5)

# Calling the method
r1.calculate_area()
