from well import Well, InjectionWell

well_a = Well("AC772 LWX1", 20201, 20102 ,10401, 10.2, 315)
well_b = Well("AC772 LWX4", 20144, 20001, 10355, 10.2, 225)
well_c = Well("AC772 LWX11", 20144, 19128, 10355, 10.6, 205)

MIN_OVERBALANCE_PSI = 150  # operational minimum margin

wells = [well_a, well_b, well_c]
for well in wells:
    margin = well.overbalance_margin()
    if margin < MIN_OVERBALANCE_PSI:
        print(f"WARNING: {well.name} - brine density too low! Margin: {margin:.0f} psi")

for well in wells:
    return_pressure = well.hydrostatic_pressure()
    print(f"{well.name} - return pressure: {return_pressure:.0f} psi")

for well in wells:
    if well.is_high_temp():
        print(f"{well.name} - {well.temperature:.0f} degF [HIGH TEMP]")
    else:
        print(f"{well.name} - {well.temperature:.0f} degF")

inj_well = InjectionWell("AC772 INJ1", 18500, 18400, 9200, 9.5, 245, 8500, "water")


print(inj_well.name)                     # works — inherited from Well
print(inj_well.hydrostatic_pressure())   # works — inherited from Well
print(inj_well.injection_fluid)          # works — defined on InjectionWell
print(inj_well.daily_injection_volume()) # works — defined on InjectionWell


#below are just examples to print the different values of the wells
print(well_a.name)
print(well_b.depth)
print(well_a.density)
print(well_c.pressure)
print(well_b.tvd)

producer = Well("AC772 LWX1", 20201, 20102, 10401, 10.2, 315)
injector = InjectionWell("AC772 INJ1", 18500, 18400, 9200, 9.5, 245, 8500, "water")

print(f"Producer margin: {producer.overbalance_margin():.2f} psi")
print(f"Injector margin: {injector.overbalance_margin():.2f} psi")