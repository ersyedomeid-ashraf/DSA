"""
Write a program to sort a list in ascending order using Selection Sort.

"""


def selection_sort(nums):
    n = len(nums)

    for i in range(0, n):
        mini_index = i

        for j in range(i + 1, n):
            if nums[j] < nums[mini_index]:
                mini_index = j

        nums[i], nums[mini_index] = nums[mini_index], nums[i]


nums = [3, 4, 8, 6, 99, 87, 7, 9, 10, 22]

selection_sort(nums)

print(nums)


# Another one


def selection_sort(nums):
    n = len(nums)

    for i in range(0, n):
        minimum_index = i

        for j in range(i + 1, n):
            if nums[j] < nums[minimum_index]:
                minimum_index = j

        nums[i], nums[minimum_index] = nums[minimum_index], nums[i]


nums = [3, 9, 8, 4, 5, 2, 1, 55, 32, 34, 11, 22, 10]

selection_sort(nums)

print(nums)


"""
Write a program to sort a list of numbers in ascending order using Bubble Sort.
"""


nums = [5, 7, 3, 2, 1, 4, 9, 10, 11]

n = len(nums)

for i in range(n - 2, -1, -1):

    for j in range(0, i + 1):

        if nums[j] > nums[j + 1]:

            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print(nums)


# Another one

num = [22, 4, 2, 33, 78, 9, 10, 34, 67, 44]

n = len(nums)

for i in range(n - 2, -1, -1):

    for j in range(0, i + 1):

        if nums[j] > nums[j + 1]:

            nums[j], nums[j + 1] = nums[j + 1], nums[j]


print(nums)


"""
Write a program to sort a list of numbers in ascending order using Selection Sort.
"""


def selection_sort(nums):
    n = len(nums)

    for i in range(0, n):
        mini_index = i

        for j in range(i + 1, n):
            if nums[j] < nums[mini_index]:
                mini_index = j

        nums[i], nums[mini_index] = nums[mini_index], nums[i]


nums = [8, 3, 5, 1, 6, 4, 9, 2, 7, 8]

selection_sort(nums)

print(nums)
