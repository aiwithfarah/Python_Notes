# .format() method

print("Hi my name is {}".format("farah"))
# Hi my name is farah

print("The {} {} {}".format('fox', 'brown', 'quick'))
# The fox brown quick
print("The {2} {1} {0}".format('fox', 'brown', 'quick'))
# The quick brown fox
print("The {q} {b} {f}".format(f='fox', b='brown', q='quick'))
# The quick brown fox

result = 100/777
print("The result is {r}".format(r=result))
# The result is 0.1287001287001287
print("The result is {r:1.3f}".format(r=result))
# The result is 0.129

# Formatted Strings - f-strings
print(f'The result is {result:1.3f}')
# The result is 0.129

name = "Farah"
age = 30
print(f"{name} is {age} years old.")
# Farah is 30 years old.
