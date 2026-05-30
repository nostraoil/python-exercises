wells = [
    {"name": "Thunder Horse #7", "depth_ft": 18500, "pressure_psi": 12450},
    {"name": "Atlantis #3", "depth_ft": 16200, "pressure_psi": 8200},
    {"name": "Mad Dog #12", "depth_ft": 19800, "pressure_psi": 11800},
    {"name": "Na Kika #5", "depth_ft": 14500, "pressure_psi": 7600}
]

for well in wells:
    print(f"{well['name']} - {well['pressure_psi']} psi")

print("\n--- High Pressure Wells ---")
for well in wells:
    if well["pressure_psi"] > 10000:
        print(f"{well['name']} - {well['pressure_psi']} psi - FLAGGED")

# Add a new field
wells[0]["basin"] = "GoM"
print(wells[0])

#update an existing field
wells[0]["pressure_psi"] = 13000
print(f"Updated pressure: {wells[0]['pressure_psi']} psi")

print(wells[0].keys())
print(wells[0].values())

print(wells[1].get("basin", "unknown"))

mud_weights = [10.0, 11.5, 12.0]
print(f"Starting list: {mud_weights}")

mud_weights.append(13.5)
print(f"After append: {mud_weights}")

mud_weights.pop()
print(f"After pop: {mud_weights}")

print(f"Length: {len(mud_weights)}")

well_location = (28.7361, -88.3672)
print(well_location)
print(well_location[0])
print(well_location[1])

basins_visited = ["GoM", "Permian", "GoM", "Bakken", "Permian", "GoM"]
print(f"All visits: {basins_visited}")

unique_basins = set(basins_visited)
print(f"Unique basins: {unique_basins}")

wells_list = ["Well-1", "Well-2", "Well-3", "Well-4", "Well-5"]
print(wells_list[0:3])
print(wells_list[2:])
print(wells_list[-1])