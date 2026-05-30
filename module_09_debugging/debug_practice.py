def calculate_drawdown(reservoir_pressure, flowing_pressure):
    pressure_drop = reservoir_pressure - flowing_pressure
    return pressure_drop

def classify_zone(zone):
    drawdown = calculate_drawdown(
        zone["reservoir_pressure_psi"],
        zone["flowing_pressure_psi"]
    )
    
    if drawdown > 2000:
        risk = "high"
    elif drawdown > 1000:
        risk = "medium"
    else:
        risk = "low"
    
    return {
        "zone": zone["name"],
        "drawdown": drawdown,
        "risk": risk
    }

zones = [
    {"name": "M1", "reservoir_pressure_psi": 9200, "flowing_pressure_psi": 7400},
    {"name": "M2", "reservoir_pressure_psi": 8800, "flowing_pressure_psi": 7100},
    {"name": "M3", "reservoir_pressure_psi": 9500, "flowing_pressure_psi": 7600},
]

results = []
for zone in zones:
    result = classify_zone(zone)
    results.append(result)

print(results)