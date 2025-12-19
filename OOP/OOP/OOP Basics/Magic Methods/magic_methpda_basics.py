# called Magic/dunder methoda cause they happen automatically in the backgroun
# You can't call them directly. Python calls them for you

# If you try to print an object python shows you the memory addess
# use __str__ method tell pyton if someone tries printing the object show them this

class Product:

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        # must return a string not print it
        return f"Product: {self.name} : {self.price}"


p = Product("Malvani", 299, 1000)
print(p)  # <__main__.Product object at 0x000001C138EB6A50>  ---> Without __str__
print(p)  # Product: Malvani : 299
