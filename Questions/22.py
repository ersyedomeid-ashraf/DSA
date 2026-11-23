# Revision

"""
Write a program to sort a list of names in alphabetical order using Selection Sort.
"""


def selection_sort(names):
    n = len(names)

    for i in range(0, n):
        mini_index = i

        for j in range(i + 1, n):
            if names[j] < names[mini_index]:
                mini_index = j

        names[i], names[mini_index] = names[mini_index], names[i]


names = ["Shahid", "Rahul", "Zayn", "Arpit", "Narendra", "Amit", "Kaif"]

selection_sort(names)

print(names)


"""
Write a program to sort a list of numbers in ascending order using Bubble Sort
"""

nums = [40, 12, 64, 56, 78, 98, 76, 45, 32, 234, 10, 30, 20, 5]

n = len(nums)

for i in range(n - 2, -1, -1):
    for j in range(0, i + 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print(nums)
