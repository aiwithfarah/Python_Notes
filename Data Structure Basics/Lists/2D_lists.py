fruits = ["apple", "banana", "cherry", "coconut"]  # ---> 1 Dimensional List
veggies = ["bhendi", "methi", "palak"]
meats = ["chicken", "lamb", "fish"]


groceries = [fruits, veggies, meats]
print(groceries)

for food in groceries:
    for item in food:
        print(item)
# apple
# banana
# cherry
# coconut
# bhendi
# methi
# palak
# chicken
# lamb
# fish
