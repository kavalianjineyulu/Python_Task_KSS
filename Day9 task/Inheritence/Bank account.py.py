class BankAccount:
    # Constructor
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    # Deposit method
    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited:", amount)

    # Withdraw method
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance!")

    # Display balance method
    def display_balance(self):
        print("Account Number:", self.account_number)
        print("Current Balance:", self.balance)


# Creating an object
account = BankAccount(123456, 10000)

# Calling methods
account.deposit(5000)
account.withdraw(2000)
account.display_balance()
