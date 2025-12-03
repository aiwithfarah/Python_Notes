def my_counter():
    print("Start")
    yield 1

    print("Resuming")
    yield 2

    print("Almost Done")
    yield 3


gen = my_counter()
print(next(gen))
print(next(gen))
print(next(gen))

# Start
# 1
# Resuming
# 2
# Almost Done
# 3
