import pandas as pd
import matplotlib.pyplot as plt

# US Historical Series
us_years = [1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020, 2024]
us_pop = [92.4, 106.5, 123.1, 132.1, 151.7, 180.7, 205.1, 227.2, 249.6, 282.2, 309.3, 331.5, 336.7]
us_veh = [0.47, 9.24, 26.75, 32.47, 49.30, 74.46, 111.24, 161.49, 193.30, 225.82, 250.07, 275.92, 297.53]
us_capita = [v / p for v, p in zip(us_veh, us_pop)]

# India Historical Series
in_years = [1951, 1961, 1971, 1981, 1991, 2001, 2011, 2021, 2025]
in_pop = [361.1, 439.2, 548.2, 683.3, 846.3, 1028.7, 1210.6, 1393.4, 1450.0]
in_veh = [0.16, 0.31, 0.68, 1.16, 2.95, 7.05, 19.23, 45.16, 52.51]
in_capita = [v / p for v, p in zip(in_veh, in_pop)]

# Clean tabular packaging
df_us = pd.DataFrame({'Year': us_years, 'US_Vehicles_Per_Capita': us_capita})
df_in = pd.DataFrame({'Year': in_years, 'India_Vehicles_Per_Capita': in_capita})
df_combined = pd.merge(df_us, df_in, on='Year', how='outer').sort_values('Year').reset_index(drop=True)

# Export combined data to local workspace 
df_combined.to_csv('combined_vehicles_per_capita.csv', index=False)

# Initialize canvas (avoiding .figure() to follow best practices)
fig, ax = plt.subplots(figsize=(12, 7))
plt.yscale("log")

# Plot structural lines
ax.plot(df_us['Year'], df_us['US_Vehicles_Per_Capita'], color='#1f77b4', linestyle='-', marker='o', linewidth=2.5, label='United States')
ax.plot(df_in['Year'], df_in['India_Vehicles_Per_Capita'], color='#ff7f0e', linestyle='-', marker='s', linewidth=2.5, label='India')

# Sparsely annotate the US trajectory to prevent clutter
for i, txt in enumerate(df_us['US_Vehicles_Per_Capita']):
    if df_us['Year'].iloc[i] in [1910, 1950, 1980, 2000, 2024]:
        ax.annotate(f"{txt:.2f}", (df_us['Year'].iloc[i], df_us['US_Vehicles_Per_Capita'].iloc[i]),
                     textcoords="offset points", xytext=(0, 10), ha='center', fontsize=9, fontweight='bold', color='#1f77b4')

# Sparsely annotate India's key macroeconomic inflection points
for i, txt in enumerate(df_in['India_Vehicles_Per_Capita']):
    if df_in['Year'].iloc[i] in [1951, 1991, 2011, 2025]:
        ax.annotate(f"{txt:.3f}", (df_in['Year'].iloc[i], df_in['India_Vehicles_Per_Capita'].iloc[i]),
                     textcoords="offset points", xytext=(0, -16), ha='center', fontsize=9, fontweight='bold', color='#ff7f0e')

# Customizing chart layout aesthetics
ax.set_title("Comparative Motorization Trajectory: US vs. India (Vehicles Per Capita)", fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12, fontweight='bold')
ax.set_ylabel("Vehicles Per Capita", fontsize=12, fontweight='bold')
ax.set_xlim(1900, 2035)
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper left', fontsize=11)

fig.tight_layout()

plt.show()
# Save image file directly to workspace directory
# plt.savefig('combined_vehicles_per_capita_plot.png', dpi=300)