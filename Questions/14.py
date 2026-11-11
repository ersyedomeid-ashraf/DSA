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


"""
Write a program to find the second largest element in an array using Better Solution
"""

nums = [
    24,
    58,
    91,
    634,
    334,
    565,
    787,
    989,
    909,
    87,
    86,
    543,
    224,
    76,
    39,
    82,
    95,
    47,
    63,
    18,
    71,
    86,
]

largest = float("-infinity")
second_largest = float("-infinity")

n = len(nums)

for i in range(0, n):
    largest = max(largest, nums[i])

for i in range(0, n):
    if nums[i] > second_largest and nums[i] != largest:
        second_largest = nums[i]

print(second_largest)


"""
Write a program to find the second largest element in an array using Optimal Solution
"""

nums = [964, 873, 299, 745, 693, 416, 827, 859, 972]

largest = float("-infinity")
second_largest = float("-infinity")

n = len(nums)

for i in range(0, n):

    if nums[i] > largest:
        second_largest = largest
        largest = nums[i]

    elif nums[i] > second_largest and nums[i] != largest:
        second_largest = nums[i]

print(second_largest)
