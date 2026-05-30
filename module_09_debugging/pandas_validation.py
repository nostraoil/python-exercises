import pandas as pd

df = pd.read_csv("wells_messy.csv")

print(df)
print()
print("Data Types:")
print(df.dtypes)

def validate_dataframe(df):
    """Validate a DataFrame of well data. Returns a list of error messages."""
    errors = []
    
    required_columns = ["name", "depth_ft", "pressure_psi"]
    
    # Check 1: required columns exist
    for col in required_columns:
        if col not in df.columns:
            errors.append(f"missing required column: {col}")
    
    # Check 2: required columns have no NaN values
    for col in required_columns:
        if col in df.columns:
            na_rows = df[df[col].isna()].index.tolist()
            if na_rows:
                for row in na_rows:
                    errors.append(f"row {row + 1}: missing {col}")
    
    return errors

errors = validate_dataframe(df)

if errors:
    print("Validation failed:")
    for error in errors:
        print(f"  - {error}")
else:
    print("Data is clean. Proceeding...")
    print(df)