


number = float(input("Pick a number: "))

cube = lambda x: x ** 3
print(cube(number))


numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x ** 2, numbers))
print(result)

grades = [35, 85, 42, 55, 38, 92, 40]

result = list(filter(lambda x: x >= 40, grades))
print(result)