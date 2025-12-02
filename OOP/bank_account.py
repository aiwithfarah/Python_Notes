class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print("Deposit Accepted")
        print(f"New Balance: {self.balance}")

    def withdraw(self, withdrawal_amount):
        if self.balance >= withdrawal_amount:
            self.balance -= withdrawal_amount
            print("Withdrawal Accepted")
            print(f"New Balance: {self.balance}")
        else:
            print("Insufficient Funds Available!")


acc1 = BankAccount('Jose', 1000)
print(f"Account Owner : {acc1.owner}")
print(f"Account Balance: {acc1.balance}")
acc1.deposit(175)
acc1.withdraw(245)
acc1.withdraw(399)
acc1.withdraw(1000)
