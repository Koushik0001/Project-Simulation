import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV file
csv_file_name = 'power_efficiency_comparison.csv'
data = pd.read_csv(csv_file_name)

# Plot 1: Number of Users vs NOMA_avg_power and OMA_avg_power
plt.figure(figsize=(10, 6))
plt.plot(data['number_of_users'], data['NOMA_avg_power'], label='NOMA_avg_power', marker='o')
plt.plot(data['number_of_users'], data['OMA_avg_power'], label='OMA_avg_power', marker='s')
plt.xlabel('Number of Users')
plt.ylabel('Average Power (dBm)')
plt.title('Number of Users vs Average Power')
plt.legend()
plt.grid(True)
plt.savefig('num_users_vs_avg_power.png')
plt.show()

# Plot 2: Number of Users vs NOMA_power_efficiency and OMA_power_efficiency
plt.figure(figsize=(10, 6))
plt.plot(data['number_of_users'], data['NOMA_power_efficiency'], label='NOMA_power_efficiency', marker='o')
plt.plot(data['number_of_users'], data['OMA_power_efficiency'], label='OMA_power_efficiency', marker='s')
plt.xlabel('Number of Users')
plt.ylabel('Power Efficiency (in log scale)')
plt.title('Number of Users vs Power Efficiency')
plt.legend()
plt.grid(True)
plt.savefig('num_users_vs_power_efficiency.png')
plt.show()
