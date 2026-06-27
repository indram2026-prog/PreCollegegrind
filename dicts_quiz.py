stock = {"Apples" : 27, "Bananas" : 35, "Mangoes" : 63}

for items in stock:
    print(f"{items}")



stock = {"Apples" : 27, "Bananas" : 35, "Mangoes" : 63}

print(stock.get("Apples"))
print(stock.get("Pineapples", "N/A"))


stock = {"Apples" : 27, "Bananas" : 35, "Mangoes" : 63}

stock["Strawberries"] = 25
print(stock)

stock = {"Apples" : 27, "Bananas" : 35, "Mangoes" : 63}

for items in stock:
    print(f"{items}: {stock[items]}")


stock = {"Apples" : 27, "Bananas" : 35, "Mangoes" : 63}
removed = stock.pop("Apples")
print(f"Removed: {removed}")
print(f"Updated stock: {stock}")

students = {"Alice": {"Math": 85, "Science": 90}}
print(students["Alice"]["Math"])

dict = {n: n**2 for n in range(1, 4)}
print(dict)

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged_dict = dict1 | dict2
print(merged_dict)

word = "banana"
letter_count = {}
for letter in word:
    letter_count[letter] = letter_count.get(letter, 0) + 1
print(letter_count)

student = {"name": "Alice", "age": 20, "grade": "A"}
student.setdefault("city", "NYC")
print(student)