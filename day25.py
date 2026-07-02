#Log for dreams

dreams = open("dreams.txt", "w")
dreams.write("I dream of a world where no one has to suffer.")
dreams.close()

with open("dreams.txt", "r") as dreams:
    content = dreams.read()
    print(content)


#The Daily Journal Logger

journal = open("journal.txt", "w")
journal.write("Today, I have completed 25 days of my precollege grind. Woohoo!")
journal.close()

with open("journal.txt", "r") as journal:
    entry = journal.read()
    print(entry)

with open("journal.txt", "a") as journal:
    journal.write("I have been committed to my goals so far.")

with open("journal.txt", "r") as journal:
    content = journal.read()
    print(content)

#The Configuration File Parser

settings = open("settings.txt", "w")
settings.write("theme=dark\n")
settings.write("fontsize=14\n")
settings.write("language=English\n")
settings.close()

with open("settings.txt", "r") as settings:
    config = settings.read()
    print(config)


for line in config:
    config.split("\n")
    config_dict = {}
    config_dict["theme"] = "dark"
    config_dict["fontsize"] = 14
    config_dict["language"] = "English"
print(config_dict)


#Custom file creator

filename = input("Enter the filename (with extension): ")
content = input("Enter the content for the file: ")

with open(filename, "w") as custom_file:
    custom_file.write(content)
    
with open(filename, "r") as custom_file:
    file_content = custom_file.read()
    print(file_content)


#Word Counter & Report Generator

sample = open("sample.txt", "w")
sample.write("This is a sample text file. It contains multiple words and sentences for testing purposes.")
sample.close()

with open("sample.txt", "r") as sample:
    text = sample.read()
    word_count = len(text.split())
    character_count = len(text)
    print(f"The word count is {word_count} and the character count is {character_count}.")