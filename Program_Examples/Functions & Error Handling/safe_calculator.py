# Write a function divide(a, b).

# It should return a / b.

# # Crucial: Use a try...except block to catch the ZeroDivisionError if b is 0. Return "Cannot divide by zero" instead of crashing.

def divide(a, b):

    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot Divide by Zero"


x = divide(10, 0)
y = divide(10, 2)
print(x)
print(y)
