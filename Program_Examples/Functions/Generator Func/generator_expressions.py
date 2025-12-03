# List Comprehesnsions use[]
# Generator Expressions use ()


# List Comprehension creates full list in the memory
square_list = [x*x for x in range(1, 11)]
print(square_list)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Generator Expression
square_gen = (x*x for x in range(1, 11))
print(square_gen)
# <generator object <genexpr> at 0x000002201D13B510>

# to use it
for num in square_gen:
    print(num)

# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
# 100
