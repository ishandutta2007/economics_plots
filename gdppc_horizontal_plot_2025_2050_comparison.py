import matplotlib.pyplot as plt
import numpy as np

# Data
regions = ['US', 'Australia', 'UK', 'Canada', 'EU', 'Japan', 'Russia', 'China', 'Latin America', 'ASEAN', 'India', 'Africa']
gdp_2025 = [89000, 65000, 57000, 54000, 45000, 35000, 14000, 13000, 10710, 5904, 2820, 2080]
gdp_2050 = [180000, 150000, 120000, 120000, 90000, 60000, 45000, 60000, 30000, 25000, 20000, 10000]

# Create a horizontal bar chart with grouped bars
fig, ax = plt.subplots(figsize=(12, 8))

# Set up the bar positions
y_pos = np.arange(len(regions))
bar_width = 0.35

# Create bars for 2025 and 2050
bars_2025 = ax.barh(y_pos + bar_width/2, gdp_2025, bar_width, 
                   label='2025', color='#1f77b4', alpha=0.8)
bars_2050 = ax.barh(y_pos - bar_width/2, gdp_2050, bar_width, 
                   label='2050', color='#ff7f0e', alpha=0.8)

# Add shaded background regions for income categories
ax.axvspan(0, 20000, alpha=0.2, color='red', label='2050s Poor levels(0-$20K)')
ax.axvspan(20000, 60000, alpha=0.2, color='orange', label='2050s Middle Income levels($20K-$60K)')
ax.axvspan(60000, max(gdp_2050) + 25000, alpha=0.2, color='green', label='2050s Developed levels($60K+)')

# Add labels and title
ax.set_xlabel('Nominal GDP per Capita (USD)', fontsize=12)
ax.set_ylabel('Region', fontsize=12)
ax.set_title('GDP per Capita Comparison: 2025 vs 2050 Projections', fontsize=14, fontweight='bold')
ax.set_yticks(y_pos)
ax.set_yticklabels(regions)

# Add value labels to the bars
for i, (val_2025, val_2050) in enumerate(zip(gdp_2025, gdp_2050)):
    # 2025 labels
    ax.text(val_2025 + 2000, i + bar_width/2, f'${val_2025/1000:.0f}K', 
            va='center', fontweight='bold', fontsize=10)
    # 2050 labels
    ax.text(val_2050 + 2000, i - bar_width/2, f'${val_2050/1000:.0f}K ({(val_2050/val_2025):.0f}x)', 
            va='center', fontweight='bold', fontsize=10)

# Add legend
ax.legend(loc='upper right')

# Adjust plot to fit labels
max_value = max(max(gdp_2025), max(gdp_2050))
ax.set_xlim(0, max_value + 20000)

# Add grid for better readability
ax.grid(True, axis='x', alpha=0.3)

# Display the plot
plt.tight_layout()
plt.show()
