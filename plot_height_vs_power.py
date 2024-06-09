import pandas as pd
import matplotlib.pyplot as plt

# Update rcParams to use Times New Roman
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'custom'
plt.rcParams['mathtext.rm'] = 'Times New Roman'
plt.rcParams['mathtext.it'] = 'Times New Roman:italic'
plt.rcParams['mathtext.bf'] = 'Times New Roman:bold'

# Read data from CSV file
csv_file_name = 'data_height_vs_energyEfficiency.csv'
data = pd.read_csv(csv_file_name)

# Plot 1: Height vs NOMA_total_power and OMA_total_power
plt.figure(figsize=(10, 6))
plt.plot(data['height'], [46]*len(data['height']), 'r--', label='maximum power')
plt.plot(data['height'], data['NOMA_total_power_40'], label='NOMA_total_power_40_UEs', marker='o')
plt.plot(data['height'], data['OMA_total_power_40'], label='OMA_total_power_40_UEs', marker='s')
plt.plot(data['height'], data['NOMA_total_power_60'], label='NOMA_total_power_60_UEs', marker='v')
plt.plot(data['height'], data['OMA_total_power_60'], label='OMA_total_power_60_UEs', marker='X')
plt.xlabel('UAV Height (m)')
plt.ylabel('Total Power (dBm)')
plt.title('Height vs Total Power')
plt.legend()
plt.savefig('Fig_Height_vs_Total_Power.png')

# Plot 2: Height vs NOMA_energy_efficiency and OMA_energy_efficiency
plt.figure(figsize=(10, 6))
plt.plot(data['height'], data['NOMA_energy_efficiency_40'], label='NOMA_energy_efficiency_40_UEs', marker='o')
plt.plot(data['height'], data['OMA_energy_efficiency_40'], label='OMA_energy_efficiency_40_UEs', marker='s')
plt.plot(data['height'], data['NOMA_energy_efficiency_60'], label='NOMA_energy_efficiency_60_UEs', marker='v')
plt.plot(data['height'], data['OMA_energy_efficiency_60'], label='OMA_energy_efficiency_60_UEs', marker='X')
plt.xlabel('UAV Height (m)')
plt.ylabel('Energy Efficiency (in log scale)')
plt.title('Height vs Energy Efficiency')
plt.legend()
plt.savefig('Fig_Height_vs_Energy_Efficiency.png')
