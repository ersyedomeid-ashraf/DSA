# 1. O(1) - Constant Time


numbers = [10, 20, 30, 40, 50]
print(numbers[0])


# 2. O(n) - Linear Time


numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)


# 3. O(n²) — Quadratic Time


numbers = [1, 2, 3]

for i in numbers:
    for j in numbers:
        print(i, j)


# Another one


# 1. O(1) - Constant Time
numbers = [15, 25, 35, 45, 55]
print(numbers[0])


# 2. O(n) - Linear Time
numbers = [12, 24, 36, 48, 60]
for number in numbers:
    print(number)


# 3. O(n²) - Quadratic Time
numbers = [2, 4, 6]
for i in numbers:
    for j in numbers:
        print(i, j)
