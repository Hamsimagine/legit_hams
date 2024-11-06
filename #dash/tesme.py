import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4']
voltages = [10, 20, 30, 40]
amperes = [5, 10, 15, 20]

# Create figure and axis
fig, ax = plt.subplots()

# Define gradient colors for voltage
cmap_voltage = plt.get_cmap('Blues')
colors_voltage = [cmap_voltage(v/40.0) for v in voltages]

# Define gradient colors for ampere
cmap_ampere = plt.get_cmap('Reds')
colors_ampere = [cmap_ampere(a/20.0) for a in amperes]

# Create bars
bars_voltage = ax.bar(np.arange(len(categories)) - 0.2, voltages, 0.4, color=colors_voltage, edgecolor='black', label='Voltage')
bars_ampere = ax.bar(np.arange(len(categories)) + 0.2, amperes, 0.4, color=colors_ampere, edgecolor='black', label='Ampere')

# Add labels and title
ax.set_xlabel('Categories')
ax.set_ylabel('Values')
ax.set_title('Bar Chart with Gradient Colors')
ax.set_xticks(np.arange(len(categories)))
ax.set_xticklabels(categories)
ax.legend()

# Display the plot
plt.show()