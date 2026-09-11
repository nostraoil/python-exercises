from wells_tools import load_wells, high_pressure

wells = load_wells("data/wells.csv")
hp = high_pressure(wells)
print(f"{len(hp)} of {len(wells)} wells above 2000 psi")