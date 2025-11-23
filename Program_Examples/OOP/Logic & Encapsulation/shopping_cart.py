# Goal: Create a class ShoppingCart.

# Attributes: An empty list items inside __init__.

# Methods:

# add_item(item_name): Adds a string to the list.

# remove_item(item_name): Removes the item if it exists.

# show_cart(): Prints all items in the cart.

# Test: Add "Apples" and "Bread", then remove "Apples", then show cart.

class ShoppingCart:

    def __init__(self):
        # We wont pass any item cause every new cart starts with an empty list
        self.items = []

    def add_item(self, item_name):
        self.items.append(item_name)
        print(f"Added Item : {item_name}")

    def remove_item(self, item_name):

        if item_name in self.items:
            self.items.remove(item_name)
            print(f"Removed Item: {item_name}")
        else:
            print(f"{item_name} is not in the cart!")

    def show_cart(self):
        print(self.items)


cart = ShoppingCart()
cart.add_item("Apple")
cart.add_item("Bread")
cart.show_cart()

cart.remove_item("Apple")
cart.show_cart()

# Added Item : Apple
# Added Item : Bread
# ['Apple', 'Bread']
# Removed Item: Apple
# ['Bread']
