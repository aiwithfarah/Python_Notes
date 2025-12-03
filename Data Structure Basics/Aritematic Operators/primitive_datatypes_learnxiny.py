# Floor Division rounds towards negative infinity

print(5 // 2)  # 2
print(-5 // 2)  # -3

# i % j have the same sign as j
print(7 % 3)  # 1
# 2 (sign does not change, cause the result of i%j will have the same sign as j)
print(-7 % 3)

# Booleans are priitive
# True and False are 1 and 0
print(True + True)  # --> 2
print(False - 5)  # --> -5

print(0 == False)  # True
print(2 == True)  # False
print(2 > True)  # True
print(-5 != False)  # True

# None, 0, Empty String, list, dict, tuple,set all evalate to False

# chaining conditionals
print(1 < 2 < 3)  # True


# is vs ==
# is checks if two variables rfer to the same object
# == checks of the objects have the same ValueError
a = [1, 2, 3, 4]
b = a
print(b is a)  # True
print(b == a)  # True

b = [1, 2, 3, 4]
print(b is a)  # False
print(b == a)  # True

# None is an object
