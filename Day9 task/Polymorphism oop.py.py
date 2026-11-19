
import math

# Circle class
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


# Rectangle class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Triangle class
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# Creating objects
c = Circle(5)
r = Rectangle(10, 5)
t = Triangle(8, 6)

# Polymorphism
for shape in (c, r, t):
    print("Area:", round(shape.area(), 2))
