import random
from random import shuffle
from random import randint

print(list(range(0, 11, 2)))
# [0, 2, 4, 6, 8, 10]

# enumerate
word = "abcde"
for item in enumerate(word):
    print(item)

# (0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'd')
# (4, 'e')

# zip together lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
# we need to iterate through it in order for this to work
for item in zip(list1, list2):
    print(item)

# ('a', 1)
# ('b', 2)
# ('c', 3)

# IN Operator - to check of item is in the list
print('x' in [1, 2, 3])  # False

my_num_list = [0, 12, 5, 6, 90]
print(min(my_num_list))  # 0
print(max(my_num_list))  # 90

# random library

list_num = [0, 1, 2, 3, 4, 5, 6]
shuffle(list_num)
print(list_num)  # [2, 3, 4, 0, 5, 1, 6]

print(randint(0, 100))  # 84

# input() to gather user input | retrns a str
x = input('>> Enter your name here: ')
print(f"Hi {x}")  # Hi farah
