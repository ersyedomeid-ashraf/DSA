# Selection Sort Program

"""
Write a porgram to sort a list of car names in alphabetical order using Selection Sort
"""

cars = ["Maruti Suzuki", "BMW", "Audi", "Honda", "Toyota", "Hyundai"]

n = len(cars)

for i in range(n):
    mini_index = i

    for j in range(i + 1, n):
        if cars[j] < cars[mini_index]:
            mini_index = j

    cars[i], cars[mini_index] = cars[mini_index], cars[i]

print(cars)


# Bubble Sort Program

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


# Insertion Sort Program

"""
Write a program to sort a list of numbers in ascending order using Insertion Sort
"""

nums = [40, 10, 30, 20, 5, 4, 34, 3, 5, 65, 76, 67, 89, 22, 34]

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
Write a program to sort a list of subjects in alphabetical order using Insertion Sort
"""

subjects = ["Python", "Maths", "English", "Science", "Hindi", "Java"]

n = len(subjects)

for i in range(1, n):
    key = subjects[i]
    j = i - 1

    while j >= 0 and subjects[j] > key:
        subjects[j + 1] = subjects[j]
        j -= 1

    subjects[j + 1] = key

print(subjects)
