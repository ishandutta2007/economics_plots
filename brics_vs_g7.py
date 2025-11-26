import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 2025 GDP per capita data (nominal USD) as of late 2025 based on IMF WEO projections
# Values are in USD

g7_data_2025 = {
    'Country': ['United States',      'Japan', 'Germany', 'United Kingdom', 'France', 'Italy', 'Canada'],
    'GDP_per_Capita_PPP_USD': [89105, 54820,    73550,    63760,             66060,    63130,   63170],
    'Population':             [347,   123,      84,       70,                68,       59,      40]
}
brics_data_2025 = {
    'Country':                ['Brazil', 'Russia', 'India', 'China', 'South Africa'   ], #, 'Egypt', 'Ethiopia', 'Iran', 'Saudi Arabia', 'UAE', 'Indonesia'],
    'GDP_per_Capita_PPP_USD': [23310,     49049,    12100,   29190,   16050,          ], #   21760,    4420,       21470,   74668,         48000,  17630]
    'Population':             [212,       144,      1460,    1420,    65,             ]
}

# Create Pandas DataFrames
df_g7 = pd.DataFrame(g7_data_2025)
df_brics = pd.DataFrame(brics_data_2025)

# Calculate initial 2025 averages
g7_avg_2025 = df_g7['GDP_per_Capita_PPP_USD'].mean()
brics_avg_2025 = df_brics['GDP_per_Capita_PPP_USD'].mean()

# Assumed average annual real GDP per capita growth rates (illustrative, based on reports)
# BRICS emerging economies generally have higher growth rates than developed G7 economies
G7_AVG_GROWTH_RATE = 0.015  # 1.5%
BRICS_AVG_GROWTH_RATE = 0.045 # 4.5%

# Generate projected data points from 2025 to 2050
years = np.arange(2025, 2051)
g7_projections = [g7_avg_2025 * (1 + G7_AVG_GROWTH_RATE)**(y - 2025) for y in years]
brics_projections = [brics_avg_2025 * (1 + BRICS_AVG_GROWTH_RATE)**(y - 2025) for y in years]

# Plotting the data
plt.figure(figsize=(10, 6))

g7_line, = plt.plot(years, g7_projections, label=f'G7 (Avg Growth {G7_AVG_GROWTH_RATE*100:.1f}%)', marker='o', linestyle='-', markersize=4)

# Annotate G7 points
for i, (x, y) in enumerate(zip(years, g7_projections)):
    if i % 5 == 0 or i == 0 or i == len(years)-1:  # Annotate every 5 years and first/last points
        plt.annotate(f'${y/1000:.0f}K', 
                    (x, y),
                    textcoords="offset points",
                    xytext=(0,10),
                    ha='center',
                    fontsize=8,
                    color=g7_line.get_color())
brics_line, = plt.plot(years, brics_projections, label=f'BRICS(original) (Avg Growth {BRICS_AVG_GROWTH_RATE*100:.1f}%)', marker='s', linestyle='--', markersize=4)

# Annotate BRICS points
for i, (x, y) in enumerate(zip(years, brics_projections)):
    if i % 5 == 0 or i == 0 or i == len(years)-1:  # Annotate every 5 years and first/last points
        plt.annotate(f'${y/1000:.0f}K', 
                    (x, y),
                    textcoords="offset points",
                    xytext=(0,-15),
                    ha='center',
                    fontsize=8,
                    color=brics_line.get_color())

# Customizing the plot
plt.xlabel('Year', fontsize=12)
plt.ylabel('Projected Average GDP per Capita (USD, PPP)', fontsize=12)
plt.title('G7 vs BRICS GDP per Capita Projections (2025-2050)')
plt.legend(fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(years[::5])  # Show x-ticks every 5 years for better readability
plt.tight_layout()

# Show the plot
plt.show()
