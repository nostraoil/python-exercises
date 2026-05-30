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


def parse_zone_data(raw_zone):
    """Parse a raw zone dictionary into a clean format."""
    return {
        "name": raw_zone["name"],
        "depth_ft": int(raw_zone["depth_ft"]),
        "pressure_psi": float(raw_zone["pressure_psi"]),
        "completion_type": raw_zone.get("completion_type", "standard")
    }


def classify_completion(zone):
    """Classify completion difficulty based on depth and pressure."""
    if zone["depth_ft"] > 20000 and zone["pressure_psi"] > 10000:
        return "ultra-deep HPHT"
    elif zone["depth_ft"] > 15000 or zone["pressure_psi"] > 9000:
        return "deep or high-pressure"
    else:
        return "standard"


def summarize_well(well_name, raw_zones):
    """Build a summary of a well from raw zone data."""
    parsed_zones = []
    for raw in raw_zones:
        parsed = parse_zone_data(raw)
        parsed_zones.append(parsed)
    
    classifications = []
    for zone in parsed_zones:
        classification = classify_completion(zone)
        classifications.append(classification)
    
    return {
        "well": well_name,
        "zone_count": len(parsed_zones),
        "classifications": classifications,
        "max_pressure": max(z["pressure_psi"] for z in parsed_zones),
        "avg_depth": sum(z["depth_ft"] for z in parsed_zones) / len(parsed_zones)
    }


raw_data = [
    {"name": "M1", "depth_ft": "18,500", "pressure_psi": "9200", "completion_type": "sand control"},
    {"depth_ft": "19200", "pressure_psi": "8800"},
    {"name": "M3", "depth_ft": "21500", "pressure_psi": "10500", "completion_type": "HPHT"},
    {"name": "M4", "depth_ft": "1780O", "pressure_psi": "N/A"},
]

errors = validate_raw_zones(raw_data)

if errors:
    print("Cannot process well — validation failed:")
    for error in errors:
        print(f"  - {error}")
else:
    summary = summarize_well("AC-857-X1", raw_data)
    print(summary)