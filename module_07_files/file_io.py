high_pressure_wells = []

with open("wells.csv", "r") as file:
    next(file)   #skip the header row
    for line in file:
        fields = line.strip().split(",")
        if int(fields[3]) > 10000:
            high_pressure_wells.append(line.strip())

with open("high_pressure.csv", "w") as file:
    file.write("name,basin,depth_ft,pressure_psi\n")
    for well in high_pressure_wells:
        file.write(well + "\n")

print("High pressure wells saved to high_pressure.csv")

import json

with open("wells.json", "r") as file:
    data = json.load(file)

print(data)
print("---")
print(type(data))
print("---")
for well in data ["wells"]:
    print(well["name"])

new_well = {
    "name": "Perdido #9",
    "basin": "GoM",
    "depth_ft": 22000,
    "pressure_psi": 13500
}

data["wells"].append(new_well)

with open("wells.json", "w") as file:
    json.dump(data, file, indent=2)

print("Added new well to wells.json")