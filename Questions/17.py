"""
Write a program to right rotate an array by one position.
"""

# Using Slicing

nums = [5, 4, 6, 7, 3, 2, 1, 8, 9, 10]

n = len(nums)

nums[:] = [nums[-1]] + nums[0 : n - 1]

print(nums)


"""
Write a program to right rotate an array by one position.
"""

# Using Temporary Variable

nums = [5, 4, 6, 7, 3, 2, 1, -9, 10]

n = len(nums)

temp = nums[n - 1]

for i in range(n - 2, -1, -1):
    nums[i + 1] = nums[i]

nums[0] = temp

print(nums)


"""
Write a program to right rotate an array by one position.
"""

# Using Temporary Variable

nums = [2, 3, 1, 4, 6, 8, 9, 6, 10, -2]

n = len(nums)

temp = nums[n - 1]

for i in range(n - 2, -1, -1):
    nums[i + 1] = nums[i]

nums[0] = temp

print(nums)


"""
Write a program to right rotate an array by one position.
"""

# Using Slicing

nums = [22, 3, 44, 11, 55, -44, -6, 56, 87, -21, 72]

n = len(nums)

nums[:] = [nums[-1]] + nums[0 : n - 1]

print(nums)
