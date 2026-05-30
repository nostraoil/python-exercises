well = {
    "name": "Thunder Horse #7",

    "water_depth_ft": 6200,
    "bottomhole_temperature_f": 245,
    "bottomhole_pressure_psi": 13200,
    "completion_brine": "14.2 ppg CaBr2",
    "pbtd_ft": 18450,
    "drill_pipe_plan": "5 in drill pipe to 18,000 ft",

    "casing_strings": [
        {
            "name": "Surface casing",
            "size_in": 13.375,
            "weight_ppf": 72,
            "top_md_ft": 0,
            "bottom_md_ft": 8500,
        },
        {
            "name": "Production casing",
            "size_in": 9.625,
            "weight_ppf": 53.5,
            "top_md_ft": 8500,
            "bottom_md_ft": 16000,
        },
    ],

    "zones": [
        {
            "name": "Zone A",
            "measured_depth_ft": 16200,
            "true_vertical_depth_ft": 15850,
        },
        {
            "name": "Zone B",
            "measured_depth_ft": 17100,
            "true_vertical_depth_ft": 16675,
        },
    ],
}

print(f"Well: {well['name']}")
print(f"Water depth: {well['water_depth_ft']} ft")
print(f"BHT: {well['bottomhole_temperature_f']}°F")
print()

print("Casing strings:")
for casing in well["casing_strings"]:
    print(f"  - {casing['name']}: {casing['size_in']} in, {casing['weight_ppf']} ppf, {casing['top_md_ft']}-{casing['bottom_md_ft']} ft")

print()
print("Zones:")
for zone in well["zones"]:
    print(f"  - {zone['name']}: MD {zone['measured_depth_ft']} ft, TVD {zone['true_vertical_depth_ft']} ft")