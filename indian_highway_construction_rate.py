import matplotlib.pyplot as plt
import numpy as np

# Data for the plot
years = ['FY 20-21', 'FY 21-22', 'FY 22-23', 'FY 23-24', 'FY 24-25', 'FY 25-26 (Proj)']
km_per_day = [37, 29, 28.3, 34, 29, 26] # Using approximate values from the data

# Create a figure and a set of subplots
fig, ax = plt.subplots(figsize=(10, 6))

# Define colors for the bars
colors = ['skyblue'] * 5 + ['coral'] # Highlight the projected year in a different color

# Create the bar chart
ax.bar(years, km_per_day, color=colors)

# Add title and labels
ax.set_title("India's National Highway Construction Pace (Km Per Day) by Fiscal Year", fontsize=16, fontweight='bold')
ax.set_xlabel("Fiscal Year", fontsize=12)
ax.set_ylabel("Kilometers Per Day (km/day)", fontsize=12)

# Set y-axis limits to provide better visualization
ax.set_ylim(0, 40)

# Add the actual values on top of the bars
for i, v in enumerate(km_per_day):
    ax.text(i, v + 0.5, str(v), ha='center', va='bottom', fontsize=10)

# Add a horizontal line to indicate a potential average or target (optional)
# ax.axhline(y=30, color='r', linestyle='--', label='30 km/day target (example)')
# ax.legend()

# Improve layout and display the plot
plt.tight_layout()
plt.show()
