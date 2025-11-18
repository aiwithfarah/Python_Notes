import random
from random import shuffle

example_list = [1, 2, 3, 4, 5, 6, 7]
shuffle(example_list)
print(example_list)

# shuffle list using function


def shuffle_list(example_list):
    shuffle(example_list)
    return example_list


x = shuffle_list(example_list)
print(x)
