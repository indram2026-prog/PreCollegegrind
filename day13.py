# Day 13: Lists - store and manipulate student grade data

names = [ ]
grades = [ ]

for i in range(5):
    names.append(input("Student's name: "))
    grades.append(float(input("Student's grade: ")))
greatest = max(grades)
smallest = min(grades)
average = sum(grades) / 5
    
print(f"{greatest} is the highest grade and {smallest} is the lowest grade. {average} is the average grade.")