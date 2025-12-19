# Define the Product class with __init__ (name, price, stock).
# Add the __str__ magic method.
# It should return a string like: "Spice: [Name] (Stock: [Stock])".
# Create an object for "Turmeric" with price 100 and stock 50.
# Print the object directly (e.g., print(turmeric)) and verify it shows your nice message instead of the memory address.

class Product:

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"Spice : {self.name}, Stock : {self.stock}"


turmeric = Product("Turmeric", 100, 50)
print(turmeric)  # Spice : Turmeric, Stock : 50
