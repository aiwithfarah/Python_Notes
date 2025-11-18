def myfunc(test_string):

    new_str = ''
    for index, char in enumerate(test_string):
        if index % 2 == 0:
            # Use the 'char' variable and make it uppercase
            new_str += char.upper()
        else:
            # Use the 'char' variable and make it lowercase
            new_str += char.lower()

    return new_str


x = myfunc("Anthropomorphism")
print(x)
