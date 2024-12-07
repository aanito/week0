import pandas as pd
import os

# Loading my data
data_path = "../data/sierraleone-bumbuna.csv"
df = pd.read_csv(data_path)

# Display the first few rows
print(df.head())


# Summary Statistics 
numeric_cols = df.select_dtypes(include='number')  # Filtering only the numeric columns
for col in numeric_cols:
    print(f"\nColumn: {col}")
    print(f"Mean: {df[col].mean()}")
    print(f"Median: {df[col].median()}")
    print(f"Standard Deviation: {df[col].std()}")


# Other Summary Statistics
print("Computed summary statistics:")
print(df.describe())