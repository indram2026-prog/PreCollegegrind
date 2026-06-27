def temperature(C): 
    F = (C * 9/5) + 32 
    return F 

fahrenheit = temperature(0) 
print(fahrenheit) 

fahrenheit = temperature(36)
print(fahrenheit)

fahrenheit = temperature(100)
print(fahrenheit)


def grade(n):
    if n >= 40:
        return True
    else:
        return False
    
result1 = grade(75)
print(result1)

result2 = grade(39)
print(result2)

result3 = grade(52)
print(result3)

def function(word):
    result0 = word[: :-1]
    return result0

end1 = function("hello")
print(end1)

end2 = function("goodbye")
print(end2)

end3 = function("dancing")
print(end3)


def analyze_grades(grades):
    highest = max(grades)
    lowest = min(grades)
    average = sum(grades) / len(grades)
    result4 = {"Highest" : highest, "Lowest" : lowest, "Average" : average}
    return result4

ending1 = analyze_grades([89,64,75])
print(ending1)

ending2 = analyze_grades([94,60,80])
print(ending2)

ending3 = analyze_grades([97,65,83])
print(ending3)
  



