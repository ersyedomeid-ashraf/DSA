"""
WAP to print elements present at even indexes of a list using recursion.
"""


def func(arr, i):
    if i >= len(arr):
        return

    print(arr[i])
    func(arr, i + 2)


func([10, 20, 30, 40, 50], 0)


"""
WAP to print each digit of a number using recursion.
"""


def func(n):
    if n == 0:
        return

    func(n // 10)
    print(n % 10)


func(1234567890)


"""
WAP to print list elements in reverse order using recursion.
"""


def func(arr, i):
    if i < 0:
        return

    print(arr[i])
    func(arr, i - 1)


func([10, 20, 30, 40], 3)


"""
WAP to print a string in reverse order using recursion.
"""


def func(text, i):
    if i < 0:
        return

    print(text[i])
    func(text, i - 1)


func("FAIRYYYYY TAIL", 8)


"""
Write a program to print "Start" before the recursive call and "End" after the recursive call.
"""


def func(count):
    if count == 0:
        return

    print("Start")
    func(count - 1)
    print("End")


func(2)
