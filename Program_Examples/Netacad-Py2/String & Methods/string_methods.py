# centers string by adding spaces before and after the string
print('[' + 'alpa'.center(10) + ']')  # [   alpa   ]

# The two-parameter variant of center() makes use of the character from the second argument, instead of a space
print('[' + 'alpha'.center(10, "*") + ']')

print("farah".endswith("f"))  # False
print("farah".find('r'))  # 2
print("farah".find("a", 2, -1))  # 3

print(",".join(["apple", "banana", "cherry"]))  # apple,banana,cherry

print("Farah Rubena".replace("Rubena", "Farah"))  # Farah Farah
