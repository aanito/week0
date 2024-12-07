import pandas as pd
import os

# Loading my data
data_path = "../data/sierraleone-bumbuna.csv"
df = pd.read_csv(data_path)

# Display the first few rows
print(df.head())

# Summary Statistics
# print("Summary Statistics:")
# print(df.describe())

# Calculate additional metrics
# numeric_cols = df.select_dtypes(include='number')  # Select numeric columns
# for col in numeric_cols:
#     print(f"\nColumn: {col}")
#     print(f"Mean: {df[col].mean()}")
#     print(f"Median: {df[col].median()}")
#     print(f"Standard Deviation: {df[col].std()}")