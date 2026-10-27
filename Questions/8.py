# Selection Sort Program

"""
Write a porgram to sort a list of car names in alphabetical order using Selection Sort
"""

cars = ["Toyota", "BMW", "Audi", "Honda"]

n = len(cars)

for i in range(n):
    mini_index = i

    for j in range(i + 1, n):
        if cars[j] < cars[mini_index]:
            mini_index = j

    cars[i], cars[mini_index] = cars[mini_index], cars[i]

print(cars)
