"""
Write a program to right rotate an array by k positions.
"""

nums = [3, 5, 1, 2, 7, 8, 9, 6, 4]

k = 3

n = len(nums)

rotations = k % n

for _ in range(0, rotations):
    # (_) is used because we don't need the loop variable, only repeat the loop
    e = nums.pop()
    nums.insert(0, e)

print(nums)
