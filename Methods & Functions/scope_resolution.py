# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Gloabl -> Built-In

from math import e


def details():
    name = "farah"  # -->Local Scope
    print(name)


details()  # farah

# Enclosed Scope


def func1():
    x = 1  # Enclosed Scope Variable for func2

    def func2():
        print(x)
    func2()


func1()  # 1

# Global scope

x = 1


def funcA():

    print(x)  # 1

    def funcB():
        print(x)  # 1
    funcB()


funcA()

# Built In
# e is an exponential constant and is built in


def func():
    print(e)  # 2.718281828459045


func()
