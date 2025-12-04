# Write a script using List Comprehensions OR Lambdas (your choice) that:

# Filters out any price lower than $10 (Too cheap!).

# Adds a 10% tax to the remaining prices (Multiply by 1.1).

# Prints the final list.

prices = [10, 55, 20, 5, 100, 3]

final_list = list(map(lambda x: x*1.1, filter(lambda x: x >= 10, prices)))
print(final_list)
