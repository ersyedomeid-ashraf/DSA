"""
WAP to print "Lailaa" 4 times using recursion.
"""

count = [0]


def func():
    if count[0] == 4:
        return

    count[0] = count[0] + 1
    func()
    print("Lailaa")


func()


"""
Write a program to print 'X' N times using recursion with parameters.
"""


def func(x, n):
    if n == 0:
        return

    print(x)

    func(x, n - 1)


func(5, 4)


"""
Write a program to print numbers from 1 to N using recursion with parameters.
"""


def func(i, n):
    if i > n:
        return

    print(i)
    func(i + 1, n)


func(1, 10)


"""
WAP to print "Python" 5 times using recursion with parameters.
"""


def func(n):
    if n == 0:
        return

    print("Python")
    func(n - 1)


func(5)
