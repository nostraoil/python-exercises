def get_zones_by_risk(zones, risk_threshold_psi):
    high_risk = []
    for zone in zones:
        if zone["pressure_psi"] >= risk_threshold_psi:
            high_risk.append(zone)
    return high_risk


def calculate_average_drawdown(zones):
    drawdowns = []
    for zone in zones:
        dd = zone["reservoir_pressure_psi"] - zone["flowing_pressure_psi"]
        drawdowns.append(dd)
    return sum(drawdowns) / len(drawdowns)


zones = [
    {"name": "M1", "pressure_psi": 9200, "reservoir_pressure_psi": 9200, "flowing_pressure_psi": 7400},
    {"name": "M2", "pressure_psi": 8800, "reservoir_pressure_psi": 8800, "flowing_pressure_psi": 7100},
    {"name": "M3", "pressure_psi": 7500, "reservoir_pressure_psi": 7500, "flowing_pressure_psi": 6800},
]

high_risk_zones = get_zones_by_risk(zones, 10000)
if high_risk_zones:
    avg_drawdown = calculate_average_drawdown(high_risk_zones)
    print(f"Average drawdown in high-risk zones: {avg_drawdown:.0f} psi")
else:
    print("No high-risk zones found.")