# Goal: Create a class CoffeeMachine.

# Attributes: water_level (starts at 100), beans (starts at 100).

# Methods:

# make_coffee(): Checks if there is enough water (needs 50) and beans (needs 20).

# If yes: Subtracts the amounts and prints "Enjoy your coffee!".

# If no: Prints "Refill needed!".

# Test: Make coffee twice. Try to make it a third time (should fail).

class CoffeeMachine:

    def __init__(self, water_level, beans):
        self.water_level = water_level
        self.beans = beans

    def make_coffee(self):

        if self.water_level >= 50 and self.beans >= 20:
            self.water_level -= 50
            self.beans -= 20
            print("Enjoy your coffee")
        else:
            print("Refill Needed")


coffee1 = CoffeeMachine(100, 100)
coffee1.make_coffee()
coffee1.make_coffee()
coffee1.make_coffee()

# Enjoy your coffee
# Enjoy your coffee
# Refill Needed
