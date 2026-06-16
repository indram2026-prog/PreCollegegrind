greatest = 0
total = 0
smallest = 0

for i in range(5):
    num = float(input("Enter a number."))

    total = total + num

    if i == 0:
        greatest = num
        smallest = num

    else:
        if num > greatest:
            greatest = num

        if num < smallest:
            smallest = num

    avg = total / 5

    print(f"Greatest: {greatest}")
    print(f"Smallest: {smallest}")
    print(f"Average: {avg}")
    print(f"Total: {total}")