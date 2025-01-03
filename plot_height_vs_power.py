import pandas as pd
import matplotlib.pyplot as plt

# Update rcParams to use Times New Roman
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'custom'
plt.rcParams['mathtext.rm'] = 'Times New Roman'
plt.rcParams['mathtext.it'] = 'Times New Roman withitalic'
plt.rcParams['mathtext.bf'] = 'Times New Roman withbold'

# Read data from CSV file
csv_file_name = 'data_height_vs_energyEfficiency.csv'
data = pd.read_csv(csv_file_name)

# Plot 1 with Height vs NOMA_total_power and OMA_total_power
# plt.figure(figsize=(10, 6))
# plt.plot(data['height'], [46]*len(data['height']), 'r--', label='maximum power')
# plt.plot(data['height'], data['NOMA_total_power_40'], label='NOMA_total_power_40_UEs', marker='o')
# plt.plot(data['height'], data['OMA_total_power_40'], label='OMA_total_power_40_UEs', marker='s')
# plt.plot(data['height'], data['NOMA_total_power_60'], label='NOMA_total_power_60_UEs', marker='v')
# plt.plot(data['height'], data['OMA_total_power_60'], label='OMA_total_power_60_UEs', marker='X')
# plt.xlabel('UAV Height (m)')
# plt.ylabel('Total Power (dBm)')
# plt.title('Height vs Total Power')
# plt.legend()
# plt.savefig('Fig_Height_vs_Total_Power.png')

# Plot 2: Height vs NOMA_energy_efficiency and OMA_energy_efficiency
font_size = 22
plt.figure(figsize=(10, 6))
plt.plot(data['height'], data['NOMA_energy_efficiency_40'], label='Non-exclusive clustering with NOMA_40 UEs', marker='v')
plt.plot(data['height'], data['NOMA_energy_efficiency_60'], label='Non-exclusive clustering with NOMA_60 UEs', marker='o')
plt.plot(data['height'], data['ex-NOMA_energy_efficiency_40'], label='Exclusive clustering with NOMA_40 UEs', marker='1')
plt.plot(data['height'], data['ex-NOMA_energy_efficiency_60'], label='Exclusive clustering with NOMA_60 UEs', marker='X')
plt.plot(data['height'], data['OMA_energy_efficiency_40'], label='No clustering with OMA_40 UEs', marker='+')
plt.plot(data['height'], data['OMA_energy_efficiency_60'], label='No clustering with OMA_60 UEs', marker='P')
plt.xlabel('UAV Height (m)', fontsize=font_size)
plt.ylabel('Energy Efficiency (in log scale)', fontsize=font_size)
plt.title('Height vs Energy Efficiency', fontsize=font_size)
plt.legend(fontsize=font_size-9)
plt.xticks(fontsize=font_size-8)
plt.yticks(fontsize=font_size-8)
plt.savefig('Fig_Height_vs_Energy_Efficiency.png')
