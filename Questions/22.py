# Revision

"""
Write a program to sort a list of names in alphabetical order using Selection Sort.
"""


def selection_sort(names):
    n = len(names)

    for i in range(0, n):
        mini_index = i

        for j in range(i + 1, n):
            if names[j] < names[mini_index]:
                mini_index = j

        names[i], names[mini_index] = names[mini_index], names[i]


names = ["Shahid", "Rahul", "Zayn", "Arpit", "Narendra", "Amit", "Kaif"]

selection_sort(names)

print(names)


"""
Write a program to sort a list of numbers in ascending order using Bubble Sort
"""

nums = [40, 12, 64, 56, 78, 98, 76, 45, 32, 234, 10, 30, 20, 5]

n = len(nums)

for i in range(n - 2, -1, -1):
    for j in range(0, i + 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print(nums)


"""
Write a program to check whether an array is sorted in ascending order or not.
"""

nums = [32, 34, 45, 4, 67, 77, 87, 89, 90, 92, 11, 23]


def isSorted(nums):

    n = len(nums)

    for i in range(0, n - 1):
        if nums[i] > nums[i + 1]:
            return False

    return True


print(isSorted(nums))

# OR

nums = [12, 23, 34, 45, 56, 67, 78, 89, 90]


def isSorted(nums):

    n = len(nums)

    for i in range(0, n - 1):
        if nums[i] > nums[i + 1]:
            return False

    return True


print(isSorted(nums))


"""
Write a program to right rotate an array by k positions.
"""

# Brute Force Approach

nums = [32, 34, 45, 4, 67, 77, 87, 89, 90, 92, 11, 23]

k = 3

n = len(nums)

rotations = k % n

for _ in range(0, rotations):
    # (_) is used because we don't need the loop variable, only repeat the loop
    e = nums.pop()
    nums.insert(0, e)

print(nums)


# Better Solution (Using Slicing)

nums = [98, 79, 57, 76, 24, 35, 51, 22, 10]

n = len(nums)

k = 5
k = k % n

nums[:] = nums[n - k :] + nums[: n - k]

print(nums)


# Optimal Approach (Using Reversal Algorithm)

nums = [44, 33, 56, 77, 88, 90, 22, 32, 12, 11]

n = len(nums)

k = 5
k = k % n


def reverse(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


reverse(nums, n - k, n - 1)
reverse(nums, 0, n - k - 1)
reverse(nums, 0, n - 1)

print(nums)


"""
Write a program to right rotate an array by one position.
"""

# Using Temporary Variable

nums = [22, 3, 44, 11, 55, -44, -6, 56, 87, -21, 72]

n = len(nums)

temp = nums[n - 1]

for i in range(n - 2, -1, -1):
    nums[i + 1] = nums[i]

nums[0] = temp

print(nums)


"""
Write a program to right rotate an array by one position.
"""

# Using Slicing

nums = [2, 3, 1, 4, 6, 8, 9, 6, 10, -2]

n = len(nums)

nums[:] = [nums[-1]] + nums[0 : n - 1]

print(nums)


"""
Write a program to search for a target element in an array using Linear Search.
"""

nums = [46, 68, -76, 53, 90, 87, -20, 65, 51, 34, 66, 88, 55]

target = 65


n = len(nums)


def linear_search(nums, target):
    for i in range(0, n):

        if nums[i] == target:
            return i

    return -1


print(linear_search(nums, target))


"""
Write a program to merge two sorted arrays into a single sorted array without duplicates
"""

nums1 = [1, 2, 3, 5, 6, 7, 8, 9, 10]
nums2 = [2, 3, 4, 5, 6, 11, 12, 13]

n = len(nums1)
m = len(nums2)

result = []

i = 0
j = 0

while i < n and j < m:

    if nums1[i] <= nums2[j]:

        if len(result) == 0 or result[-1] != nums1[i]:
            result.append(nums1[i])
        i += 1

    else:

        if len(result) == 0 or result[-1] != nums2[j]:
            result.append(nums2[j])
        j += 1


while i < n:

    if len(result) == 0 or result[-1] != nums1[i]:
        result.append(nums1[i])
    i += 1

while j < m:

    if len(result) == 0 or result[-1] != nums2[j]:
        result.append(nums2[j])
    j += 1

print(result)


"""
Write a program to merge two sorted arrays into a single sorted array without duplicates.
"""


cities1 = ["Bhopal", "Chennai", "Kolkata", "Ludhiyana", "Nanital", "Pune"]
cities2 = ["Agra", "Champawat", "Delhi", "Gujrat", "Jaipur", "Mumbai"]

result = []

i = 0
j = 0

while i < len(cities1) and j < len(cities2):

    if cities1[i] <= cities2[j]:
        result.append(cities1[i])
        i += 1

    else:
        result.append(cities2[j])
        j += 1

while i < len(cities1):
    result.append(cities1[i])
    i += 1

while j < len(cities2):
    result.append(cities2[j])
    j += 1

print(result)


"""
Write a program to merge two sorted lists of countries into a single sorted list without duplicates.
"""


countries1 = ["Australia", "Canada", "France", "India"]
countries2 = ["Brazil", "China", "Germany", "Japan"]

result = []

i = 0
j = 0

while i < len(countries1) and j < len(countries2):

    if countries1[i] <= countries2[j]:
        if len(result) == 0 or result[-1] != countries1[i]:
            result.append(countries1[i])
        i += 1

    else:
        if len(result) == 0 or result[-1] != countries2[j]:
            result.append(countries2[j])
        j += 1

while i < len(countries1):
    if len(result) == 0 or result[-1] != countries1[i]:
        result.append(countries1[i])
    i += 1

while j < len(countries2):
    if len(result) == 0 or result[-1] != countries2[j]:
        result.append(countries2[j])
    j += 1

print(result)
