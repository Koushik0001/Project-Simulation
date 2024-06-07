import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV file
csv_file_name = 'data_numberOfUsers_vs_power.csv'
data = pd.read_csv(csv_file_name)

# Plot 1: Number of Users vs NOMA_avg_power and OMA_avg_power
plt.figure(figsize=(10, 6))
plt.plot(data['number_of_users'], [46]*len(data['number_of_users']), 'r--', label='maximum power')
plt.plot(data['number_of_users'], data['NOMA_total_power'], label='NOMA_avg_power', marker='o')
plt.plot(data['number_of_users'], data['OMA_total_power'], label='OMA_avg_power', marker='s')
plt.xlabel('Number of Users')
plt.ylabel('Total Power (dBm)')
plt.title('Number of Users vs Total Power')
plt.legend()
plt.savefig('Fig_Users_vs_TotalPower.png')

# Plot 2: Number of Users vs NOMA_power_efficiency and OMA_power_efficiency
plt.figure(figsize=(10, 6))
plt.plot(data['number_of_users'], data['NOMA_power_efficiency'], label='NOMA_power_efficiency', marker='o')
plt.plot(data['number_of_users'], data['OMA_power_efficiency'], label='OMA_power_efficiency', marker='s')
plt.xlabel('Number of Users')
plt.ylabel('Power Efficiency (in log scale)')
plt.title('Number of Users vs Power Efficiency')
plt.legend()
plt.savefig('Fig_Users_vs_PowerEfficiency.png')

