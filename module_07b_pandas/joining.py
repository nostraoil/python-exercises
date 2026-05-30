import pandas as pd

wells = pd.read_csv("wells.csv")
completions = pd.read_csv("completions.csv")

print("Wells:")
print(wells)
print()
print("Completions:")
print(completions)

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

merged = pd.merge(
    wells,
    completions,
    left_on="name",
    right_on="well_name"
)

merged = merged.drop(columns=["well_name"])

print("Merged:")
print(merged)

print()
print("Question: Average completion cost by basin?")
print(merged.groupby("basin")["total_cost_usd"].mean())

print()
print("Question: Most expensive completion?")
most_expensive = merged.sort_values("total_cost_usd", ascending=False).head(1)
print(most_expensive[["name", "basin", "configuration", "total_cost_usd"]])

# Reading JSON into a DataFrame
wells_from_json = pd.read_json("wells.json")
print()
print("From JSON:")
print(wells_from_json)

import json
with open("wells.json", "r") as file:
    data = json.load(file)

wells_df = pd.DataFrame(data["wells"])
print(wells_df)