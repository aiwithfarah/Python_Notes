# by default the print function prints out a new line to the end
print("Hello, Farah. ")
print("How are you?")

# Hello, Farah.
# How are you?

print("Hello, Rusu. ", end="")
print("How are you?")
# Hello, Rusu. How are you?

# Ternary Operator. If in a expression
print("yay" if 0 > 1 else "nay!")  # nay

# Tuple Unpacking - -> Unpack tuples(or lists) into variables
a, b, c = (1, 2, 3)
print(b)  # 2

# Extened unpacking
a, *c, b = (1, 2, 3, 4)
print(c)  # [2, 3]

dict1 = {
    'one': 1,
    'two': 2,
    'three': 3,
}

print(dict1.keys())  # dict_keys(['one', 'two', 'three'])
# ['one', 'two', 'three'] --> Wrap leys in list to get it out of the iterable
print(list(dict1.keys()))

# looking for non-existig key results in a key error
# print(dict1['four']) KeyError: 'four'

# Use get() metho to avoid KeyErrorśr̥
print(dict1.get("four"))  # None

# setdefault() inserts into a dict only if the given key isn't present
dict1.setdefault("five", 5)
print(dict1)  # {'one': 1, 'two': 2, 'three': 3, 'five': 5}

# Set
set1 = {1, 1, 2, 3, 4}
print(set1)  # {1, 2, 3, 4}

set1.add(5)
print(set1)  # {1, 2, 3, 4, 5}
print(type(set1))

# Set Union
set2 = {6, 7, 8}
print(type(set2))
print(set1 | set2)  # {1, 2, 3, 4, 5, 6, 7, 8}

# Set Intersection
print(set1 & set2)  # set()

set3 = {4, 5, 6, 7}
set4 = {4, 5, 8}
print(set3 - set4)  # {6, 7} difference
print(set3 ^ set4)  # {6, 7, 8} symmetric difference

# superset
set5 = {1, 2}
set6 = {1, 2, 3, 4, 5}
print(set5 >= set6)  # false

# subset
print(set5 <= set6)  # True
