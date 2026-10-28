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


"""
Write a porgram to sort a list of fruit names in alphabetical order using Selection Sort
"""

fruit = ["Pinepapple", "Mango", "Grapes", "Apple", "Orange", "Banana"]

n = len(fruit)

for i in range(n):
    mini_index = i

    for j in range(i + 1, n):
        if fruit[j] < fruit[mini_index]:
            mini_index = j

    fruit[i], fruit[mini_index] = fruit[mini_index], fruit[i]

print(fruit)


# Bubble Sort Program

"""
Write a program to sort a list of numbers in ascending order using Bubble Sort
"""

nums = [40, 10, 30, 20, 5]

n = len(nums)

for i in range(n - 2, -1, -1):
    for j in range(0, i + 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print(nums)


"""
Write a program to sort a list of mobile brands in alphabetical order using Bubble Sort
"""

mobiles = ["Samsung", "Apple", "Vivo", "OnePlus", "Oppo"]

n = len(mobiles)

for i in range(n - 2, -1, -1):
    for j in range(0, i + 1):
        if mobiles[j] > mobiles[j + 1]:
            mobiles[j], mobiles[j + 1] = mobiles[j + 1], mobiles[j]

print(mobiles)
