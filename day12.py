#Print the first 10 multiples of a number given by the user.

num = float(input("Pick a number."))
for i in range(1,11):
    print(f"{num} * {i} = {num * i}")

#Count how many times a specific digit appears in a number.

num = input("Pick a number.")
var = input("Pick a digit to count.")
count = 0
for digit in num:
    if digit == var:
        count = count + 1
print(f"The digit {var} appears {count} times in the number {num}.")


#Keep asking the user for numbers until they enter 0, then print the sum of all numbers.
total = 0
while True:
    num = float(input("Pick a number. Enter 0 to stop."))
    if num == 0:
        break
    total = total + num
    print(f"The sum of all numbers entered is {total}.")