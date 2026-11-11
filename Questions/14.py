"""
Write a program to find the second large element in an array without sorting
"""

# Brute Force Solution

nums = [15, 42, 67, 29, 85, 96, 73, 54, 88, 31, 62, 90]

largest = max(nums)
second_largest = -1

for i in range(0, len(nums)):

    if nums[i] > second_largest and nums[i] < largest:
        second_largest = nums[i]

print(second_largest)
