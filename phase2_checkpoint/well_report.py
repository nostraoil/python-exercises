import pandas as pd


def load_csv(path):
    try:
        dataframe = pd.read_csv(path)
        return dataframe
    except FileNotFoundError:
        print(f"ERROR: File not found: {path}")
        return None


def report_loaded_data(wells, completions):
    missing_pressure = wells["pressure_psi"].isna().sum()

    print(f"Well rows loaded: {len(wells)}")
    print(f"Completion rows loaded: {len(completions)}")
    print(f"Wells missing pressure_psi: {missing_pressure}")


def filter_high_pressure(wells):
    # NaN > 2000 is False, so wells with missing pressure
    # will not be included in this filtered DataFrame.
    high_pressure_wells = wells[
        wells["pressure_psi"] > 2000
    ]

    print(f"Wells above 2000 psi: {len(high_pressure_wells)}")

    return high_pressure_wells


def report_by_field(wells):
    field_report = wells.groupby("field").agg(
        mean_water_depth_ft=("water_depth_ft", "mean"),
        well_count=("well_id", "count"),
    )

    print("\nHigh-pressure wells grouped by field:")
    print(field_report)


def merge_wells_and_completions(wells, completions):
    merged = pd.merge(wells, completions, on="well_id")

    print(f"\nRows after merge: {len(merged)}")

    return merged


def main():
    wells = load_csv("data/wells_full.csv")
    completions = load_csv("data/completions.csv")

    # Stop if either file could not be loaded.
    if wells is None or completions is None:
        return

    report_loaded_data(wells, completions)

    high_pressure_wells = filter_high_pressure(wells)

    report_by_field(high_pressure_wells)

    merge_wells_and_completions(wells, completions)


if __name__ == "__main__":
    main()