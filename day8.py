sentence = input("Enter a sentence: ")
count = 0
for letters in sentence:
    if letters in "aeiouAEIOU":
        count = count + 1
print(f"Number of vowels in the sentence is {count}")