#1st question (split)

batch_code = "BATCH-98432-XYZ"
updated_batch_code= batch_code.split("-")
print(updated_batch_code[1])


#2nd question (find)

sensor_data = "temp:32;status:OK;coords:12.97,77.59"
index_no = sensor_data.find("coords")
print(index_no)

#3rd question (replace)
email = "indrajit@gmail#com"
corrected_email = email.replace("#", ".")
print(corrected_email)

#4th question (split)

games_string = "GTA_V/Genshin_Impact/Valorant"
games = games_string.split("/")
print(games)

#5th question (join)

url_segments = ["user", "settings", "profile"]
url = "/".join(url_segments)
print(url)