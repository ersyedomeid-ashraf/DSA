"""
Write a program to move all zeros to the end of the list without changing the order of non-zero elements.
"""

# Brute Force Approach

nums = [1, 0, 2, 4, 3, 0, 0, 3, 5, 1]

n = len(nums)
temp = []

for i in range(0, n):

    if nums[i] != 0:
        temp.append(nums[i])


nz = len(temp)

for i in range(0, nz):
    nums[i] = temp[i]

for i in range(nz, n):
    nums[i] = 0

print(nums)
