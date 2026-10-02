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


"""
Write a program to find and print all the factors of the given number.
"""

num = 10

result = []

for i in range(1, num // 2 + 1):

    if num % i == 0:
        result.append(i)

result.append(num)

print(result)


"""
Write a program to find and print all the factors of a given number in ascending order.
"""


from math import sqrt

num = 36
result = []

for i in range(1, int(sqrt(num)) + 1):

    if num % i == 0:
        result.append(i)

        if num // i != i:

            result.append(num // i)

result.sort()

print(result)


"""
Store the frequency of each element in a dictionary.
"""


# Method 1

nums = [5, 6, 7, 7, 7, 1, 9, 111, 1, 1, 5, 4, 1]

freq_map = {}

for i in range(0, len(nums)):

    if nums[i] in freq_map:
        freq_map[nums[i]] += 1

    else:
        freq_map[nums[i]] = 1

print(freq_map)


# Method 2

nums = [5, 6, 7, 7, 7, 1, 9, 3, 7, 8, 9, 2, 1, 1, 1, 5, 4, 1]

hash_map = {}

n = len(nums)

for i in range(0, n):

    hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1

print(hash_map)


"""
Write a program to find and print all the factors of the given number.
"""

num = 45

result = []

for i in range(1, num + 1):

    if num % i == 0:
        result.append(i)

print(result)


"""
Store the frequency of each element in a dictionary.
"""

nums = [2, 5, 2, 8, 5, 2, 9, 8, 5, 1]

freq_map = {}

for i in range(0, len(nums)):

    if nums[i] in freq_map:
        freq_map[nums[i]] += 1

    else:
        freq_map[nums[i]] = 1

print(freq_map)


"""
Write a program to find and print all the factors of a given number in descending order.
"""

num = 36
result = []

for i in range(1, int(sqrt(num)) + 1):

    if num % i == 0:
        result.append(i)

        if num // i != i:
            result.append(num // i)

result.sort(reverse=True)

print(result)


"""
Write a program to Print all even factors
"""

from math import sqrt

num = 36
result = []

for i in range(1, int(sqrt(num)) + 1):

    if num % i == 0:

        if i % 2 == 0:
            result.append(i)

        pair = num // i

        if pair != i and pair % 2 == 0:
            result.append(pair)

result.sort()

print(result)


"""
Write a program to print all odd factors
"""

from math import sqrt

num = 36
result = []

for i in range(1, int(sqrt(num)) + 1):

    if num % i == 0:

        if i % 2 != 0:
            result.append(i)

        pair = num // i

        if pair != i and pair % 2 != 0:
            result.append(pair)

result.sort()

print(result)


"""
Write a program to find the sum of all factors
"""

from math import sqrt

num = 65
result = []

for i in range(1, int(sqrt(num)) + 1):

    if num % i == 0:
        result.append(i)

        if num // i != i:
            result.append(num // i)

print(sum(result))
