import matplotlib.pyplot as plt

# Dataset based on IEA and macroeconomic energy tracking studies
years = [1979, 1998, 2008, 2015, 2019, 2022, 2024]
total_gdp_share = [10.3, 3.0, 8.1, 6.0, 5.5, 9.8, 8.0]
crude_oil_share = [6.5, 1.2, 4.3, 3.1, 2.3, 4.6, 3.4]
non_crude_share = [3.8, 1.8, 3.8, 2.9, 3.2, 5.2, 4.6]

# Initialize the plot layout
plt.figure(figsize=(10, 6))

# Plot each data trend line
plt.plot(years, total_gdp_share, marker='o', label='Total Energy Expenditure', color='#1f77b4', linewidth=3, markersize=7)
plt.plot(years, crude_oil_share, marker='s', label='Crude Oil (Petroleum)', color='#d62728', linewidth=2, linestyle='--')
plt.plot(years, non_crude_share, marker='^', label='Non-Crude (Gas, Coal, Renewables)', color='#2ca02c', linewidth=2, linestyle='-.')

# Title and axis customization
plt.title('Energy Expenditure Shares of World GDP (1979-2024)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Share of World GDP (%)', fontsize=12)

# Axis limits and grid properties
plt.ylim(0, 12)
plt.xticks(years)
plt.grid(True, linestyle=':', alpha=0.6)

# Display the legend
plt.legend(loc='upper right', frameon=True, shadow=False)

# Render and optimize layout
plt.tight_layout()
plt.show()
