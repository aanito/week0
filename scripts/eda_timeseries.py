import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading my data
data_path = "../data/sierraleone-bumbuna.csv"
df = pd.read_csv(data_path)

# Convert 'Timestamp' to datetime for time-based analysis
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Extract additional time-related features
df['Month'] = df['Timestamp'].dt.month
df['Hour'] = df['Timestamp'].dt.hour
df['Date'] = df['Timestamp'].dt.date


# Plotting GHI, DNI, DHI, and Tamb by Month
monthly_avg = df.groupby('Month')[['GHI', 'DNI', 'DHI', 'Tamb']].mean()
plt.figure(figsize=(10, 6))
monthly_avg.plot(kind='bar', alpha=0.8, figsize=(10, 6), colormap='viridis')
plt.title('Monthly Average of Solar Irradiance (GHI, DNI, DHI) and Temperature (Tamb)')
plt.xlabel('Month')
plt.ylabel('Value')
plt.xticks(range(12), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45)
plt.tight_layout()
plt.savefig("../output/monthly_irradiance_temperature.png")
# plt.show()

# Plotting GHI, DNI, DHI, and Tamb Trends Throughout the Day
hourly_avg = df.groupby('Hour')[['GHI', 'DNI', 'DHI', 'Tamb']].mean()
plt.figure(figsize=(10, 6))
hourly_avg.plot(kind='line', alpha=0.8, figsize=(10, 6), colormap='coolwarm')
plt.title('Hourly Average of Solar Irradiance (GHI, DNI, DHI) and Temperature (Tamb)')
plt.xlabel('Hour of the Day')
plt.ylabel('Value')
plt.grid()
plt.tight_layout()
plt.savefig("../output/hourly_irradiance_temperature.png")
plt.show()

# 3. Identifying Anomalies (Peaks and Fluctuations)
plt.figure(figsize=(12, 6))
for col in ['GHI', 'DNI', 'DHI', 'Tamb']:
    plt.plot(df['Timestamp'], df[col], label=col, alpha=0.7)
plt.title('Trends of GHI, DNI, DHI, and Tamb Over Time')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.tight_layout()
plt.savefig("../output/time_trends_irradiance_temperature.png")
# plt.show()

# Impact of Cleaning on Sensor Readings

# Comparing Sensor Readings (ModA, ModB) with and without Cleaning
cleaning_impact = df.groupby('Cleaning')[['ModA', 'ModB']].mean()
print("\nAverage Sensor Readings (ModA, ModB) Based on Cleaning:")
print(cleaning_impact)

# Bar plot for sensor readings based on cleaning status
plt.figure(figsize=(8, 5))
cleaning_impact.plot(kind='bar', alpha=0.8, colormap='plasma', figsize=(8, 5))
plt.title('Impact of Cleaning on Sensor Readings (ModA, ModB)')
plt.xlabel('Cleaning Status (0 = Not Cleaned, 1 = Cleaned)')
plt.ylabel('Average Reading')
plt.tight_layout()
plt.savefig("../output/cleaning_impact_sensor_readings.png")
# plt.show()

# 5. Line Plot of ModA and ModB Over Time, Highlighting Cleaning Events
plt.figure(figsize=(12, 6))
plt.plot(df['Timestamp'], df['ModA'], label='ModA', alpha=0.7)
plt.plot(df['Timestamp'], df['ModB'], label='ModB', alpha=0.7)
plt.scatter(df['Timestamp'][df['Cleaning'] == 1], df['ModA'][df['Cleaning'] == 1], color='red', label='Cleaning Event (ModA)', alpha=0.7)
plt.scatter(df['Timestamp'][df['Cleaning'] == 1], df['ModB'][df['Cleaning'] == 1], color='blue', label='Cleaning Event (ModB)', alpha=0.7)
plt.title('Sensor Readings (ModA, ModB) Over Time with Cleaning Events Highlighted')
plt.xlabel('Time')
plt.ylabel('Sensor Reading')
plt.legend()
plt.tight_layout()
plt.savefig("../output/sensor_readings_cleaning_events.png")
# plt.show()
