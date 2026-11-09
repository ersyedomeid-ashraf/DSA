"""
Write a program to find the largest element in an array.
"""

nums = [3, 22, 44, 53, -56, 21, 89]

largest = nums[0]
n = len(nums)

for i in range(0, n):

    largest = max(largest, nums[i])

print(largest)
