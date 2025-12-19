# With the __add__ magic method, you can define exactly what the + symbol does for your objects.
#  This is called Operator Overloading.
# When you write a + b, Python secretly converts it to: a.__add__(b)
# self is the item on the left of the +.
# other is the item on the right of the +.

# Let's say we want + to calculate the total price of two items combined.


class Spice:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __add__(self, other):
        # We add the price of THIS object (self) to the price of the OTHER object
        return self.price + other.price


p1 = Spice("Salt", 10)
p2 = Spice("Pepper", 20)

total = p1+p2
print(total)  # 30
