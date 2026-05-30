def get_completion_summary(well_name, zones):
    summary = {
        "well": well_name,
        "zone_count": len(zones),
        "total_perforations": 0,
        "high_risk_zones": [],
        "unmeasured_zones": []   # new field
    }
    
    for zone in zones:
        summary["total_perforations"] += zone["perforations"]
        
        if "pressure_psi" not in zone:
            summary["unmeasured_zones"].append(zone["name"])
            continue   # skip the high-risk check for this zone
        
        if zone["pressure_psi"] > 9000:
            summary["high_risk_zones"].append(zone["name"])
    
    return summary


wells = {
    "AC-857-X1": [
        {"name": "M1", "perforations": 24, "pressure_psi": 9200},
        {"name": "M2", "perforations": 32, "pressure_psi": 8800},
        {"name": "M3", "perforations": 18, "pressure_psi": 9500},
    ],
    "AC-857-X2": [
        {"name": "U1", "perforations": 28, "pressure_psi": 7800},
        {"name": "U2", "perforations": 22},
        {"name": "U3", "perforations": 30, "pressure_psi": 8500},
    ],
}

for well_name, zones in wells.items():
    summary = get_completion_summary(well_name, zones)
    print(summary)