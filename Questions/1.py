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


"""
Write a program to count the number of digits in an integer. 
"""

n = 65745

num = n
count = 0

while num > 0:

    count += 1

    num = num // 10


print(count)


# Another one


n = 764599873

num = n
count = 0

while num > 0:

    count += 1

    num = num // 10


print(count)


"""
Write a program to check if a number is palindrome or not.
"""

n = 12345

num = n
result = 0

while num > 0:

    last_digit = num % 10
    result = (result * 10) + last_digit
    num = num // 10

print(result)


# Another one

n = 786593

num = n
result = 0

while num > 0:

    last_digit = num % 10
    result = (result * 10) + last_digit
    num = num // 10

print(result)


"""
Write a program to Extraction of digits using loops.
"""

n = 4783638

num = n

while num > 0:

    last_digit = num % 10
    print(last_digit)

    num = num // 10


"""
Write a program to count the number of digits in an integer. 
"""

n = 7548794

num = n
count = 0

while num > 0:

    count += 1

    num = num // 10


print(count)


"""
Write a program to check whether a given number is an Armstrong number or not using a while loop.
"""


n = 153

num = n
total = 0

nod = len(str(n))

while num > 0:

    large_digit = num % 10
    total = total + (large_digit**nod)
    num = num // 10

print(total == n)


# Another one

n = 6557

num = n
total = 0

nod = len(str(n))

while num > 0:

    large_digit = num % 10
    total = total + (large_digit**nod)
    num = num // 10

print(total == n)


"""
Write a program to find and print all the factors of the given number.
"""

num = 20

result = []

for i in range(1, num + 1):

    if num % i == 0:
        result.append(i)

print(result)
