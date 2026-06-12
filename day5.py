bacteria = int(input("How much bacteria is present in the petri dish?"))
hours = int(input("How many hours have passed since the bacteria was placed in the petri dish?"))
final = bacteria * (2 ** hours)
print(f"After {hours} hours, there will be {final} bacteria in the dish.")
