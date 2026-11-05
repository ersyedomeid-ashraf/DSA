"""
Write a program to sort a list of mobile brands in alphabetical order using Quick Sort.
"""

brands = ["Samsung", "Apple", "Vivo", "OnePlus", "Oppo", "Realme", "Xiaomi", "Nokia"]


def partition(brands, low, high):

    pivot = brands[low]

    i = low
    j = high

    while i < j:

        while brands[i] <= pivot and i <= high - 1:
            i += 1

        while brands[j] > pivot and j >= low + 1:
            j -= 1

        if i < j:
            brands[i], brands[j] = brands[j], brands[i]

    brands[low], brands[j] = brands[j], brands[low]

    return j


def quick_sort(brands, low, high):

    if low < high:

        p_index = partition(brands, low, high)
        quick_sort(brands, low, p_index - 1)
        quick_sort(brands, p_index + 1, high)


quick_sort(brands, 0, len(brands) - 1)
print(brands)
