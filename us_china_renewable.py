import matplotlib.pyplot as plt

# Years for the X-axis (Historical + 10-year Projection)
years = list(range(2015, 2036))

# Estimated Renewable Capacity in Gigawatts (GW)
# Data includes Solar, Wind, and Hydro
# Based on 2025/2026 IEA/EIA/GlobalData estimates
china_capacity = [
    520, 580, 650, 728, 790, 934, 1063, 1200, 1450, 1700, # 2015-2024
    2050, 2250, 2450, 2650, 2850, 3050, 3250, 3400, 3550, 3700, 3850 # 2025-2035 (Projected)
]

us_capacity = [
    210, 230, 250, 275, 300, 335, 370, 410, 440, 480, # 2015-2024
    520, 560, 610, 660, 710, 760, 810, 870, 930, 990, 1060 # 2025-2035 (Projected)
]

# Create the plot
plt.figure(figsize=(12, 7))

# Plot historical and projected data
plt.plot(years, china_capacity, label='China (Historical + Projected)', color='#de2910', linewidth=2.5, marker='o', markevery=[10])
plt.plot(years, us_capacity, label='U.S. (Historical + Projected)', color='#3c3b6e', linewidth=2.5, marker='o', markevery=[10])

# Highlight the projection start (2026)
plt.axvline(x=2026, color='gray', linestyle='--', alpha=0.6)
plt.text(2026.5, 2000, 'Projection Starts (2026)', rotation=90, verticalalignment='center', color='gray')

# Formatting the Chart
plt.title('Renewable Energy Capacity Growth: U.S. vs. China (2015-2035)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Installed Capacity (Gigawatts - GW)', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper left', fontsize=11)

# Adding Annotations for 2035 Targets
plt.annotate(f'{china_capacity[-1]} GW', xy=(2035, china_capacity[-1]), xytext=(2031, china_capacity[-1]+100),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5))
plt.annotate(f'{us_capacity[-1]} GW', xy=(2035, us_capacity[-1]), xytext=(2031, us_capacity[-1]-200),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5))

plt.tight_layout()
plt.show()