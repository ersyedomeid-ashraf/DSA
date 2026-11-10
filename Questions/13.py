"""
Write a program to find the second large element in an array without sorting
"""

# Brute Force Solution

nums = [33, 56, 44, 51, 78, 98, 99, 78, 65, 76, 78, 90, 80, 44]

largest = max(nums)
second_largest = -1

for i in range(0, len(nums)):

    if nums[i] > second_largest and nums[i] < largest:
        second_largest = nums[i]

print(second_largest)


# Better Solution Code

nums = [65, 78, 96, 97, 99, 90, 43, 54, 31, 23, 32, 11, 28, 79, 65]

largest = float("-infinity")
second_largest = float("-infinity")

n = len(nums)

for i in range(0, n):
    largest = max(largest, nums[i])

for i in range(0, n):
    if nums[i] > second_largest and nums[i] != largest:
        second_largest = nums[i]

print(second_largest)
