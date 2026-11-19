
# Parent class
class Vehicle:

    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def display_details(self):
        print("Brand:", self.brand)
        print("Speed:", self.speed, "km/h")


# Child class 1
class Car(Vehicle):

    def __init__(self, brand, speed, doors):
        super().__init__(brand, speed)
        self.doors = doors

    def display_details(self):
        print("Car Details:")
        super().display_details()
        print("Number of Doors:", self.doors)


# Child class 2
class Bike(Vehicle):

    def __init__(self, brand, speed, type):
        super().__init__(brand, speed)
        self.type = type

    def display_details(self):
        print("Bike Details:")
        super().display_details()
        print("Bike Type:", self.type)


# Creating objects
car = Car("Toyota", 180, 4)
bike = Bike("Yamaha", 120, "Sports")

# Display details
car.display_details()
print()
bike.display_details()
