import matplotlib.pyplot as plt
import numpy as np
import csv

# Read data from CSV file
heights = []
data = []

with open('data_height_vs_channelGain.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        heights.append(int(row[0]))  # Assuming first value in row is height
        user_values = list(map(float, row[1:]))
        data.append(user_values)

# Transpose the data to group by users
data = np.array(data).T

# Number of heights and users
num_heights = len(heights)
num_users = data.shape[0]

# Define the positions of the bars
bar_width = 0.1
indices = np.arange(num_heights)

# Plotting the bars
for i in range(num_users):
    plt.bar(indices + i * bar_width, data[i], bar_width, label=f'User {i+1}')

# Set the labels and title
plt.xlabel('UAV Height (m)')
plt.ylabel('Value of h')
plt.title('Values of h for Each Height and User')
plt.xticks(indices + bar_width * (num_users - 1) / 2, heights)
plt.legend()
plt.savefig("Fig_Height_vs_Channel_Gain.png")
