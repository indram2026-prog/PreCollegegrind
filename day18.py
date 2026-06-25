students = {"Alice": {"Maths": 85, "English": 92, "Science": 88},
    "Bob": {"Maths": 78, "English": 81, "Science": 90},
    "Charlie": {"Maths": 92, "English": 89, "Science": 95}}

greatest_avg = 0
total = 0

for names in students:
    avg = sum(students[names].values()) / len(students[names].values())
    print(f"{names}: {avg}")
    total = total + avg

    if avg > greatest_avg:
        greatest_avg = avg
        top_student = names

class_avg = total / len(students)
print(f"Class average: {class_avg}")
print(f"Total students: {len(students)}")
print(f"Top student: {top_student} with average: {greatest_avg}")