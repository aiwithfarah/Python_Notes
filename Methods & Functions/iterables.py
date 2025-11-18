nums = [1, 2, 3, 4, 5]

for n in reversed(nums):
    print(n, end=" ")  # 5 4 3 2 1
print()


my_dict = {
    'name': 'Farah',
    'place': 'NYE',
    'animal': 'Tiger',
    'thing': 'Book',

}

for key, value in my_dict.items():
    print(f"{key} - {value}")

# name - Farah
# place - NYE
# animal - Tiger
# thing - Book
