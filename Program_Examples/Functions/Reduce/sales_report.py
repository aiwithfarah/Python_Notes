# You are analyzing a list of daily transactions in US Dollars ($). However, your data is messy:

# Some transactions are refunds (negative numbers) or errors (0). You need to ignore them.

# Your boss wants the report in Euros (€). The exchange rate is 0.85.

# You need the Total Sum of all valid revenue in Euros.

from functools import reduce

transactions = [100, -50, 200, 0, 50, -10]
valid_items = reduce(lambda x, y: x+y, list(
    map(lambda x: x*0.85, filter(lambda x: x > 0, transactions))))
print(valid_items)
