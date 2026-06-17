# This is me practising my first while loop in python.

num = 1000
while num > 159:
    print(f"{num}")
    num = num - 10


# My first loop including break and continue statements.

for i in range(1,99):
    if i % 3 == 0:
        continue

    if i > 97:
        break
    print(f"{i}")