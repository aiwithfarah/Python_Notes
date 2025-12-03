# Your Challenge: Write a filter function (using a lambda) that creates a new list
# containing only numbers greater than or equal to 18.

ages = [12, 18, 25, 16, 30, 17]

ages_greater_than_18 = list(filter(lambda x: x >= 18, ages))
print(ages_greater_than_18)  # [18, 25, 30]
