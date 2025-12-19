# Define the Product class with __init__ (name, price).
# Add the __add__ method.
# It should return the sum of self.price and other.price.
# Create an object spice1 ("Clove", 300).
# Create an object spice2 ("Cardamom", 900).
# Create a variable total_bill = spice1 + spice2.
# Print total_bill.

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __add__(self, other):
        return self.price + other.price


spice1 = Product("Clove", 300)
spice2 = Product("Cardamom", 900)
total_bill = spice1 + spice2
print(total_bill)
