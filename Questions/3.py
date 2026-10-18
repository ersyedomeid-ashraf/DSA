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
