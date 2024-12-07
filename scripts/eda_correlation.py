import pandas as pd
# import os
import seaborn as sns
# import matplotlib
# matplotlib.use('TkAgg') 

import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix


# Loading my data
data_path = "../data/sierraleone-bumbuna.csv"
df = pd.read_csv(data_path)

#Correlation - Solar radiation and temprature
solar_temp_cols = ['GHI', 'DNI', 'DHI', 'TModA', 'TModB']
print("\nCorrelation Matrix (Solar Radiation and Temperature):")
correlation_matrix = df[solar_temp_cols].corr()
print(correlation_matrix)

#Plot matric to a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", cbar=True)
plt.title("Correlation Matrix - Solar Radiation and Temperature")
plt.tight_layout()
plt.savefig("../output/correlation_matrix_solar_temp.png")
# plt.show()


#Pair plot visualizing the relationship
sns.pairplot(df[solar_temp_cols], diag_kind="kde", corner=True)
plt.suptitle("Pair Plot: Solar Radiation and Temperature", y=1.02)
plt.tight_layout()
plt.savefig("../output/pair_plot_solar_temp.png")
plt.show()


#Define wind and solar columns
wind_solar_cols = ['GHI', 'DNI', 'DHI', 'WS', 'WSgust', 'WD']

#Scatter matrix - wind conditions vs solar irradation
print("\nGenerating scatter matrix for wind conditions and solar irradiance...")
scatter_matrix_fig = scatter_matrix(df[wind_solar_cols], figsize=(10, 10), diagonal='kde', alpha=0.7, grid=True)
plt.suptitle("Scatter Matrix: Wind Conditions and Solar Irradiance", y=1.02)
plt.tight_layout()
plt.savefig("../output/scatter_matrix_wind_solar.png")
plt.show()


