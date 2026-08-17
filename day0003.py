grades = {}
amount_of_students = int(input("Enter the number of students: "))

def add_grade(student, grade):
    grades[student] = grade
    return 

for i in range(amount_of_students):
       add_grade(input("Enter student name: "), input("Enter grade: "))

class_average = sum(grades.values()) / len(grades)
highest_grade = max(grades.values())
lowest_grade = min(grades.values())

print(grades)
print(f"The class average is {class_average}.")
print(f"The highest grade is {highest_grade}.")
print(f"The lowest grade is {lowest_grade}.")
