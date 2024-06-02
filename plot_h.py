import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV file
csv_file_name = 'power_efficiency_vs_height.csv'
data = pd.read_csv(csv_file_name)

# Plot 1: Height vs NOMA_avg_power and OMA_avg_power
plt.figure(figsize=(10, 6))
plt.plot(data['height'], data['NOMA_avg_power'], label='NOMA_avg_power', marker='o')
plt.plot(data['height'], data['OMA_avg_power'], label='OMA_avg_power', marker='s')
plt.xlabel('UAV height')
plt.ylabel('Average Power (dBm)')
plt.title('Height  vs Average Power')
plt.legend()
plt.gca().set_xticks(range(0, max(data['height']) + 1, 10)) # set vertical gridlines at multiples of 4
plt.grid(which='both', axis='x')
plt.grid(True)
plt.savefig('Height_vs_avg_power.png')
plt.show()

# Plot 2: Height vs NOMA_power_efficiency and OMA_power_efficiency
plt.figure(figsize=(10, 6))
plt.plot(data['height'], data['NOMA_power_efficiency'], label='NOMA_power_efficiency', marker='o')
plt.plot(data['height'], data['OMA_power_efficiency'], label='OMA_power_efficiency', marker='s')
plt.xlabel('Height')
plt.ylabel('Power Efficiency (in log scale)')
plt.title('Height vs Power Efficiency')
plt.legend()
plt.gca().set_xticks(range(0, max(data['height']) + 1, 10)) # set vertical gridlines at multiples of 4
plt.grid(which='both', axis='x')
plt.grid(True)
plt.savefig('height_vs_power_efficiency.png')
plt.show()
