# False values - these all evaluate to False in an if statement
if 0:
    print("0 is truthy")
else:
    print("0 is falsy")

if "":
    print("empty string is truthy")
else:
    print("empty string is falsy")
if []:
    print("empty list is truthy")
else:
    print("empty list is falsy")

if None:
    print("None is truthy")
else:
    print("None is falsy")

# Truthy values
if 1:
    print("1 is truthy")

if "anything":
    print("non-empty string is truthy")

if [1, 2]:
    print("non-empty list is truthy")

wells_list = ["Thunder Horse", "Atlantis"]
empty_list = []

if wells_list:
    print(f"Got {len(wells_list)} wells")

if empty_list:
    print("This won't print")
else:
    print("Empty list - nothing to process")

#same as line 58 and below
pressure = 12000
basin = "GoM"
depth = 18000

if pressure > 10000:
    if basin == "GoM":
        if depth > 15000:
            print("Deepwater high pressure GoM well - use MZST")
        else:
            print("Shallow high pressure GoM well")
    else:
        print("High pressure non-GoM well")
else:
    print("Normal pressure well")

#same as above
if pressure > 10000 and basin == "GoM" and depth > 15000:
    print("Deepwater high pressure GoM well - use MZST")
elif pressure > 10000 and basin == "GoM":
    print("Shallow high pressure GoM well")
elif pressure > 10000:
    print("High pressure non-GoM well")
else:
    print("Normal pressure well")

#module 2.3 below

print("--- break example ---")
pressures = [8000, 9500, 12500, 7000, 6000]

for p in pressures:
    if p > 10000:
        print(f"Found high pressure: {p} - stopping search")
        break
    print(f"Checked: {p}")

print("--- continue example ---")
pressures = [8000, 9500, 12500, 7000, 6000]

for p in pressures:
    if p > 10000:
        continue
    print(f"Processing safe pressure: {p}")

print("--- nested loops ---")
basins = ["GoM", "Permian"]
years = [2024, 2025]

for basin in basins:
    for year in years:
        print(f"{basin} - {year}")

#starting 2.5 gaps

def calculate_volume(length, width, height):
    return length * width * height

# Positional - depends on order
v1 = calculate_volume(10, 5, 3)
print(f"Positional: {v1}")

# Keyword - explicit, order doesn't matter
v2 = calculate_volume(width=5, height=3, length=10)
print(f"Keyword: {v2}")

# Mixed - positional first, then keyword
v3 = calculate_volume(10, height=3, width=5)
print(f"Mixed: {v3}")

#lambda functions

# regular function
def double(x):
    return x * 2

#same thing as a lambda

double_lambda = lambda x: x * 2

print(double(5))
print(double_lambda(5))

wells = [
    {"name": "Thunder Horse", "pressure": 12450},
    {"name": "Atlantis", "pressure": 8200},
    {"name": "Mad Dog", "pressure": 11800}
]

# Sort by pressure using a lambda
sorted_wells = sorted(wells, key=lambda w: w["pressure"])

for well in sorted_wells:
    print(f"{well['name']}: {well['pressure']}")

import pandas as pd

# Same data, two structures

# As a list of dictionaries (vanilla Python)
wells_list = [
    {"name": "Thunder Horse #7", "basin": "GoM", "pressure_psi": 12450},
    {"name": "Atlantis #3", "basin": "GoM", "pressure_psi": 8200},
    {"name": "Mad Dog #12", "basin": "GoM", "pressure_psi": 11800},
]

# As a DataFrame (pandas)
wells_df = pd.DataFrame(wells_list)

print("List of dicts:")
print(wells_list)
print()
print("DataFrame:")
print(wells_df)

import pandas as pd

df = pd.read_csv("wells.csv")

# Select one column - returns a Series (single column)
print("Just the pressures:")
print(df["pressure_psi"])
print()

# Select multiple columns - returns a smaller DataFrame
print("Names and pressures only:")
print(df[["name", "pressure_psi"]])
print()

# Sort by a column
print("Sorted by pressure (ascending):")
print(df.sort_values("pressure_psi"))
print()

# Sort descending
print("Sorted by pressure (descending):")
print(df.sort_values("pressure_psi", ascending=False))