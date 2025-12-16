from random import choice, sample
# choice chooses a random element
# sample build a list ()

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(choice(lst))  # 2
print(sample(lst, 5))  # [7, 6, 5, 8, 3]
