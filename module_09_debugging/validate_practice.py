def validate_raw_zones(raw_zones):
    """Validate raw zone data. Returns a list of error messages."""
    errors = []
    
    for i, zone in enumerate(raw_zones):
        if "name" not in zone:
            errors.append(f"row {i + 1}: missing name")
    
        if "depth_ft" not in zone:
            errors.append(f"row {i + 1}: missing depth_ft")
        else:
            try:
                int(zone["depth_ft"])
            except ValueError:
                errors.append(f"row {i + 1}: unparseable depth_ft: {zone['depth_ft']!r}")

        if "pressure_psi" not in zone:
            errors.append(f"row {i + 1}: missing pressure_psi")
        else:
            try:
                float(zone["pressure_psi"])
            except ValueError:
                errors.append(f"row {i + 1}: unparseable pressure_psi: {zone['pressure_psi']!r}")

    return errors



test_data = [
    {"name": "M1", "depth_ft": "18500", "pressure_psi": "9200.77"},
    {"depth_ft": "19200", "pressure_psi": "8800"},
    {"name": "M3", "depth_ft": "21500", "pressure_psi": "10500"},
    {"name": "M4", "pressure_psi": "9800"},    #missing depth_ft
    {"name": "M5", "depth_ft": "N/A", "pressure_psi": "8500"},
    {"name": "M6", "depth_ft": "21400", "pressure_psi": "N/A"},
]

result = validate_raw_zones(test_data)
print(result)