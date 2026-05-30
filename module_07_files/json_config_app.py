import json
import pandas as pd

# Step 1: Load the config
with open("job_config.json", "r") as file:
    config = json.load(file)

# Step 2: Read the CSV with pandas
df = pd.read_csv("wells.csv")

# Step 3: Filter based on config values
filtered = df[
    (df["basin"] == config["filter_basin"])
    & (df["pressure_psi"] >= config["min_pressure_psi"])
]

# Step 4: Write to the file specified in config
filtered.to_csv(config["output_file"], index=False)

print(f"Saved to {config['output_file']}")
