import pandas as pd

# Read Excel file
df = pd.read_excel("route_mapping_with_tsa_id.xlsx")

# Keep only needed columns
df = df[['id', 'route_id']].rename(columns={'id': 'tsa_location_id'})

# Drop rows where tsa_location_id or route_id is missing
df = df.dropna(subset=['tsa_location_id', 'route_id'])

# Convert to int safely
df['tsa_location_id'] = df['tsa_location_id'].astype(int)
df['route_id'] = df['route_id'].astype(int)

# Drop duplicate pairs
df = df.drop_duplicates(subset=['tsa_location_id', 'route_id'])

# Generate unique 'name' like 101_1, 101_2, ...
df['name'] = df.groupby('tsa_location_id').cumcount() + 1
df['name'] = df['tsa_location_id'].astype(str) + "_" + df['name'].astype(str)

# Add created_at and updated_at with static values
static_time = "2025-08-18 00:00:00.000"
df['created_at'] = static_time
df['updated_at'] = static_time

# Select only required columns
df_final = df[['name', 'tsa_location_id', 'route_id', 'created_at', 'updated_at']]

# Export to CSV
df_final.to_csv("final_tsa_location_mapping.csv", index=False)

print("✅ final_tsa_location_mapping.csv created successfully!")
