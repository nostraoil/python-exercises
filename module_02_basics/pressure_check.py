pressure_psi = 3000

if pressure_psi > 10000:
    print("WARNING: High pressure")
elif pressure_psi > 5000:
    print("pressure is normal")
else:
    print("Low pressure - check well")