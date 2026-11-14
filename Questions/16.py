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


"""
Write a program to remove duplicates from a unsorted array.
"""

nums = [6, 5, 6, 7, 8, 9, 8, 7, 5, 4, 3, 1, 2, 1, 3, 4, 5, 9, 8, 7, 6, 8, 9, 10]

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

nums = [66, 55, 22, 66, 55, 33, 22, 88, 22, 3, 11, 44, 66, 77, 55]

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
