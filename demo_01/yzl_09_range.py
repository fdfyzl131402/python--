numbers = list(range(1, 20, 2))
print(numbers)

number = list(range(3, 31))
for even_number in range(3, 31, 3):
    print(even_number)

num = []
for cube in range(1, 11):
    cubes = cube**3
    num.append(cubes)
print(num)

num_two = [value**3 for value in range(1, 11)]
print(num_two)