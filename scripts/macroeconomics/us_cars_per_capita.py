import pandas as pd
import matplotlib.pyplot as plt

# Data points based on historical FHWA (Federal Highway Administration) and U.S. Census Bureau data
years = [1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020, 2024]
population_millions = [92.4, 106.5, 123.1, 132.1, 151.7, 180.7, 205.1, 227.2, 249.6, 282.2, 309.3, 331.5, 336.7]
registered_vehicles_millions = [0.47, 9.24, 26.75, 32.47, 49.30, 74.46, 111.24, 161.49, 193.30, 225.82, 250.07, 275.92, 297.53]

# Calculate per capita
vehicles_per_capita = [v / p for v, p in zip(registered_vehicles_millions, population_millions)]

# Create dataframe
df = pd.DataFrame({
    'Year': years,
    'US_Population_Millions': population_millions,
    'Registered_Vehicles_Millions': registered_vehicles_millions,
    'Vehicles_Per_Capita': vehicles_per_capita
})

# Save to CSV as per guidelines
df.to_csv('data/us_vehicles_per_capita_historical.csv', index=False)

# Plotting using subplots (avoiding .figure() as per guidelines)
fig, ax1 = plt.subplots(figsize=(14, 8))

color_pop = '#1f77b4'
color_veh = '#ff7f0e'
color_cap = '#2ca02c'

# Plot population and registrations on ax1
ax1.plot(df['Year'], df['US_Population_Millions'], color=color_pop, linestyle='--', marker='o', label='U.S. Population (Millions)')
ax1.plot(df['Year'], df['Registered_Vehicles_Millions'], color=color_veh, linestyle='-', marker='s', label='Registered Vehicles (Millions)')
ax1.set_xlabel('Year', fontsize=12, fontweight='bold')
ax1.set_ylabel('Count (Millions)', fontsize=12, fontweight='bold')
ax1.tick_params(axis='y')
ax1.grid(True, linestyle=':', alpha=0.6)

# Create a second axis for per capita
ax2 = ax1.twinx()
ax2.plot(df['Year'], df['Vehicles_Per_Capita'], color=color_cap, linestyle='-.', marker='^', linewidth=2, label='Vehicles Per Capita')
ax2.set_ylabel('Vehicles Per Capita', color=color_cap, fontsize=12, fontweight='bold')
ax2.tick_params(axis='y', labelcolor=color_cap)

# Annotate points to make them readable and non-overlapping
for i, txt in enumerate(df['Vehicles_Per_Capita']):
    ax2.annotate(f"{txt:.2f}", (df['Year'].iloc[i], df['Vehicles_Per_Capita'].iloc[i]),
                 textcoords="offset points", xytext=(0,10), ha='center', fontsize=9,
                 color=color_cap, weight='bold', bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=color_cap, lw=0.5, alpha=0.8))

for i, txt in enumerate(df['Registered_Vehicles_Millions']):
    ax1.annotate(f"{txt:.1f}M", (df['Year'].iloc[i], df['Registered_Vehicles_Millions'].iloc[i]),
                 textcoords="offset points", xytext=(-10,-15), ha='center', fontsize=9, color=color_veh)

# Title and legends
plt.title("U.S. Population vs. Registered Vehicles & Vehicles Per Capita (1910-2024)", fontsize=14, fontweight='bold', pad=20)
fig.tight_layout()

plt.show()
# Save plot instead of show()
# plt.savefig('us_vehicles_per_capita_plot.png', dpi=300)
print("Saved CSV and Plot successfully.")
