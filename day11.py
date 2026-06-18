for i in range(1,5):
    for j in range(4):
        print("*", end="")
print()


for i in range(1,5):
    for j in range(i):
        print("*", end="")
    print()


for i in range(1,5):
    for j in range(5-i):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()


for i in range(5,0, -1):
    for j in range(i):
        print("*", end="")
    print()

for i in range(1,5):
    for j in range(1, i + 1):
        print(j, end="")
    print()


for i in range(1,5):
    for j in range(4 - i, 0, -1):
        print(" ", end=" ")

    for j in range(1, i + 1):
        print(j, end=" ")

    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()

