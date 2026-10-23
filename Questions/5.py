"""
Write a program to sort a list of names in alphabetical order using Bubble Sort.
"""

names = ["Sahil", "Aman", "Ravi", "Ravindra"]

n = len(names)

for i in range(n - 2, -1, -1):
    for j in range(0, i + 1):
        if names[j] > names[j + 1]:
            names[j], names[j + 1] = names[j + 1], names[j]

print(names)
