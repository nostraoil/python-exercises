def calculate_zone_volume(length_ft, diameter_in):
    # Volume of a cylindrical zone in cubic feet
    radius_ft = diameter_in / 12 / 2
    volume = 3.14159 * radius_ft ** 2 * length_ft
    return volume

zones = [
    {"name": "M1", "length_ft": 50, "diameter_in": 8.5},
    {"name": "M2", "length_ft": 75, "diameter_in": 9.625},
    {"name": "M3", "length_ft": 100, "diameter_in": 10.75},
]

total_volume = 0
for zone in zones:
    volume = calculate_zone_volume(zone["length_ft"], zone["diameter_in"])
    total_volume += volume
    print(f"{zone['name']}: {volume:.2f} cubic ft")

print(f"Total volume: {total_volume:.2f} cubic ft")