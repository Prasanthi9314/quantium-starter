import pandas as pd
import os

# Folder containing the CSV files
data_folder = "data"

# Get all CSV files in the data folder
csv_files = [file for file in os.listdir(data_folder) if file.endswith(".csv")]

all_data = []

for file in csv_files:
    file_path = os.path.join(data_folder, file)

    # Read CSV
    df = pd.read_csv(file_path)

    # Clean product names (remove spaces + make lowercase)
    df["product"] = df["product"].astype(str).str.strip().str.lower()

    # Keep only pink morsel rows
    df = df[df["product"] == "pink morsel"]

    # Convert price column (remove $ sign)
    df["price"] = df["price"].replace('[\$,]', '', regex=True).astype(float)

    # Convert quantity to numeric
    df["quantity"] = pd.to_numeric(df["quantity"])

    # Create Sales column
    df["Sales"] = df["price"] * df["quantity"]

    # Keep only required columns
    df = df[["Sales", "date", "region"]]

    # Rename columns as required
    df = df.rename(columns={"date": "Date", "region": "Region"})

    # Add to list
    all_data.append(df)

# Combine all files into one dataframe
final_df = pd.concat(all_data, ignore_index=True)

# Save output file
final_df.to_csv("output.csv", index=False)

print(" Task 1 complete! output.csv generated successfully.")
print("Total rows:", final_df.shape[0])
print(final_df.head())
