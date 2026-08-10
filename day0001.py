weight = float(input("Enter your weight in kgs: "))
height = float(input("Enter your height in meters: "))

BMI = weight / (height * height)

if BMI < 18.5:
    print(f"You are underweight. Your BMI is {BMI}. Please eat more and exercise regularly. Take care.")

elif BMI >= 18.5 and BMI < 24.9:
    print(f"You have a normal weight. Your BMI is {BMI}. Keep up the good work and maintain a healthy lifestyle. :) ")

else:
    print(f"You are overweight. Your BMI is {BMI}. Please consider a healthy diet and regular exercise. Take care.")