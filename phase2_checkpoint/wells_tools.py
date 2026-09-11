import csv

MIN_PRESSURE = 2000

def load_wells(path):
    wells = []
    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                row["pressure_psi"] = float(row["pressure_psi"])
            except ValueError:
                continue
            wells.append(row)
    return wells

def high_pressure(wells):
    return [w for w in wells if w["pressure_psi"] > MIN_PRESSURE]

if __name__ == "__main__":
    wells = load_wells("data/wells.csv")
    print(f"Loaded {len(wells)} wells")