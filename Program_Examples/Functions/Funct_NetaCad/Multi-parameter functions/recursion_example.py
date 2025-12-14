# Recursion --> function invokes itself
# The Fibonacci numbers definition is a clear example of recursion.

def factorial(n):

    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(4))  # 24
