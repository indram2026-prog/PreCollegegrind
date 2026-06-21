


patients = {"Alice": 130, "Bruce": 150, "Kratos": 190, "Delta": 130, "Helios": 140}
print(patients["Alice"])
patients["Diana"] = 115
for name in patients:
    print(f"{name} = {patients[name]}")