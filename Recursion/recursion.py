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
