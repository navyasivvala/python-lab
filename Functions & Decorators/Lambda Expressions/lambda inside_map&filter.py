# Task 4: Lambda Inside map() and filter()

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

cubes = list(map(lambda x: x ** 3, numbers))
print(cubes)

divisible = list(filter(lambda x: x % 3 == 0, numbers))
print(divisible)
#[1, 8, 27, 64, 125, 216, 343, 512, 729]
#[3, 6, 9]
