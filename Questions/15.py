"""
Write a program to check whether an array is sorted in ascending order or not.
"""

nums = [45, 75, 88, 90, 98, 43, 66, 87, 95]


def isSorted(nums):

    n = len(nums)

    for i in range(0, n - 1):
        if nums[i] > nums[i + 1]:
            return False

    return True


print(isSorted(nums))


"""
Write a program to check whether an array is sorted in ascending order or not.
"""

nums = [12, 25, 34, 46, 58, 67, 79, 85, 97]


def isSorted(nums):

    n = len(nums)

    for i in range(0, n - 1):
        if nums[i] > nums[i + 1]:
            return False

    return True


print(isSorted(nums))


"""
Write a program to check whether an array is sorted in ascending order or not.
"""

nums = [12, 23, 34, 45, 56, 67, 78, 89, 90, 100]


def isSorted(nums):

    n = len(nums)

    for i in range(0, n - 1):
        if nums[i] > nums[i + 1]:
            return False

    return True


print(isSorted(nums))


# Another one


nums = [45, 33, 46, 78, 89, 98, 53, 21, 34, 58, 95]


def isSorted(nums):

    n = len(nums)

    for i in range(0, n - 1):
        if nums[i] > nums[i + 1]:
            return False

    return True


print(isSorted(nums))
