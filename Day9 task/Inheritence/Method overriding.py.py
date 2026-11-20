# Base class
class Payment:
    def process_payment(self):
        print("Processing payment...")


# Derived class 1
class CreditCard(Payment):
    def process_payment(self):
        print("Payment done using Credit Card")


# Derived class 2
class UPI(Payment):
    def process_payment(self):
        print("Payment done using UPI")


# Derived class 3
class NetBanking(Payment):
    def process_payment(self):
        print("Payment done using Net Banking")


# Creating objects
p1 = CreditCard()
p2 = UPI()
p3 = NetBanking()

# Calling methods
p1.process_payment()
p2.process_payment()
p3.process_payment()
