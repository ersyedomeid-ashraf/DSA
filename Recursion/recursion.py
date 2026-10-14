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
