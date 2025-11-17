fruits = ["apple", "banana", "cherry"]
# print(dir(fruits))
# print(help(fruits))
print("guava" in fruits)  # False

fruits.append("chilli")
print(fruits)  # ['apple', 'banana', 'cherry', 'chilli']
fruits.remove("apple")
print(fruits)  # ['banana', 'cherry', 'chilli']
fruits.insert(1, "pop")
print(fruits)  # ['banana', 'pop', 'cherry', 'chilli']
fruits.sort()
print(fruits)  # ['banana', 'cherry', 'chilli', 'pop']
fruits.reverse()
print(fruits)  # ['pop', 'chilli', 'cherry', 'banana']
# fruits.clear()
# print(fruits)  # []
print(fruits.index("pop"))  # 0
print(fruits.count('banana'))  # 1
