pressure_psi = 15000
depth_ft = 1000
basin = "GoM"

if basin == "GoM" and depth_ft > 15000 and pressure_psi > 10000:
    print("Deppwater high pressure - use MST system")
elif basin == "GoM" and depth_ft > 15000:
    print("Deepwater normal pressure - standard completion")
elif basin == "Permian":
    print("Permian basin - land completion")
else:
    print("review well parameters")