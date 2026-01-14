# Create a class BankAccount. [encapsulation]
# __init__: Starts with balance = 0.
# Method deposit(amount): Adds amount to balance.
# Method withdraw(amount): Subtracts amount only if sufficient funds exist. If not, print "Insufficient Funds".

class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(self.balance)

    def withdraw(self, amount):
        if (amount <= self.balance):
            self.balance -= amount
            print(self.balance)
        else:
            print('Insufficient Funds!')


x = BankAccount(0)
x.deposit(500)
x.withdraw(600)
