"""
Write a program to search for a target element in an array using Linear Search.
"""

nums = [5, 3, 9, 8, 1, 6, 4, -10, -100]
target = 4

n = len(nums)


def linear_search(nums, target):
    for i in range(0, n):

        if nums[i] == target:
            return i

    return -1


print(linear_search(nums, target))


"""
Write a program to search for a target element in an array using Linear Search.
"""

nums = [32, 3, 5, 65, 78, -22, -90, 58, 96, 11]

target = 3


n = len(nums)


def linear_search(nums, target):
    for i in range(0, n):

        if nums[i] == target:
            return i

    return -1


print(linear_search(nums, target))
