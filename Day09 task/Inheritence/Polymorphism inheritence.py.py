import math

# Circle class
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Area of Circle:", math.pi * self.radius * self.radius)


# Rectangle class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area of Rectangle:", self.length * self.width)


# Triangle class
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        print("Area of Triangle:", 0.5 * self.base * self.height)


# Creating objects
c1 = Circle(5)
r1 = Rectangle(10, 5)
t1 = Triangle(8, 6)

# Demonstrating polymorphism
for shape in (c1, r1, t1):
    shape.area()
