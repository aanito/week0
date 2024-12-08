import pandas as pd
import numpy as np

# Loading my data
data_path = "../data/sierraleone-bumbuna.csv"
df = pd.read_csv(data_path)

# Display the initial state of the dataset
print("Initial dataset summary:")
print(df.info())
print("\nMissing values per column:")
print(df.isnull().sum())

# -------------------- Data Cleaning --------------------

# 1. Drop columns with excessive missing values (e.g., 'Comments')
if df['Comments'].isnull().all():
    print("\nDropping column 'Comments' as it is entirely null.")
    df.drop(columns=['Comments'], inplace=True)

# 2. Handle missing values in critical numerical columns
critical_columns = ['GHI', 'DNI', 'DHI', 'Tamb', 'TModA', 'TModB', 'WS', 'WSgust', 'BP', 'RH']
for col in critical_columns:
    if col in df.columns:
        missing_count = df[col].isnull().sum()
        if missing_count > 0:
            print(f"Handling missing values in {col}: {missing_count} missing.")
            
            # Replace missing values with the median
            median_value = df[col].median()
            df[col].fillna(median_value, inplace=True)
            print(f"Filled missing values in {col} with median: {median_value:.2f}")

# 3. Remove invalid or anomalous data
# Example: Solar irradiance (GHI, DNI, DHI) should not be negative
irradiance_columns = ['GHI', 'DNI', 'DHI']
for col in irradiance_columns:
    if col in df.columns:
        invalid_count = (df[col] < 0).sum()
        if invalid_count > 0:
            print(f"Removing {invalid_count} invalid entries in {col} (negative values).")
            df = df[df[col] >= 0]

# Example: Wind Speed and Gust should not be negative
wind_columns = ['WS', 'WSgust']
for col in wind_columns:
    if col in df.columns:
        invalid_count = (df[col] < 0).sum()
        if invalid_count > 0:
            print(f"Removing {invalid_count} invalid entries in {col} (negative values).")
            df = df[df[col] >= 0]

# 4. Remove rows with extreme Z-score outliers
from scipy.stats import zscore

# Define a threshold for Z-scores
z_threshold = 3

# Apply Z-score filtering on critical columns
zscore_columns = critical_columns  # Focus on numerical columns
z_scores = df[zscore_columns].apply(zscore, nan_policy='omit')
outliers = (np.abs(z_scores) > z_threshold).any(axis=1)
outlier_count = outliers.sum()
if outlier_count > 0:
    print(f"Removing {outlier_count} rows with extreme Z-scores (>|{z_threshold}|).")
    df = df[~outliers]

# 5. Remove duplicate rows
duplicate_count = df.duplicated().sum()
if duplicate_count > 0:
    print(f"Removing {duplicate_count} duplicate rows.")
    df.drop_duplicates(inplace=True)

# -------------------- Save Cleaned Dataset --------------------

# Save the cleaned dataset
cleaned_data_path = "../output/cleaned_data.csv"
df.to_csv(cleaned_data_path, index=False)
print(f"\nCleaned dataset saved to {cleaned_data_path}")

# Final dataset summary
print("\nCleaned dataset summary:")
print(df.info())
