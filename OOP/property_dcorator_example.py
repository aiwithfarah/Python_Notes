class BankAccount:

    def __init__(self, balance):
        self.balance = balance


acc = BankAccount(100)
print(acc.balance)  # 100
acc.balance = -500
# -500 #BAD you shouldn;t be able to set negative balance directy
print(acc.balance)

# Solution use property decorator


class BkAccount:

    def __init__(self, balance):
        self.balance = balance

    # 1. Getter (Read Access)
    # this runs when we type print(acc.balance)
    @property
    def balance(self):
        return self._balance

    # 2. Setter(Write Access)
    # this runs when you type 500
    @balance.setter
    def balance(self, value):
        if value < 0:
            print("Error. Balance cannot be Negative")
        else:
            print("Updating the balance....")
            self._balance = value


acc = BkAccount(100)
acc.balance = 200
print(acc.balance)
# Updating the balance....
# 200
