import matplotlib.pyplot as plt
import numpy as np

# Data
# regions = ['US', 'Australia', 'UK', 'Canada', 'EU', 'China', 'Latin America', 'ASEAN', 'India', 'Africa']
# gdp_per_capita = [89000, 65000, 57000, 54000, 45000, 13000, 10710, 5904, 2820, 2080]
regions = ['US', 'Australia', 'UK', 'Canada', 'EU', 'Japan', 'Russia', 'China', 'Latin America', 'ASEAN', 'India', 'Africa']
gdp_per_capita = [89000, 65000, 57000, 54000, 45000, 35000, 14000, 13000, 10710, 5904, 2820, 2080]

# Create a horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 6))

# Add shaded background regions for income categories
ax.axvspan(0, 10000, alpha=0.2, color='red', label='Poor (0-$10K)')
ax.axvspan(10000, 30000, alpha=0.2, color='orange', label='Middle Income ($10K-$30K)')
ax.axvspan(30000, max(gdp_per_capita) + 15000, alpha=0.2, color='green', label='Developed ($30K+)')

# Create the horizontal bar chart
ax.barh(regions, gdp_per_capita, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'])

# Add labels and title
ax.set_xlabel('Nominal GDP per Capita (USD)')
ax.set_ylabel('Region')
ax.set_title('Nominal GDP per Capita (2025)')

# Add value labels to the bars
for index, value in enumerate(gdp_per_capita):
    ax.text(value + 1000, index, f'${value/1000:.0f}K', va='center', fontweight='bold', fontsize=20)

# Adjust plot to fit labels
ax.set_xlim(0, max(gdp_per_capita) + 15000)

# Add legend for the background regions
ax.legend(loc='upper right')

# Display the plot
plt.tight_layout()
plt.show()
