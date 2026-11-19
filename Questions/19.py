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


"""
Write a program to move all zeros to the end of the list without changing the order of non-zero elements.
"""

# Optimal Solution

nums = [2, 0, 4, 3, 5, 0, 0, 5, 6, 0, 6, 0, 8, 7]


i = 0

while i < len(nums):

    if nums[i] == 0:
        break

    i += 1

j = i + 1

while j < len(nums):

    if nums[j] != 0:
        nums[i], nums[j] = nums[j], nums[i]

        i += 1
    j += 1

print(nums)
