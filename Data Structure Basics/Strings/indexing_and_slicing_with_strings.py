my_string = "hello, World"
# H  --> Indexing allows us to access element of the sequence
print(my_string[0])
print(my_string[-3])  # r --> Indexing

print(my_string[2:])  # llo, World --> Slicing
print(my_string[:3])  # hel --> Slicing
print(my_string[:])  # hello, World --> Slicing
print(my_string[::2])  # hlo ol  --> Slicing with step
print(my_string[::-1])  # dlroW ,olleh  --> Reverses a String

print(my_string.split())  # ['hello,', 'World']
