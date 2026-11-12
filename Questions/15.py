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
