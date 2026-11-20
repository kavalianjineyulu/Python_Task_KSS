# Base class
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed


# Derived class Car
class Car(Vehicle):
    def display_details(self):
        print("Car Brand:", self.brand)
        print("Car Speed:", self.speed, "km/h")


# Derived class Bike
class Bike(Vehicle):
    def display_details(self):
        print("Bike Brand:", self.brand)
        print("Bike Speed:", self.speed, "km/h")


# Creating objects
car1 = Car("Toyota", 180)
bike1 = Bike("Honda", 120)

# Displaying details
print("Car Details:")
car1.display_details()

print("\nBike Details:")
bike1.display_details()
