fruits = {1, 2, 3, 4, 5, 6}
fruits.remove(1)
print(fruits)  # {2, 3, 4, 5, 6}
fruits.add(44)
print(fruits)  # {2, 3, 4, 5, 6, 44}

fruits.discard(4)
print(fruits)  # {2, 3, 5, 6, 44}

# Removes an item safely (No error if the item is missing).
fruits.discard("Apple")
print(fruits)  # {2, 3, 5, 6, 44}

# .pop(): Removes a random item (since sets are unordered).
fruits.pop()
print(fruits)  # {3, 5, 6, 44}
