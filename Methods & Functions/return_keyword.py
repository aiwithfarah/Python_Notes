# used to end the func and send the result back to the caller

def add_num(num1, num2):
    return num1 + num2


x = add_num(1, 2)
print(x)  # 3


# check if number is even

def check_even(num):
    result = num % 2 == 0
    return result


even = check_even(32)
print(even)  # True

# return true if ny number inside a list is even


def check_even_list(num_list):

    new_list = []
    for num in num_list:
        if num % 2 == 0:
            new_list.append(num)
        else:
            pass
    return new_list  # [2, 4, 6]


even_list = check_even_list([1, 2, 3, 4, 5, 6, 7])
print(even_list)
