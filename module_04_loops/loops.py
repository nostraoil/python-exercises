wells = ["Thunderhorse #7", "Atlantis#3", "Mad Dog #12", "Na Kika #5"]
pressures = [12500, 8200, 11800, 7600]

high_pressure_wells = [wells[i] for i in range(len(wells)) if pressures[i] > 10000]
print(high_pressure_wells)