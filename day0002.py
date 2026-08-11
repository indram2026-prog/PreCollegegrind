principal = float(input("Enter the principal amount: "))
interest = input("Is your interest simple or compound? (Enter either 's' or 'c'): ")
method = input("Is your rate set monthly or annually? (Enter either 'm' or 'y'): ")

if interest == 'c':
    if method == 'm':
        rate = float(input("Enter the monthly interest rate as percentage: "))
        time = int(input("Enter the time in months: "))
        
        for i in range(time):
            sum = principal + ((rate / 100) * principal)
            principal = sum
        print(f"The total amount after {time} months is: {sum:.2f}.")

    else:
        rate = float(input("Enter the annual interest rate as percentage: "))
        time = int(input("Enter the time in years: "))
        

        for i in range(time):
            sum = principal + ((rate / 100) * principal)
            principal = sum
        print(f"The total amount after {time} years is: {sum:.2f}.")


if interest == 's':
    if method == 'm':
        rate = float(input("Enter the monthly interest rate as percentage: "))
        time = int(input("Enter the time in months: "))
        sum = principal + ((rate / 100) * principal * time)
        print(f"The total amount after {time} months is: {sum:.2f}.")

    else:
        rate = float(input("Enter the annual interest rate as percentage: "))
        time = int(input("Enter the time in years: "))
        sum = principal + ((rate / 100) * principal * time)
        print(f"The total amount after {time} years is: {sum:.2f}.")



        
