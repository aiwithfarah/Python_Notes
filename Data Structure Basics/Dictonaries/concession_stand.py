menu = {
    'pizza': 2.99,
    'popcorn': 1.99,
    'hotdog': 1.45,
    'nachos': 3.99,
    'soda': 1.50
}

# to keep track to user's selected items
cart = []
total = 0

print("----------Menu----------")
for key, value in menu.items():
    print(f"{key:10} : ${value:.2f}")

print('----------------------------')


while True:
    food = input("Select an item from the Menu: (q to quit): ").lower()
    if food == 'q':
        break
    elif food not in menu.keys():
        print("Please only select from the menu")
    else:
        cart.append(food)

print(cart)


print("-------Your Cart--------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")
print()
print(f"Your Total is {total}")
