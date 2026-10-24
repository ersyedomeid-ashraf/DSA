"""
Write a program to sort a list of numbers in ascending order using Insertion Sort.
"""

nums = [3, 5, 6, 4, 7, 9, 8, 1, 2, 10]

n = len(nums)

for i in range(1, n):

    key = nums[i]
    j = i - 1

    while j >= 0 and nums[j] > key:
        nums[j + 1] = nums[j]

        j -= 1

    nums[j + 1] = key


print(nums)


# Another one

nums = [2, 11, 4, 6, 45, 6, 54, 21, 32, 7, 5, 4, 3, 1]

n = len(nums)

for i in range(1, n):

    key = nums[i]
    j = i - 1

    while j >= 0 and nums[j] > key:
        nums[j + 1] = nums[j]

        j -= 1

    nums[j + 1] = key


print(nums)
