# executes a block of code a fixed num of times

myList = [1, 2, 3, 4, 5, 6]

for num in myList:
    print(num)

# 1
# 2
# 3
# 4
# 5
# 6

# print even numbers
for num in myList:
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

# 1 is Odd
# 2 is Even
# 3 is Odd
# 4 is Even
# 5 is Odd
# 6 is Even

# sum of every number in a the list
sum = 0
for num in myList:
    sum += num
print(sum)  # 21

# access every character in a string
new_string = "farah"

for char in new_string:
    print(char)

# f
# a
# r
# a
# h

# ITERATE OVER A TUPLE
tup = (1, 2, 3)

for item in tup:
    print(item)

# 1
# 2
# 3

# tuple unpacking
my_list = [(1, 2), (3, 4), (5, 6)]

for (a, b) in my_list:
    print(a)
    print(b)

# 1
# 2
# 3
# 4
# 5
# 6

# iterating over a dict
d = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}

for item in d:
    print(item)
# a
# b
# c
# d

for item in d.items():
    print(item)

# ('a', 1)
# ('b', 2)
# ('c', 3)
# ('d', 4)

for key, value in d.items():
    print(value)

# 1
# 2
# 3
# 4
