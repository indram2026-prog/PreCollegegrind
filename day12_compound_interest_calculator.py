total = float(input("Enter the principal amount."))
num = int(input("Enter the number of years that have passed."))
var = float(input("Enter the interest rate in percentage."))
if total < 0:
    print("The principal amount cannot be negative.")
    exit()
for i in range(num):
    total = total + ((var/100) * total)
print(f"The total amount after {num} years is {total:.2f}.")