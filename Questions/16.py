"""
Write a program to remove duplicates from a sorted array.
"""

nums = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 7, 8, 8, 9, 9, 10, 11, 22, 44]

n = len(nums)

freq_map = {}

for i in range(0, n):
    freq_map[nums[i]] = 0

j = 0

for k in freq_map:
    nums[j] = k
    j += 1

print(j)
print(nums[:j])


# Another one

"""
Write a program to remove duplicates from a sorted array.
"""


nums = [11, 22, 11, 33, 44, 77, 22, 33, 66, 88, 99, 55, 66, 88, 22, 11, 99, 55, 44, 77]

n = len(nums)

freq_map = {}

for i in range(0, n):
    freq_map[nums[i]] = 0

j = 0

for k in freq_map:
    nums[j] = k
    j += 1

print(j)
print(nums[:j])
