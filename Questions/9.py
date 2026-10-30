"""
Write a program to sort a list of numbers in ascending order using Insertion Sort
"""

nums = [40, 10, 30, 20, 5]

n = len(nums)

for i in range(1, n):
    key = nums[i]
    j = i - 1

    while j >= 0 and nums[j] > key:
        nums[j + 1] = nums[j]
        j -= 1

    nums[j + 1] = key

print(nums)


"""
Write a program to sort a list of mobile brands in alphabetical order using Insertion Sort
"""

mobiles = ["Samsung", "Apple", "Vivo", "OnePlus", "Oppo"]

n = len(mobiles)

for i in range(1, n):
    key = mobiles[i]
    j = i - 1

    while j >= 0 and mobiles[j] > key:
        mobiles[j + 1] = mobiles[j]
        j -= 1

    mobiles[j + 1] = key

print(mobiles)
