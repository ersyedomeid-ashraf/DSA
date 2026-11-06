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


"""
Write a program to sort a list of programming languages in alphabetical order using Quick Sort.
"""

languages = [
    "Python",
    "Java",
    "C++",
    "JavaScript",
    "C",
    "HTML",
    "CSS",
]


def partition(languages, low, high):

    pivot = languages[low]

    i = low
    j = high

    while i < j:

        while languages[i] <= pivot and i <= high - 1:
            i += 1

        while languages[j] > pivot and j >= low + 1:
            j -= 1

        if i < j:
            languages[i], languages[j] = languages[j], languages[i]

    languages[low], languages[j] = languages[j], languages[low]

    return j


def quick_sort(languages, low, high):

    if low < high:

        p_index = partition(languages, low, high)
        quick_sort(languages, low, p_index - 1)
        quick_sort(languages, p_index + 1, high)


quick_sort(languages, 0, len(languages) - 1)
print(languages)
