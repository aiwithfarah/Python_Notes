# *args allows us to pass multiple arguments
def myunc(*args):
    return sum(args) * 0.05


x = myunc(1, 2, 3, 4, 5)
print(x)  # 0.75


# **kwargs allows us to pass multiple keywprd args

def myfunc(**kwargs):
    if 'fruit' in kwargs:
        return f"My Fruit of choice is {kwargs['fruit']}"
    else:
        return "My fruit of choice is not available here"


y = myfunc(fruit='apple', veggie='papaya')
print(y)


def address(**kwargs):
    # for key in kwargs.keys():
    #     print(key)

    for item, value in kwargs.items():
        print(f"{item} : {value}")


x = address(street="Kanakia", locality="Marigold",
            complex="GG", building=1, flat_no=502)


# street : Kanakia
# locality : Marigold
# complex : GG
# building : 1
# flat_no : 502
