import matplotlib.pyplot as plt
import csv

# Read data from CSV file
heights = []
values = []

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        heights.append(int(row[0]))  # Assuming first value in row is height
        # Convert the rest of the row to integers and calculate the average
        user_values = list(map(float, row[1:]))
        values.append(sum(user_values) / len(user_values))

# Plot the bar graph
plt.plot(heights, values)
plt.xlabel('Height')
plt.ylabel('Average Value of Channel Gain')
plt.title('Height vs Average Channel Gain')
plt.savefig("Fig_Height_vs_Average_Channel_Gain.png")
plt.show()
