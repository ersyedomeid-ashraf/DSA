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


# Merge Sort Program


"""
Write a program to sort a list of numbers in ascending order using Merge Sort.
"""

nums = [3, 22, 5, 1, 2, 7, 55, 4, 34, 67, 65, 90, 72]


def merge_array(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge_array(left_half, right_half)


print(merge_sort(nums))


"""
Write a program to sort mobile brands alphabetically using Merge Sort
"""

mobiles = ["Vivo", "Samsung", "Apple", "Oppo", "OnePlus"]


def merge_array(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge_array(left_half, right_half)


print(merge_sort(mobiles))


# Quick Sort Program

"""
Write a program to sort a list of cities in alphabetical order using Quick Sort.
"""

cities = ["Delhi", "Agra", "Mumbai", "Jaipur", "Chennai", "Bhopal", "Kolkata", "Pune"]


def partition(cities, low, high):

    pivot = cities[low]

    i = low
    j = high

    while i < j:

        while cities[i] <= pivot and i <= high - 1:
            i += 1

        while cities[j] > pivot and j >= low + 1:
            j -= 1

        if i < j:
            cities[i], cities[j] = cities[j], cities[i]

    cities[low], cities[j] = cities[j], cities[low]

    return j


def quick_sort(cities, low, high):

    if low < high:

        p_index = partition(cities, low, high)
        quick_sort(cities, low, p_index - 1)
        quick_sort(cities, p_index + 1, high)


quick_sort(cities, 0, len(cities) - 1)
print(cities)
