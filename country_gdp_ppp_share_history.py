import matplotlib.pyplot as plt
import pandas as pd

# 1. Define the data extracted from the plot
data = {
    'Year': [1, 1000, 1500, 1600, 1700, 1820, 1850, 1870, 1900, 1913, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2017],
    'UNITED STATES': [2, 3, 3, 4, 4, 2, 8, 9, 18, 20, 28, 40, 39, 36, 35, 33, 31, 30, 29],
    'FRANCE': [2, 2, 2, 2, 2, 3, 4, 4, 4, 5, 3, 5, 4, 4, 3, 3, 3, 3, 2],
    'UNITED KINGDOM': [2, 2, 2, 2, 3, 5, 9, 12, 11, 10, 7, 6, 5, 4, 3, 2, 2, 2, 2],
    'SPAIN': [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'ITALY': [1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 1, 1],
    'GERMANY': [1, 1, 2, 2, 2, 4, 6, 7, 8, 11, 8, 4, 4, 4, 4, 4, 4, 3, 3],
    'RUSSIA': [2, 3, 2, 2, 2, 4, 6, 6, 8, 9, 7, 4, 4, 4, 4, 4, 3, 3, 3],
    'JAPAN': [3, 3, 3, 4, 5, 3, 3, 2, 4, 4, 5, 3, 4, 6, 7, 8, 8, 7, 6],
    'INDIA': [40, 37, 31, 28, 28, 18, 16, 16, 14, 12, 12, 7, 8, 8, 7, 7, 7, 8, 8],
    'CHINA': [30, 33, 34, 37, 32, 40, 30, 24, 16, 15, 14, 8, 8, 7, 7, 7, 11, 17, 15],
    'ANCIENT': [12, 12, 5, 5, 4, 8, 15, 18, 12, 9, 12, 20, 21, 24, 27, 29, 28, 25, 30]
}

# 2. Create a Pandas DataFrame
df = pd.DataFrame(data)
df = df.set_index('Year')

# 3. Define the stacking order (bottom to top) and colors
# This order must match the legend from bottom to top
columns = [
    'UNITED STATES', 'FRANCE', 'UNITED KINGDOM', 'SPAIN', 'ITALY', 
    'GERMANY', 'RUSSIA', 'JAPAN', 'INDIA', 'CHINA', 'ANCIENT'
]

# Approximate colors from the chart
colors = [
    '#000080',  # US (Navy)
    '#4169E1',  # FRANCE (RoyalBlue)
    '#800080',  # UK (Purple)
    '#006400',  # SPAIN (DarkGreen)
    '#FFD700',  # ITALY (Gold)
    '#000000',  # GERMANY (Black)
    '#48D1CC',  # RUSSIA (MediumTurquoise)
    '#E67E22',  # JAPAN (Carrot)
    '#F39C12',  # INDIA (Orange)
    '#C0392B',  # CHINA (Pomegranate)
    '#F5DEB3'   # ANCIENT (Wheat)
]

# 4. Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Generate the stackplot using index positions for x-axis
x_positions = range(len(df.index))
ax.stackplot(x_positions, df[columns].T, labels=columns, colors=colors, alpha=0.9)

# 5. Customize the plot to match the original
ax.set_title('Share of GDP (WORLD POWERS)', fontsize=16, fontweight='bold')
ax.set_ylabel('Share of GDP (%)', fontsize=12)
ax.set_xlabel('Year', fontsize=12)

# Set Y-axis limits and ticks
ax.set_ylim(0, 100)
ax.set_yticks(range(0, 101, 10))
ax.set_yticklabels([f'{y}%' for y in range(0, 101, 10)])

# Set X-axis limits and ticks to match the index positions
ax.set_xlim(0, len(df.index) - 1)
ax.set_xticks(x_positions)
ax.set_xticklabels(df.index, rotation=45, ha='right')

# Add legend to the right side of the plot
# We reverse the handles and labels to match the plot's stacking order (top to bottom)
handles, labels = ax.get_legend_handles_labels()
ax.legend(
    handles[::-1], 
    labels[::-1], 
    loc='center left', 
    bbox_to_anchor=(1.0, 0.5), 
    fontsize=11
)

# Remove the top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Adjust layout to prevent legend from being cut off
plt.tight_layout(rect=[0, 0, 0.85, 1])

# 6. Show the plot
plt.show()