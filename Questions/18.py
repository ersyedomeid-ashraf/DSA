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


"""
Write a program to right rotate an array by k positions.
"""

# Optimal Approach (Using Reversal Algorithm)

nums = [3, 9, 5, 6, 7, 2, 10, 9]

n = len(nums)

k = 5
k = k % n


def reverse(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


reverse(nums, n - k, n - 1)
reverse(nums, 0, n - k - 1)
reverse(nums, 0, n - 1)

print(nums)


# Another one

"""
Write a program to right rotate an array by k positions.
"""

# Optimal Approach (Using Reversal Algorithm)

nums = [34, 56, 78, 98, 75, 53, 31, 21, 11, 10]

n = len(nums)

k = 5
k = k % n


def reverse(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


reverse(nums, n - k, n - 1)
reverse(nums, 0, n - k - 1)
reverse(nums, 0, n - 1)

print(nums)


"""
Write a program to right rotate an array by k positions.
"""

# Brute Force Approach

nums = [34, 21, 34, 56, 98, 80, 76, 67, 99]

k = 3

n = len(nums)

rotations = k % n

for _ in range(0, rotations):
    # (_) is used because we don't need the loop variable, only repeat the loop
    e = nums.pop()
    nums.insert(0, e)

print(nums)


# Better Solution (Using Slicing)

nums = [44, 33, 56, 77, 88, 90, 22, 32, 12, 11]

n = len(nums)

k = 5
k = k % n

nums[:] = nums[n - k :] + nums[: n - k]

print(nums)


# Optimal Approach (Using Reversal Algorithm)

nums = [98, 79, 57, 76, 24, 35, 51, 22, 10]

n = len(nums)

k = 5
k = k % n


def reverse(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


reverse(nums, n - k, n - 1)
reverse(nums, 0, n - k - 1)
reverse(nums, 0, n - 1)

print(nums)
