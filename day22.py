grades = [35, 85, 42, 55, 38, 92, 40]

pass_grades = (list(filter(lambda x: x >= 40, grades)))
print(pass_grades)

A_grade = (list(filter(lambda x: x >= 90, pass_grades)))

for items in A_grade:
    print(f"{items} = A")

B_grade = (list(filter(lambda x: x >= 80 and x < 90, pass_grades)))

for items in B_grade:
    print(f"{items} = B")

C_grade = (list(filter(lambda x: x >= 70 and x < 80, pass_grades)))

for items in C_grade:
    print(f"{items} = C")


D_grade = (list(filter(lambda x: x >= 60 and x < 70, pass_grades)))

for items in D_grade:
    print(f"{items} = D")

F_grade = (list(filter(lambda x: x < 60, pass_grades)))

for items in F_grade:
    print(f"{items} = F")


grades = [35, 85, 42, 55, 38, 92, 40]

grade_lambda = lambda x: x >= 40
letter_lambda = lambda x: 'A' if x >= 90 else( 'B' if x >= 80 else( 'C' if x >= 70 else( 'D' if x >= 60 else('F') )))

result = list(map(letter_lambda, filter(grade_lambda, grades)))
print(result)

