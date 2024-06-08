import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV file
csv_file_name = 'data_numberOfUEs_vs_power.csv'
data = pd.read_csv(csv_file_name)

# Plot 1: Number of UEs vs NOMA_total_power and OMA_total_power
plt.figure(figsize=(10, 6))
plt.plot(data['number_of_UEs'], [46]*len(data['number_of_UEs']), 'r--', label='maximum power')
plt.plot(data['number_of_UEs'], data['NOMA_total_power'], label='NOMA_total_power', marker='o')
plt.plot(data['number_of_UEs'], data['OMA_total_power'], label='OMA_total_power', marker='s')
plt.xlabel('Number of Users')
plt.ylabel('Total Power (dBm)')
plt.title('Number of UEs vs Total Power')
plt.legend()
plt.savefig('Fig_UEs_vs_TotalPower.png')

# Plot 2: Number of UEs vs NOMA_energy_efficiency and OMA_energy_efficiency
plt.figure(figsize=(10, 6))
plt.plot(data['number_of_UEs'], data['NOMA_energy_efficiency'], label='NOMA_energy_efficiency', marker='o')
plt.plot(data['number_of_UEs'], data['OMA_energy_efficiency'], label='OMA_energy_efficiency', marker='s')
plt.xlabel('Number of Users')
plt.ylabel('Energy Efficiency (in log scale)')
plt.title('Number of UEs vs Energy Efficiency')
plt.legend()
plt.savefig('Fig_UEs_vs_EnergyEfficiency.png')

