import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV file
csv_file_name = 'data_height_vs_powerEfficiency.csv'
data = pd.read_csv(csv_file_name)

# Plot 1: Height vs NOMA_avg_power and OMA_avg_power
plt.figure(figsize=(10, 6))
plt.plot(data['height'], data['NOMA_total_power'], label='NOMA_total_power', marker='o')
plt.plot(data['height'], data['OMA_total_power'], label='OMA_total_power', marker='s')
plt.xlabel('UAV Height (m)')
plt.ylabel('Total Power (dBm)')
plt.title('Height vs Total Power')
plt.legend()
plt.gca().set_xticks(range(0, max(data['height']) + 1, 10)) # set vertical gridlines at multiples of 4
plt.grid(which='both', axis='x')
plt.savefig('Fig_Height_vs_Total_Power.png')

# Plot 2: Height vs NOMA_power_efficiency and OMA_power_efficiency
plt.figure(figsize=(10, 6))
plt.plot(data['height'], data['NOMA_power_efficiency'], label='NOMA_power_efficiency', marker='o')
plt.plot(data['height'], data['OMA_power_efficiency'], label='OMA_power_efficiency', marker='s')
plt.xlabel('UAV Height (m)')
plt.ylabel('Power Efficiency (dBm)')
plt.title('Height vs Power Efficiency')
plt.legend()
plt.gca().set_xticks(range(0, max(data['height']) + 1, 10)) # set vertical gridlines at multiples of 4
plt.grid(which='both', axis='x')
plt.savefig('Fig_Height_vs_Power_Efficiency.png')
