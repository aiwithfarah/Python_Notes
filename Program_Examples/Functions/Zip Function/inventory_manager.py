# You have a list of items and a list of their quantities.

# Use zip to combine them.

# Convert the result into a dictionary so we can look up how many "Swords" we have.

items = ["Sword", "Shield", "Potion"]
counts = [1, 1, 5]
swords = dict(zip(items, counts))
print(swords)  # {'Sword': 1, 'Shield': 1, 'Potion': 5}
