# You have a list of numbers. You need to multiply them all together to get one giant number.
# numbers = [1, 2, 3, 4]
# Goal 1 * 2 * 3 * 4 = 24

from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x*y, numbers)
print(product)  # 24
