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
