"""
Write a program to right rotate an array by k positions.
"""

# Brute Force Approach

nums = [3, 5, 1, 2, 7, 8, 9, 6, 4]

k = 3

n = len(nums)

rotations = k % n

for _ in range(0, rotations):
    # (_) is used because we don't need the loop variable, only repeat the loop
    e = nums.pop()
    nums.insert(0, e)

print(nums)


# Another one

# Brute Force Approach

nums = [6, 5, 4, 7, 8, 9, 2, 3, 1, 10]

k = 3

n = len(nums)

rotations = k % n

for _ in range(0, rotations):
    # (_) is used because we don't need the loop variable, only repeat the loop
    e = nums.pop()
    nums.insert(0, e)

print(nums)


"""
Write a program to right rotate an array by k positions
"""

# Better Solution (Using Slicing)

nums = [3, 9, 5, 6, 7, 2, 10, 9]

n = len(nums)

k = 5
k = k % n

nums[:] = nums[n - k :] + nums[: n - k]

print(nums)


# Another one

# Better Solution

nums = [12, 32, 79, 86, 75, 67, 30, 20, 77]

n = len(nums)

k = 5
k = k % n

nums[:] = nums[n - k :] + nums[: n - k]

print(nums)
