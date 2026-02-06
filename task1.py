import pandas as pd
import os

# Folder where your CSV files are stored
data_folder = "data"

# List of all csv files inside the folder
csv_files = [file for file in os.listdir(data_folder) if file.endswith(".csv")]

all_data = []

for file in csv_files:
    file_path = os.path.join(data_folder, file)
    
    df = pd.read_csv(file_path)

    # Keep only Pink Morsels
    df = df[df["product"] == "Pink Morsels"]

    # Create sales column
    df["Sales"] = df["quantity"] * df["price"]

    # Keep only required columns
    df = df[["Sales", "date", "region"]]

    # Rename columns properly
    df = df.rename(columns={"date": "Date", "region": "Region"})

    all_data.append(df)

# Combine all 3 files into one dataframe
final_df = pd.concat(all_data, ignore_index=True)

# Save output file
final_df.to_csv("output.csv", index=False)

print("Output saved as output.csv")
