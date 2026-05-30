def hydrostatic_pressure(depth_ft, mud_weight_ppg=10.0):
    """Calculate hydrostatic pressure in psi.

    depth_ft: measure depth in feet
    mud_weight_ppg: mud weight in lbs/gal (default 10.0)
    """

    pressure = .052 *mud_weight_ppg*depth_ft
    return pressure

result = hydrostatic_pressure(18000, 12.5)
print(result)
