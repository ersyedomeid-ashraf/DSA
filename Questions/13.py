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
