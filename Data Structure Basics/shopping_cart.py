# based on lists, sets and tuples

foods = []
prices = []
total = 0

while True:
    food = input("What food would you like to buy?: (q to quit) ").lower()
    if food == 'q':
        break
    else:
        price = float(input(f"Enter the price of {food}: $"))
        foods.append(food)
        prices.append(price)
print("----- Your Cart -----")

for f in foods:
    print(f, end=" ")
print()

for p in prices:
    total += p
print(f"Your Total Is: ${total}")
