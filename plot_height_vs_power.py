import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV file
csv_file_name = 'data_height_vs_energyEfficiency.csv'
data = pd.read_csv(csv_file_name)

# Plot 1: Height vs NOMA_total_power and OMA_total_power
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

# Plot 2: Height vs NOMA_energy_efficiency and OMA_energy_efficiency
plt.figure(figsize=(10, 6))
plt.plot(data['height'], data['NOMA_energy_efficiency_40'], label='NOMA_energy_efficiency_40', marker='o')
plt.plot(data['height'], data['OMA_energy_efficiency_40'], label='OMA_energy_efficiency_40', marker='s')
plt.plot(data['height'], data['NOMA_energy_efficiency_60'], label='NOMA_energy_efficiency_60', marker='v')
plt.plot(data['height'], data['OMA_energy_efficiency_60'], label='OMA_energy_efficiency_60', marker='X')
plt.xlabel('UAV Height (m)')
plt.ylabel('Energy Efficiency (in log scale)')
plt.title('Height vs Energy Efficiency')
plt.legend()
plt.savefig('Fig_Height_vs_Energy_Efficiency.png')
