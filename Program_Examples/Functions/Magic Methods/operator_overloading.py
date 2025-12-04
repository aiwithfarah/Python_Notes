# You can teach Python how to use the + symbol on your custom objects!

class Wallet:

    def __init__(self, money):
        self.money = money

    # Teach python what the + symbol means for wallet
    def __add__(self, other):
        # return a new wallet with combned money
        return Wallet(self.money + other.money)

    def __str__(self):
        return f"{self.money}"


w1 = Wallet(50)
w2 = Wallet(100)

w3 = w1 + w2  # python calls w1.__add__w2 automatically
print(w3)  # 150
