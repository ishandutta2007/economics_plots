
import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.polynomial import polyfit, polyval

# SaaS Market Size Data from Precedence Research
saas_years = np.arange(2024, 2035)
saas_market_size_2024 = 0.35833
saas_market_size_2025 = 0.40821
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

world_gdp = [gdp_2023 * (1 + gdp_growth_2024_2025)]  # GDP for 2024
world_gdp.append(world_gdp[-1] * (1 + gdp_growth_2024_2025))  # GDP for 2025

for year in range(2026, 2035):
    world_gdp.append(world_gdp[-1] * (1 + gdp_growth_2026_onwards))

# --- Extrapolation ---
projection_years = np.arange(2034, 2201)

# SaaS projection
saas_coeffs = polyfit(saas_years, saas_market_size, 2)
saas_projection = polyval(projection_years, saas_coeffs)

# GDP projection
gdp_coeffs = polyfit(gdp_years, world_gdp, 2)
gdp_projection = polyval(projection_years, gdp_coeffs)

# --- Scaling ---
# Convert GDP from trillions to trillions and scale it to be on a similar range as SaaS
gdp_scaling_factor = 1# / (world_gdp[0] / saas_market_size[0])
scaled_world_gdp = [x * gdp_scaling_factor for x in world_gdp]
scaled_gdp_projection = [x * gdp_scaling_factor for x in gdp_projection]


# --- Data Transformation for Log Scale ---
x_saas_years = saas_years - 2023
x_projection_years = projection_years - 2023
x_gdp_years = gdp_years - 2023

# Create the plot
fig, ax1 = plt.subplots(figsize=(12, 7))

# Plot SaaS Market Size
color = 'tab:blue'
ax1.set_xlabel('Year')
ax1.set_xscale("log")
ax1.set_ylabel('Trillions(USD)')
ax1.set_yscale("log")
ax1.plot(x_saas_years, saas_market_size, marker='o', linestyle='-', color=color, label='SaaS Market Size')
ax1.plot(x_projection_years, saas_projection, linestyle='--', color=color)
ax1.tick_params(axis='y')
ax1.grid(True)

# Plot scaled World GDP
color = 'tab:red'
ax1.plot(x_gdp_years, scaled_world_gdp, marker='o', linestyle='-', color=color, label=f'World GDP (Scaled by {gdp_scaling_factor:.2f})')
ax1.plot(x_projection_years, scaled_gdp_projection, linestyle='--', color=color)


# --- Annotations ---
years_to_annotate = [2024, 2030, 2034, 2050, 2100, 2200]
for year in years_to_annotate:
    x_year = year - 2023
    # SaaS annotation
    if year <= saas_years[-1]:
        saas_val = saas_market_size[np.where(saas_years == year)[0][0]]
    else:
        saas_val = saas_projection[np.where(projection_years == year)[0][0]]
    ax1.annotate(f'{saas_val:.2f}', (x_year, saas_val), textcoords="offset points", xytext=(0,-15), va="bottom", ha='center', color='tab:blue')

    # GDP annotation
    if year <= gdp_years[-1]:
        gdp_val = scaled_world_gdp[np.where(gdp_years == year)[0][0]]
    else:
        gdp_val = scaled_gdp_projection[np.where(projection_years == year)[0][0]]
    ax1.annotate(f'{gdp_val:.0f}', (x_year, gdp_val), textcoords="offset points", xytext=(0,10), va="top", ha='center', color='tab:red')

# --- X-axis Ticks ---
tick_years = [2024, 2030, 2040, 2050, 2075, 2100, 2150, 2200]
tick_x_values = [year - 2023 for year in tick_years]
ax1.set_xticks(tick_x_values)
ax1.set_xticklabels(tick_years, rotation=45)


# Add titles and legend
plt.title('SaaS Market Size vs. World GDP with Projection to 2200 (Log Scale X-axis)')
fig.tight_layout()
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))
# Save the plot
# plt.savefig('saas_vs_world_gdp_scaled_annotated.png')
plt.show()

print("Plot saved as saas_vs_world_gdp_scaled_annotated.png")
