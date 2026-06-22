player_info = ("Alex", 25,)
inventory = {"sword": 1, "chestplate": 1, "pickaxe": 1}
print(inventory["sword"])
inventory["axe"] = 1
for item in inventory:
    print(f"{item}: {inventory[item]}")

visited_zones = {"badlands", "nether", "end" , "badlands"}
print(visited_zones)

visited_zones.add("overworld")
print(visited_zones)