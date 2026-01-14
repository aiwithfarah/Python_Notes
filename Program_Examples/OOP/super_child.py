# Challenge 8: The Super Child (Inheritance)
# Create a parent class Vehicle with __init__ taking brand.
# Create a child class Car that inherits from Vehicle.
# In Car, override __init__ to take brand AND model.
# Must Use: super().__init__(brand) inside the child.

class Vehicle:

    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):

    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model


x = Car("Mercedes", "Benz")
print(x.brand)
print(x.model)
