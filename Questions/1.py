"""
Write a program to Extraction of digits using loops.
"""

n = 35478

num = n

while num > 0:

    last_digit = num % 10
    print(last_digit)

    num = num // 10


# Another one

n = 78453

num = n

while num > 0:

    last_digit = num % 10
    print(last_digit)

    num = num // 10
