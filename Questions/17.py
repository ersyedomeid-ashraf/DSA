"""
Write a program to right rotate an array by one position.
"""

# Using Slicing

nums = [5, 4, 6, 7, 3, 2, 1, 8, 9, 10]

n = len(nums)

nums[:] = [nums[-1]] + nums[0 : n - 1]

print(nums)
