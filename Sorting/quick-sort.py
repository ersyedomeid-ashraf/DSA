"""
Write a program to sort a list of numbers in ascending order using Quick Sort.
"""

nums = [4, 1, 7, 6, 3, 2, 8]


def partition(nums, low, high):

    pivot = nums[low]

    i = low
    j = high

    while i < j:

        while nums[i] <= pivot and i <= high - 1:
            i += 1

        while nums[j] > pivot and j >= low + 1:
            j -= 1

        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    nums[low], nums[j] = nums[j], nums[low]

    return j


def quick_sort(nums, low, high):

    if low < high:

        p_index = partition(nums, low, high)
        quick_sort(nums, low, p_index - 1)
        quick_sort(nums, p_index + 1, high)


quick_sort(nums, 0, len(nums) - 1)
print(nums)


# Another One

nums = [6, 5, 2, 4, 3, 1, 8, 7, 9, 10]


def partition(nums, low, high):

    pivot = nums[low]

    i = low
    j = high

    while i < j:

        while nums[i] <= pivot and i <= high - 1:
            i += 1

        while nums[j] > pivot and j >= low + 1:
            j -= 1

            if i < j:
                nums[i], nums[j] = nums[j], nums[i]

        nums[low], nums[j] = nums[j], nums[low]

        return j


def quick_sort(nums, low, high):

    if low < high:

        p_index = partition(nums, low, high)
        quick_sort(nums, low, p_index - 1)
        quick_sort(nums, p_index + 1, high)


quick_sort(nums, 0, len(nums) - 1)
print(nums)
