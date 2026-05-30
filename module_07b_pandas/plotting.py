import pandas as pd
import matplotlib.pyplot as plt

# load data
df = pd.read_csv("wells.csv")

# drop rows with missing pressure (matplotlib can't plot NaN)
df = df.dropna(subset=["pressure_psi"])

# bar chart: pressure by well
df.plot(kind="bar" , x="name", y="pressure_psi", title="Pressure by Well")
plt.tight_layout()
plt.savefig("pressure_chart.png")

print("Chart saved as pressure_chart.png")

# scatter plot: depth vs pressure
df.plot(kind="scatter", x="depth_ft", y="pressure_psi", title="Depth vs Pressure")
plt.tight_layout()
plt.savefig("depth_pressure.png")

# group by basin, plot averages
basin_pressure = df.groupby("basin")["pressure_psi"].mean()
basin_pressure.plot(kind="bar", title="Average Pressure by Basin")
plt.tight_layout()
plt.savefig("basin_pressure.png")

print("All charts saved")