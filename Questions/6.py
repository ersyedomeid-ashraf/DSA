"""
Write a program to sort a list of names in alphabetical order using Insertion Sort.
"""

names = ["Alto", "Slavia", "Virtus", "Bmw"]

n = len(names)

for i in range(1, n):
    key = names[i]
    j = i - 1

    while j >= 0 and names[j] > key:
        names[j + 1] = names[j]
        j -= 1

    names[j + 1] = key

print(names)
