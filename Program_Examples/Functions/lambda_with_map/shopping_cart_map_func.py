# The "Shopping Cart" (Object/Dictionary Processing)
# You have a list of prices (numbers), and a store-wide sale just started.
# You need to apply a 20% discount to every item and format it as a currency string.

# Input: [100.00, 50.00, 25.00]

# Challenge: Multiply by 0.8 and add a "$" sign.

# Goal: Practice combining math and string formatting.

prices = [100.00, 50.00, 25.00]

discounted_prices = list(map(lambda x: f"${x*0.8}", prices))

print(discounted_prices)
