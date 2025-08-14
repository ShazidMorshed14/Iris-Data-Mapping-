import pandas as pd

input_file = "Updated National Retailer List with TSA Demarcation_June'25.xlsb"
output_file = "unique_tsa_list.xlsx"

# Read from the 'Outlet List' sheet, starting from row 5 (skip first 4 rows)
df = pd.read_excel(
    input_file,
    sheet_name="Outlet List",   # specify sheet
    engine="pyxlsb",
    skiprows=4,
    dtype={"TSA ID 2": str}
)

# Show available columns to verify
print("Available columns:", df.columns.tolist())

# Select needed columns
df = df[["TSA Location", "TSA ID 2"]]

# Drop rows without TSA ID 2
df = df.dropna(subset=["TSA ID 2"])

# Keep first occurrence of each TSA ID 2
unique_df = df.drop_duplicates(subset=["TSA ID 2"], keep="first").reset_index(drop=True)

# Save to Excel
unique_df.to_excel(output_file, index=False)

print(f"✅ Unique TSA ID 2 list saved as: {output_file}")
