import os

# This shows you the path of the script itself
print(f"Script location: {__file__}")

# This shows the directory the script is in
script_dir = os.path.dirname(os.path.abspath(__file__))
print(f"Script directory: {script_dir}")

# This builds a path to wells.csv that lives next to the script
csv_path = os.path.join(script_dir, "wells.csv")
print(f"CSV path: {csv_path}")

# Now we can open the file using that path
with open(csv_path, "r") as file:
    print("\nFirst line of CSV:")
    print(file.readline())