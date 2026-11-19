
# Parent class
class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_product(self):
        print("Product Name:", self.name)
        print("Product Price:", self.price)


# Child class 1
class ElectronicProduct(Product):

    def __init__(self, name, price, brand):
        super().__init__(name, price)
        self.brand = brand

    def display_electronic(self):
        self.display_product()
        print("Brand:", self.brand)


# Child class 2
class MobilePhone(ElectronicProduct):

    def __init__(self, name, price, brand, storage):
        super().__init__(name, price, brand)
        self.storage = storage

    def display_mobile(self):
        self.display_electronic()
        print("Storage:", self.storage)


# Creating object
mobile = MobilePhone("Smartphone", 25000, "Samsung", "128GB")

# Display details
print("Mobile Phone Details:")
mobile.display_mobile()
