"""
Write a program to print numbers from N to 1 using recursion with parameters.
"""


def func(i):
    if i < 1:
        return

    print(i)
    func(i - 1)


func(7)
