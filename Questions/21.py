"""
Write a program to merge two sorted arrays into a single sorted array without duplicates
"""

nums1 = [1, 1, 1, 2, 4, 6, 7]
nums2 = [1, 2, 3, 5, 6, 7, 8, 9, 10]

n = len(nums1)
m = len(nums2)

result = []

i = 0
j = 0

while i < n and j < m:

    if nums1[i] <= nums2[j]:

        if len(result) == 0 or result[-1] != nums1[i]:
            result.append(nums1[i])
        i += 1

    else:

        if len(result) == 0 or result[-1] != nums2[j]:
            result.append(nums2[j])
        j += 1


while i < n:

    if len(result) == 0 or result[-1] != nums1[i]:
        result.append(nums1[i])
    i += 1

while j < m:

    if len(result) == 0 or result[-1] != nums2[j]:
        result.append(nums2[j])
    j += 1

print(result)


"""
Write a program to merge two sorted arrays into a single sorted array without duplicates
"""

nums1 = [3, 4, 5, 7, 10, 12, 14, 15, 17, 18]
nums2 = [1, 2, 3, 6, 8, 9, 11, 13, 16, 19, 20]

n = len(nums1)
m = len(nums2)

result = []

i = 0
j = 0

while i < n and j < m:

    if nums1[i] <= nums2[j]:

        if len(result) == 0 or result[-1] != nums1[i]:
            result.append(nums1[i])
        i += 1

    else:

        if len(result) == 0 or result[-1] != nums2[j]:
            result.append(nums2[j])
        j += 1


while i < n:

    if len(result) == 0 or result[-1] != nums1[i]:
        result.append(nums1[i])
    i += 1

while j < m:

    if len(result) == 0 or result[-1] != nums2[j]:
        result.append(nums2[j])
    j += 1

print(result)


"""
Write a program to merge two sorted arrays into a single sorted array without duplicates.
"""


names1 = ["Aman", "Deepak", "Rahul", "Rohit"]
names2 = ["Ankit", "Karan", "Raj", "Vijay"]

result = []

i = 0
j = 0

while i < len(names1) and j < len(names2):

    if names1[i] <= names2[j]:
        result.append(names1[i])
        i += 1

    else:
        result.append(names2[j])
        j += 1

while i < len(names1):
    result.append(names1[i])
    i += 1

while j < len(names2):
    result.append(names2[j])
    j += 1

print(result)
