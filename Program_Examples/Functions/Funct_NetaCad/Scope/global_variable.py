def my_func():
    global var
    var = 2
    print(f"The value of the variable is {var}")


var = 1
my_func()
print(var)

# The value of the variable is 2
# 2


a = 1


def fun():
    global a
    a = 2
    print(a)


a = 3
fun()  # 2
print(a)  # 2
