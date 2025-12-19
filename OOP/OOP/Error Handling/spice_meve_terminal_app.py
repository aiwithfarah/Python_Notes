# # Cash Register

# REQUIREMENTS:
# Class Product:
# __init__: Name, Price.
# __str__: Returns "Item: [Name] - $[Price]".
# Class DiscountProduct (Inherits from Product):
# __init__: Name, Price, Discount_Amount.
# Override __str__: Returns "Item: [Name] - $[Price] (DISCOUNT APPLIED!)".
# Method get_final_price(): Returns the price minus the discount.
# The Logic (Main Code):
# Create a list of products (one normal Product, one DiscountProduct).
# Ask the user "Which product number do you want? (0 or 1)".
# Use try/except to handle if they type "apple" or a number that doesn't exist.
# Print the selected product and the final price.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Item: {self.name} - ${self.price}"


class DiscountProduct(Product):
    # FIXED: Added 'price' to arguments
    def __init__(self, name, price, discount_amount):
        # FIXED: Sent 'price' to the Parent
        super().__init__(name, price)
        self.discount_amount = discount_amount

    def __str__(self):
        return f"Item: {self.name} - ${self.price} (DISCOUNT APPLIED!)"

    def get_final_price(self):
        return self.price - self.discount_amount

# --- MAIN LOGIC ---


# 1. Create the Objects (The Robots)
p1 = Product("Malvani Masala", 300)
p2 = DiscountProduct("Old Stock Pepper", 200, 50)  # 200 price, 50 off

# 2. Put Objects in a list
product_list = [p1, p2]

# 3. Get User Input
user_input_str = input("Which product do you want (0 or 1): ")

try:
    # Convert to integer
    index = int(user_input_str)

    # Select the product from the list using the index
    selected_product = product_list[index]

    # Print the result using our Magic Method __str__
    print(f"\nYou selected: {selected_product}")

    # Check if it has a discount method and show final price
    # (A simple way to check type, or just rely on polymorphism if both had the method)
    if isinstance(selected_product, DiscountProduct):
        print(f"Final Price to Pay: ${selected_product.get_final_price()}")
    else:
        print(f"Final Price to Pay: ${selected_product.price}")

except ValueError:
    print("Error: Please enter a number!")
except IndexError:
    print("Error: That product number doesn't exist!")
