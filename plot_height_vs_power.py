import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV file
csv_file_name = 'data_height_vs_powerEfficiency.csv'
data = pd.read_csv(csv_file_name)

# Plot 1: Height vs NOMA_avg_power and OMA_avg_power
plt.figure(figsize=(10, 6))
plt.plot(data['height'], [46]*len(data['height']), 'r--', label='maximum power')
plt.plot(data['height'], data['NOMA_total_power_40'], label='NOMA_total_power_40', marker='o')
plt.plot(data['height'], data['OMA_total_power_40'], label='OMA_total_power_40', marker='s')
plt.plot(data['height'], data['NOMA_total_power_60'], label='NOMA_total_power_60', marker='v')
plt.plot(data['height'], data['OMA_total_power_60'], label='OMA_total_power_60', marker='X')
plt.xlabel('UAV Height (m)')
plt.ylabel('Total Power (dBm)')
plt.title('Height vs Total Power')
plt.legend()
plt.savefig('Fig_Height_vs_Total_Power.png')

# Plot 2: Height vs NOMA_power_efficiency and OMA_power_efficiency
plt.figure(figsize=(10, 6))
plt.plot(data['height'], data['NOMA_power_efficiency_40'], label='NOMA_power_efficiency_40', marker='o')
plt.plot(data['height'], data['OMA_power_efficiency_40'], label='OMA_power_efficiency_40', marker='s')
plt.plot(data['height'], data['NOMA_power_efficiency_60'], label='NOMA_power_efficiency_60', marker='v')
plt.plot(data['height'], data['OMA_power_efficiency_60'], label='OMA_power_efficiency_60', marker='X')
plt.xlabel('UAV Height (m)')
plt.ylabel('Power Efficiency (dBm)')
plt.title('Height vs Power Efficiency')
plt.legend()
plt.savefig('Fig_Height_vs_Power_Efficiency.png')
