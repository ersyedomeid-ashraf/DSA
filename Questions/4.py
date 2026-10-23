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


names = ["Zoya", "Huzaifa", "Fairy", "Neha"]

selection_sort(names)

print(names)


"""
Write a program to sort a list of fruits in alphabetical order using Selection Sort.
"""


def selection_sort(fruits):
    n = len(fruits)

    for i in range(0, n):
        mini_index = i

        for j in range(i + 1, n):
            if fruits[j] < fruits[mini_index]:
                mini_index = j

        fruits[i], fruits[mini_index] = fruits[mini_index], fruits[i]


fruits = ["Mango", "Apple", "Banana", "Orange"]

selection_sort(fruits)

print(fruits)
