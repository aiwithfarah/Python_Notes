def print_name(name):
    print(f"Hello {name}")


print_name("Farah")  # Hello Farah


# providing default values to parameters
def say_hello(name="farah"):
    print(f"hello {name}")


say_hello()  # hello farah
say_hello("Sana")  # hello Sana
