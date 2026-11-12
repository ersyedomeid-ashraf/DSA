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
