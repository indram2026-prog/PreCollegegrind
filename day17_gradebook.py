students = {"Alice": {"Maths": 85, "English": 92, "Science": 88},
    "Bob": {"Maths": 78, "English": 81, "Science": 90},
    "Charlie": {"Maths": 92, "English": 89, "Science": 95}}
greatest_avg = 0
for names in students:
    avg = sum(students[names].values()) / 3
    print(f"{names}: {avg}")
    
    if avg > greatest_avg:
        greatest_avg = avg
        top_student = names
print(f"Top student: {top_student} with average: {greatest_avg}")
