
class BankAccount:

    # Constructor
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    # Deposit method
    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited successfully")

    # Withdraw method
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully")
        else:
            print("Insufficient balance")

    # Display balance method
    def display_balance(self):
        print("Account Number:", self.account_number)
        print("Available Balance:", self.balance)


# Creating object
account = BankAccount(12345, 5000)

# Calling methods
account.deposit(2000)
account.withdraw(1000)
account.display_balance()
