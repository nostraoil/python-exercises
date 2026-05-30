import pandas as pd

df = pd.read_csv("wells.csv")
print(df)

print(df.head(2))

print(df.shape)
print(df.columns)

high_pressure = df[df["pressure_psi"] > 10000]
print(high_pressure)

gom_high = df[(df["basin"] == "GoM") & (df["pressure_psi"] > 10000)]
print(gom_high)

basin_stats = df.groupby("basin")["pressure_psi"].mean()
print(basin_stats)

basin_counts = df.groupby("basin")["name"].count()
print(basin_counts)

high_pressure.to_csv("high_pressure_pandas.csv" , index=False)
print("Saved")

# Option 1: Drop rows with any missing values
df_clean = df.dropna()
print("After dropping rows with NaN:")
print(df_clean)
print()

# Option 2: Fill missing values with a default
df_filled = df.fillna(0)
print("After filling NaN with 0:")
print(df_filled)