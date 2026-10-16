"""
Write a program to print numbers from N to 1 using recursion with parameters.
"""


def func(i):
    if i < 1:
        return

    print(i)
    func(i - 1)


func(7)


"""
WAP to print the multiplication table of a number using recursion.
"""


def func(x, i):
    if i > 10:
        return

    print(x, "x", i, "=", x * i)
    func(x, i + 1)


func(46, 1)
