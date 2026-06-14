#P1. Print every other number from 1 to 10 (1, 3, 5, 7, 9).

for i in range(1, 11, 2):
    print(f"{i}")

#P2.Ask for a number, print its times table (1 to 10)

number = float(input("Enter a number."))
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")

#P3. Count down from 10 to 1

for i in range(10, 0, -1):
    print(f"{i}")

#P4. Print squares of numbers 1 to 5.

for i in range(1, 6):
    print(f"{i} squared is {i ** 2}")

#P5. Sum all numbers from 1 to 100 and print the result
total = 0 
for i in range(1,101): 
    total = total + i 
    print(f"{total} + {i} = {total + i}")

#P6. Ask for 5 numbers, find and print the largest.
greatest = 0
for i in range(5):
    number = float(input("Enter a number."))
    if number > greatest:
        greatest = number

print(f"{greatest} is the greatest number.")