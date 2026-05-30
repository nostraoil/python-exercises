def get_zone_by_name(zones, name):
    for zone in zones:
        if zone["name"] == name:
            return zone

def calculate_drawdown(reservoir_pressure, flowing_pressure):
    return reservoir_pressure - flowing_pressure

def evaluate_zone(zones, zone_name):
    zone = get_zone_by_name(zones, zone_name)
    drawdown = calculate_drawdown(
        zone["reservoir_pressure_psi"],
        zone["flowing_pressure_psi"]
    )
    return {
        "zone": zone_name,
        "drawdown_psi": drawdown,
        "needs_sand_control": drawdown > 1500
    }

def evaluate_well(well, zones_to_check):
    results = []
    for zone_name in zones_to_check:
        result = evaluate_zone(well["zones"], zone_name)
        results.append(result)
    return results

well = {
    "name": "AC-857-X1",
    "zones": [
        {"name": "M1", "reservoir_pressure_psi": 9200, "flowing_pressure_psi": 7400},
        {"name": "M2", "reservoir_pressure_psi": 8800, "flowing_pressure_psi": 7100},
        {"name": "M3", "reservoir_pressure_psi": 9500, "flowing_pressure_psi": 7600},
    ]
}

zones_to_evaluate = ["M1", "M2", "M4"]

results = evaluate_well(well, zones_to_evaluate)

for r in results:
    print(f"{r['zone']}: drawdown {r['drawdown_psi']} psi, sand control: {r['needs_sand_control']}")