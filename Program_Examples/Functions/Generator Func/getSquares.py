# Standard function

def get_squares(n):
    result = []
    for i in range(n):
        result.append(i*i)
    return result


def generate_squares(n):
    for i in range(n):
        yield i*i


my_gen = generate_squares(5)
print(my_gen)  # <generator object generate_squares at 0x00000177E8A8A5A0>

# We use next() to get the next value
print(next(my_gen))  # 1
print(next(my_gen))  # 1
