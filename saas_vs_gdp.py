
import matplotlib.pyplot as plt
import numpy as np

# SaaS Market Size Data from Precedence Research
saas_years = np.arange(2024, 2035)
saas_market_size_2024 = 358.33
saas_market_size_2025 = 408.21
saas_cagr = 0.1332

# Calculate SaaS market size for the forecast period
saas_market_size = [saas_market_size_2024, saas_market_size_2025]
for year in range(2026, 2035):
    saas_market_size.append(saas_market_size[-1] * (1 + saas_cagr))

# World GDP Data
gdp_years = np.arange(2024, 2035)
gdp_2023 = 105  # in trillion USD
gdp_growth_2024_2025 = 0.032
gdp_growth_2026_onwards = 0.030

world_gdp = [gdp_2023 * (1 + gdp_growth_2024_2025)] # GDP for 2024
world_gdp.append(world_gdp[-1] * (1 + gdp_growth_2024_2025)) # GDP for 2025

for year in range(2026, 2035):
    world_gdp.append(world_gdp[-1] * (1 + gdp_growth_2026_onwards))

# Create the plot
fig, ax1 = plt.subplots(figsize=(12, 7))

# Plot SaaS Market Size
color = 'tab:blue'
ax1.set_xlabel('Year')
ax1.set_ylabel('SaaS Market Size (Billion USD)', color=color)
ax1.plot(saas_years, saas_market_size, marker='o', linestyle='-', color=color, label='SaaS Market Size')
ax1.tick_params(axis='y', labelcolor=color)
ax1.grid(True)

# Create a second y-axis for World GDP
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('World GDP (Trillion USD)', color=color)
ax2.plot(gdp_years, world_gdp, marker='o', linestyle='-', color=color, label='World GDP')
ax2.tick_params(axis='y', labelcolor=color)

# Add titles and legend
plt.title('SaaS Market Size vs. World GDP (2024-2034)')
fig.tight_layout()
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))

plt.show()
# Save the plot
# plt.savefig('saas_vs_world_gdp.png')

print("Plot saved as saas_vs_world_gdp.png")
