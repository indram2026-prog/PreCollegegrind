grades = {}
amount_of_students = int(input("Enter the number of students: "))

def add_grade(student, grade):
    grades[student] = grade
    return 

for i in range(amount_of_students):
       add_grade(input("Enter student name: "), input("Enter grade: "))

print(grades)