students = {
    "Neville": {"Maths": 86, "Science": 92, "English": 75},
    "Nolan": {"Maths": 95, "Science": 89, "English": 97},
    "Alina": {"Maths": 92, "Science": 93, "English": 93},
}


def calculate_average(grades):
    total = sum(grades.values())
    count = len(grades)
    average = total / count
    return average

for student_name in students:
    avg = calculate_average(students[student_name])
    print(f"{student_name}: {avg}")