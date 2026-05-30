# Messy version - everything in one big script
well1_name = "Thunder Horse #7"
well1_depth = 18500
well1_mud_weight = 13.0
well1_pressure = 0.052 * well1_mud_weight * well1_depth
print(f"{well1_name}: {well1_pressure} psi")

well2_name = "Atlantis #3"
well2_depth = 16200
well2_mud_weight = 12.5
well2_pressure = 0.052 * well2_mud_weight * well2_depth
print(f"{well2_name}: {well2_pressure} psi")

well3_name = "Mad Dog #12"
well3_depth = 19800
well3_mud_weight = 13.5
well3_pressure = 0.052 * well3_mud_weight * well3_depth
print(f"{well3_name}: {well3_pressure} psi")

def calculate_pressure(depth, mud_weight):
    return 0.052 * mud_weight * depth

#cleaner version of above below, defined a data structure and looped through it

wells = [
    {
        "name": "Thunder Horse #7",
        "depth": 18500,
        "mud_weight": 13.0,
    },
    {
        "name": "Atlantis #3",
        "depth": 16200,
        "mud_weight": 12.5,
    },
    {
        "name": "Mad Dog #12",
        "depth": 19800,
        "mud_weight": 13.5,
    },
    {
    "name": "Spraberry #21",
    "depth": 9500,
    "mud_weight": 11.0,
    },
]


for well in wells:
    pressure = calculate_pressure(well["depth"], well["mud_weight"])
    print(f"{well['name']}: {pressure} psi")
