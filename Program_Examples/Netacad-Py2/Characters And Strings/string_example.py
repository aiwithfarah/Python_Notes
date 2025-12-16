# Strings are immutable sequences
# len func counts whitespace as well

name = '''farah
rubena'''

print(len(name))  # 12
print(name.index('a'))  # 1


# The list() function takes its argument (a string) and creates a new list containing all the string's characters,
#  one per list element.

# ['f', 'a', 'r', 'a', 'h', '\n', 'r', 'u', 'b', 'e', 'n', 'a']
print(list(name))
