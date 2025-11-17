my_list = ['farah', 30, 'NYC', 50.0]
print(len(my_list))  # 4
print(my_list[1])  # 30 --> Indexing
print(my_list[::-1])  # [50.0, 'NYC', 30, 'farah'] -->Slicing
# ['farah', 30, 'NYC', 50.0, 1, 2, 3, 4] --> concatenation
print(my_list + [1, 2, 3, 4])

my_list[0] = "haraf"
print(my_list)  # ['haraf', 30, 'NYC', 50.0]
my_list.append("aba")
print(my_list)  # ['haraf', 30, 'NYC', 50.0, 'aba']
popped_item = my_list.pop(2)
print(popped_item)  # NYC
print(my_list)  # ['haraf', 30, 50.0, 'aba']

new_list = ['p', 'a', 'o', 'c']
new_list.sort()  # inplace method - doesn't return anything but sorts the list in place
print(new_list)  # ['a', 'c', 'o', 'p']

new_list.reverse()  # inplace method does not return anything, Reverses the list in place
print(new_list)  # ['p', 'o', 'c', 'a']

# Index a Nested Lsit
nested_list = [1, 2, 3, [4, 5]]
print(nested_list[3][1])  # 5
