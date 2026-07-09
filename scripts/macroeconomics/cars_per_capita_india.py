import pandas as pd
import matplotlib.pyplot as plt

# Historical decadal data for India (Sources: MoRTH & Census of India / UN Pop)
years = [1951, 1961, 1971, 1981, 1991, 2001, 2011, 2021, 2025]
population_millions = [361.1, 439.2, 548.2, 683.3, 846.3, 1028.7, 1210.6, 1393.4, 1450.0]
registered_vehicles_millions = [0.16, 0.31, 0.68, 1.16, 2.95, 7.05, 19.23, 45.16, 52.51]

# Compute per capita metric
vehicles_per_capita = [v / p for v, p in zip(registered_vehicles_millions, population_millions)]

# Build analytical data frame
df_india = pd.DataFrame({
    'Year': years,
    'India_Population_Millions': population_millions,
    'Registered_Vehicles_Millions': registered_vehicles_millions,
    'Vehicles_Per_Capita': vehicles_per_capita
})

# Export data matrix to workspace CSV
df_india.to_csv('data/india_vehicles_per_capita_historical.csv', index=False)

# Initialize dual-axis plotting engine
fig, ax1 = plt.subplots(figsize=(14, 8))

color_pop = '#1f77b4'  # Slate Blue
color_veh = '#e377c2'  # Indian Pink/Magenta for vehicle curve contrast
color_cap = '#9467bd'  # Deep Amethyst

# Primary Axis: Population & Vehicle Volumes
ax1.plot(df_india['Year'], df_india['India_Population_Millions'], color=color_pop, linestyle='--', marker='o', alpha=0.7, label='India Population (Millions)')
ax1.plot(df_india['Year'], df_india['Registered_Vehicles_Millions'], color=color_veh, linestyle='-', marker='s', alpha=0.8, label='Registered Vehicles (Millions)')
ax1.set_xlabel('Year', fontsize=12, fontweight='bold', labelpad=10)
ax1.set_ylabel('Absolute Count (Millions)', fontsize=12, fontweight='bold', labelpad=10)
ax1.grid(True, linestyle=':', alpha=0.6)

# Secondary Axis: Shared x-axis for Per Capita Adoption Target
ax2 = ax1.twinx()
ax2.plot(df_india['Year'], df_india['Vehicles_Per_Capita'], color=color_cap, linestyle='-.', marker='^', linewidth=2.5, label='Vehicles Per Capita')
ax2.set_ylabel('Vehicles Per Capita', color=color_cap, fontsize=12, fontweight='bold', labelpad=15)
ax2.tick_params(axis='y', labelcolor=color_cap)

# Target Metric Explicit Annotation Blocks (Pillbox formatting to ensure zero truncation)
for i, txt in enumerate(df_india['Vehicles_Per_Capita']):
    ax2.annotate(f"{txt:.3f}", (df_india['Year'].iloc[i], df_india['Vehicles_Per_Capita'].iloc[i]),
                 textcoords="offset points", xytext=(0, 12), ha='center', fontsize=9,
                 color=color_cap, weight='bold', 
                 bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=color_cap, lw=0.5, alpha=0.9))

# Volume Curve Point Annotations (offset below points to maintain axis separation)
for i, txt in enumerate(df_india['Registered_Vehicles_Millions']):
    ax1.annotate(f"{txt:.1f}M", (df_india['Year'].iloc[i], df_india['Registered_Vehicles_Millions'].iloc[i]),
                 textcoords="offset points", xytext=(0, -18), ha='center', fontsize=8, color=color_veh, weight='semibold')

# Composite Legend Generation
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', frameon=True, facecolor='white', framealpha=0.9)

plt.title("India Population Scale vs. Vehicle Motorization Trajectory (1951-2025)", fontsize=14, fontweight='bold', pad=20)
fig.tight_layout()

plt.show()
# Save final render asset directly to working environment
# plt.savefig('india_vehicles_per_capita_plot.png', dpi=300)