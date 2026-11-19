
# Parent class
class Payment:

    def process_payment(self, amount):
        print("Processing payment...")


# Child class 1
class CreditCard(Payment):

    def process_payment(self, amount):
        print("Credit Card Payment")
        print("Amount:", amount)
        print("Payment successful using Credit Card")


# Child class 2
class UPI(Payment):

    def process_payment(self, amount):
        print("UPI Payment")
        print("Amount:", amount)
        print("Payment successful using UPI")


# Child class 3
class NetBanking(Payment):

    def process_payment(self, amount):
        print("Net Banking Payment")
        print("Amount:", amount)
        print("Payment successful using Net Banking")


# Creating objects
p1 = CreditCard()
p2 = UPI()
p3 = NetBanking()

# Calling methods
p1.process_payment(5000)

print()

p2.process_payment(2000)

print()

p3.process_payment(3000)
