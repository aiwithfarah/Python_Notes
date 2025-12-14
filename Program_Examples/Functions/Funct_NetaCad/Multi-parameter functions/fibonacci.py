# the first element of the sequence is equal to one (Fib1 = 1)
# the second is also equal to one (Fib2 = 1)
# every subsequent number is the the_sum of the two preceding numbers:(Fibi = Fibi-1 + Fibi-2)

# fib_1 = 1 fib_2 = 1 fib_3 = 1 + 1 = 2 fib_4 = 1 + 2 = 3
# fib_5 = 2 + 3 = 5 fib_6 = 3 + 5 = 8 fib_7 = 5 + 8 = 13

# The sequence is: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

def fib(n):

    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = 1
    elem_2 = 1
    sum = 0

    for i in range(3, n+1):
        sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, sum
    return sum


for n in range(1, 10):  # testing
    print(n, "->", fib(n))
