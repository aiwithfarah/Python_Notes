# map function

def square(n):
    return n*n


my_nums = [1, 2, 3, 4, 5]
# We want to apply the square fun to every single item in the list
for item in map(square, my_nums):
    print(item)

# 1
# 4
# 9
# 16
# 25


def splicer(mystr):

    if len(mystr) % 2 == 0:
        return 'Even'
    else:
        return mystr[0]


names = ["farah", "rusu", "sun"]
print(list(map(splicer, names)))
# ['f', 'Even', 's']

# Filter func


def chck_even(num):
    return num % 2 == 0


mynums = [1, 2, 3, 4, 5, 6]
print(list(filter(chck_even, my_nums)))  # [2, 4]
for item in filter(chck_even, my_nums):
    print(item)
    # 2
    # 4

# lambda expressions
# square = lambda n: n**2
# print(square(2))

# lambda in conjunction with map
num_lists = [1, 2, 3, 4, 5]
print(list(map(lambda n: n**2, num_lists)))
# [1, 4, 9, 16, 25]

# lambda in conjunction with filter
print(list(filter(lambda n: n % 2 == 0, num_lists)))
[2, 4]
