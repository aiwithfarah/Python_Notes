# There are only two kinds of circumstances when None can be safely used:

# 1.when you assign it to a variable (or return it as a function's result)
# 2. when you compare it with a variable to diagnose its internal state.

value = None
if value is None:
    print("Sorry you don't carry any value!")


# if a function doesn't return a certain value using a return expression clause,
#  it is assumed that it implicitly returns None.

def check_even(num):

    if (num % 2 == 0):
        return True


print(check_even(2))  # True
print(check_even(1))  # None
