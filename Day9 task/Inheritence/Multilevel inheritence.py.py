# Base class
class Product:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price


# Derived class
class ElectronicProduct(Product):
    def __init__(self, product_name, price, brand):
        super().__init__(product_name, price)
        self.brand = brand


# Derived class
class MobilePhone(ElectronicProduct):
    def __init__(self, product_name, price, brand, storage):
        super().__init__(product_name, price, brand)
        self.storage = storage

    def display_details(self):
        print("Product Name:", self.product_name)
        print("Price:", self.price)
        print("Brand:", self.brand)
        print("Storage:", self.storage)


# Creating object
m1 = MobilePhone("Smartphone", 25000, "Samsung", "128GB")

# Displaying details
m1.display_details()
