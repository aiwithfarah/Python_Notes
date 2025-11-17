my_str = "hello"
# task : to make a list of every character in the list
x = [x for x in my_str]
print(x)  # ['h', 'e', 'l', 'l', 'o']

# for square of every number
my_list = [x**x for x in range(1, 10)]
print(my_list)
# [1, 4, 27, 256, 3125, 46656, 823543, 16777216, 387420489]

# for even numbers
my_evens = [x for x in range(0, 11) if x % 2 == 0]
print(my_evens)
# [0, 2, 4, 6, 8, 10]

# double a number from 1 to 9
doubles = [x+x for x in range(1, 10)]
print(doubles)
# [2, 4, 6, 8, 10, 12, 14, 16, 18]
