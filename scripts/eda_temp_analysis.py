import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Loading my data
data_path = "../data/sierraleone-bumbuna.csv"
df = pd.read_csv(data_path)

# Convert 'Timestamp' to datetime
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Filter necessary columns for analysis
columns_of_interest = ['RH', 'Tamb', 'TModA', 'TModB', 'GHI', 'DNI', 'DHI']
df = df[columns_of_interest]

# Correlation Analysis 

# Calculate correlation matrix
correlation_matrix = df.corr()
print("\nCorrelation Matrix:")
print(correlation_matrix)

# Plot correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", cbar=True)
plt.title("Correlation Matrix: RH, Temperature, and Solar Radiation")
plt.tight_layout()
plt.savefig("../output/correlation_matrix_rh_temp_radiation.png")
# plt.show()

# Scatter Plots 
# Define pairs to plot: RH vs. other variables
variables_to_analyze = ['Tamb', 'TModA', 'TModB', 'GHI', 'DNI', 'DHI']

plt.figure(figsize=(12, 10))
for i, var in enumerate(variables_to_analyze, 1):
    plt.subplot(3, 2, i)
    sns.scatterplot(x=df['RH'], y=df[var], alpha=0.7)
    plt.title(f"RH vs. {var}")
    plt.xlabel("Relative Humidity (%)")
    plt.ylabel(var)
    plt.grid(alpha=0.3)

plt.tight_layout()
plt.savefig("../output/scatter_plots_rh_temp_radiation.png")
# plt.show()

# -------------------- Statistical Relationships --------------------

# Perform Pearson correlation tests between RH and other variables
print("\nPearson Correlation Coefficients:")
for var in variables_to_analyze:
    corr, p_value = pearsonr(df['RH'], df[var])
    print(f"RH vs. {var}: Correlation = {corr:.2f}, p-value = {p_value:.3e}")

# -------------------- Regression Analysis --------------------

# Pairplot with regression lines for RH and selected variables
sns.pairplot(df, x_vars=['RH'], y_vars=variables_to_analyze, kind='reg', height=3, aspect=1)
plt.suptitle("Regression Analysis: RH vs. Temperature and Solar Radiation", y=1.02)
plt.tight_layout()
plt.savefig("../output/regression_rh_temp_radiation.png")
# plt.show()





