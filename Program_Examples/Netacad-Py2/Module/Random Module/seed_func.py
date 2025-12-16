# Setting the generator's seed with the same value each time your program
# is run guarantees that the pseudo-random values
# emitted from the random module will be exactly the same.

from random import seed, random

seed(1)

for _ in range(5):
    print(random())

# 0.13436424411240122
# 0.8474337369372327
# 0.763774618976614
# 0.2550690257394217
# 0.49543508709194095
