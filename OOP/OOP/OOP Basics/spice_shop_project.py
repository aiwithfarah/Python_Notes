# Create a class Product.
# __init__: Name, Price, Stock Quantity.
# Method sell(quantity):
# Check if you have enough stock.
# If yes, subtract the stock and print "Sold!".
# If no, print "Out of stock!".
# Create a child class DigitalProduct (like an E-book or Recipe PDF).
# Inherit from Product.
# Override sell():
# Digital products never run out of stock.
# It should just print "File sent to email!" without reducing any stock number.

class Product:

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def sell(self, quantity):
        if quantity < self.stock:
            self.stock -= quantity
            print("Sold")
            print(f"Remaining Product Stock : {self.stock}")
        else:
            print("Out of Stock")


class DigitalProduct(Product):

    def __init__(self, name, price):
        # 2. Call the Parent's __init__ using super()
        # We manually pass '0' or infinity as stock so the Parent is happy
        super().__init__(name, price, 0)

    def sell(self, quantity):
        print(f"{self.name} File sent to email!")


product = Product("Malvani", 299, 1000)
product.sell(50)

digitalproduct = DigitalProduct("Recipe", 1000)
digitalproduct.sell(40)
