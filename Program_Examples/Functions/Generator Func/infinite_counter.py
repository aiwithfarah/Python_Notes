def inifite_func(n):

    while True:
        yield n
        n += 1


my_gen = inifite_func(0)
print(my_gen)

print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
