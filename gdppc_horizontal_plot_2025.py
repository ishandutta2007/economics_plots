import matplotlib.pyplot as plt
import numpy as np

# Data
# regions = ['US', 'Australia', 'UK', 'Canada', 'EU', 'China', 'Latin America', 'ASEAN', 'India', 'Africa']
# gdp_per_capita = [89000, 65000, 57000, 54000, 45000, 13000, 10710, 5904, 2820, 2080]
regions = ['US', 'Australia', 'UK', 'Canada', 'EU', 'Japan', 'Russia', 'China', 'Latin America', 'ASEAN', 'India', 'Africa']
gdp_per_capita = [89000, 65000, 57000, 54000, 45000, 35000, 14000, 13000, 10710, 5904, 2820, 2080]

# Create a horizontal bar chart
plt.figure(figsize=(10, 6))
plt.barh(regions, gdp_per_capita, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'])

# Add labels and title
plt.xlabel('Nominal GDP per Capita (USD)')
plt.ylabel('Region')
plt.title('Nominal GDP per Capita (2025)')

# Add value labels to the bars
for index, value in enumerate(gdp_per_capita):
    plt.text(value + 1000, index, f'${value/1000:.0f}K', va='center', fontweight='bold', fontsize=20)

# Adjust plot to fit labels
plt.xlim(0, max(gdp_per_capita) + 15000)

# Display the plot
plt.tight_layout()
plt.show()
