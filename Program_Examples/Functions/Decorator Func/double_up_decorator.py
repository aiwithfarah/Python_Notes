def double_decorator(func):

    def wrapper():
        func()
        func()
    return wrapper


@double_decorator
def greet():
    print("Hello")


greet()
