import pandas as pd
import matplotlib.pyplot as plt
from windrose import WindroseAxes

# Loading my data
data_path = "../data/sierraleone-bumbuna.csv"
df = pd.read_csv(data_path)

# Converting 'Timestamp' to datetime
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Filtering necessary columns: WS, WSgust, WD
df = df[['Timestamp', 'WS', 'WSgust', 'WD']]

# -------------------- Wind Rose Plot --------------------

# Define a function to plot a wind rose
def plot_wind_rose(speed, direction, title, output_path):
    """
    Plots a wind rose using wind speed and direction data.
    """
    # Create WindroseAxes instance
    ax = WindroseAxes.from_ax()
    ax.bar(direction, speed, normed=True, opening=0.8, edgecolor='white', bins=[0, 2, 4, 6, 8, 10, 12, 15, 20])
    
    # Customize plot
    ax.set_legend(title="Wind Speed (m/s)", loc="lower right", fontsize=10)
    ax.set_title(title, fontsize=12)
    
    # Save and show the plot
    plt.savefig(output_path, bbox_inches='tight')
    plt.show()

# Plot wind rose for wind speed
print("\nPlotting Wind Rose for Wind Speed (WS)...")
plot_wind_rose(
    speed=df['WS'], 
    direction=df['WD'], 
    title="Wind Rose: Wind Speed Distribution by Direction", 
    output_path="../output/wind_rose_ws.png"
)

# Plot wind rose for wind gusts
print("\nPlotting Wind Rose for Wind Gusts (WSgust)...")
plot_wind_rose(
    speed=df['WSgust'], 
    direction=df['WD'], 
    title="Wind Rose: Wind Gust Distribution by Direction", 
    output_path="../output/wind_rose_wsgust.png"
)

# -------------------- Variability in Wind Direction --------------------

# Aggregating wind direction variability over time
df['Hour'] = df['Timestamp'].dt.hour
wind_variability = df.groupby('Hour')['WD'].std()

# Plot wind direction variability
plt.figure(figsize=(10, 6))
plt.plot(wind_variability.index, wind_variability.values, marker='o', linestyle='-', color='b', label='Wind Direction Variability')
plt.title('Hourly Variability in Wind Direction', fontsize=14)
plt.xlabel('Hour of the Day', fontsize=12)
plt.ylabel('Standard Deviation of Wind Direction (°)', fontsize=12)
plt.grid(alpha=0.5)
plt.legend()
plt.tight_layout()
plt.savefig("../output/wind_direction_variability.png")
plt.show()

