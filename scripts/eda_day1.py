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

#check missing values
print("\nMissing values per each column:")
print(df.isnull().sum())

#Check for incorrecct values (negative or out of range)
numeric_col2 = ['GHI', 'DNI', 'DHI']
#outlier set = []'ModA', 'ModB', 'WS', 'WSgust']
negative_values = df[numeric_col2][df[numeric_col2] < 0].dropna(how="all")
if not negative_values.empty:
    print("\nNegative values found:")
    print(negative_values)

#Outlier detection
def detect_outliers_iqr(data, column):
    q1 = data[column].quantile(0.25)
    q3 = data[column].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]
    return outliers

print("\nOutlers detected:")
outlier_cols = ['ModA', 'ModB', 'WS', 'WSgust']
for col in outlier_cols:
    outliers = detect_outliers_iqr(df, col)
    if not outliers.empty:
        print(f" - outliers in {col}:")
        print(outliers[[col]])
    else:
        print(f"- no significant outliers in {col}")


