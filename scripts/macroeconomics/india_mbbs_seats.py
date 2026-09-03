import matplotlib.pyplot as plt

# 1. Historical Dataset
years = [1996, 2000, 2005, 2010, 2015, 2020, 2021, 2022, 2023, 2024, 2025, 2026]
intake_capacity = [13000, 18000, 25500, 34000, 54500, 83400, 91800, 98600, 108900, 118100, 128900, 136939]

# Population converted to raw integers (e.g., 1.45B = 1,450,000,000) for a unified scale
population_raw = [971000000, 1050000000, 1150000000, 1230000000, 1310000000, 1380000000, 
                  1390000000, 1400000000, 1420000000, 1430000000, 1440000000, 1450000000]

# 2. Plot Initialization
fig, ax = plt.subplots(figsize=(15, 9))

color_intake = '#1f77b4'  # Deep Blue
color_pop = '#d62728'     # Vivid Crimson

# 3. Plot Lines
ax.plot(years, intake_capacity, color=color_intake, marker='o', linewidth=3, markersize=8, label="MBBS Intake Capacity")
ax.plot(years, population_raw, color=color_pop, marker='s', linestyle='--', linewidth=2.5, markersize=8, label="Total Population")

# 4. Set Y-Axis to Logarithmic Scale
ax.set_yscale('log')

# 5. Annotate Points (Properly formatted raw numbers)
for x, y in zip(years, intake_capacity):
    ax.annotate(f"{y:,.0f}", 
                xy=(x, y), 
                xytext=(0, 12), 
                textcoords='offset points', 
                ha='center', va='bottom',
                fontsize=9, fontweight='bold', color=color_intake,
                bbox=dict(boxstyle='round,pad=0.2', fc='#edf8ff', alpha=0.8, ec=color_intake, lw=0.5))

for x, y in zip(years, population_raw):
    # Convert back to readable Billions for the annotation label
    billions_label = f"{y / 1e9:.3f}B"
    ax.annotate(billions_label, 
                xy=(x, y), 
                xytext=(0, -22), 
                textcoords='offset points', 
                ha='center', va='top',
                fontsize=9, fontweight='bold', color=color_pop,
                bbox=dict(boxstyle='round,pad=0.2', fc='#fff5f5', alpha=0.8, ec=color_pop, lw=0.5))

# 6. Formatting & Readability Adjustments
ax.set_title("Logarithmic Comparison: India's MBBS Seat Expansion vs. Total Population (1996–2026)", 
             fontsize=15, fontweight='bold', pad=25)
ax.set_xlabel("Year", fontsize=12, fontweight='bold', labelpad=12)
ax.set_ylabel("Absolute Value Scale (Logarithmic Base-10)", fontsize=12, fontweight='bold', labelpad=12)

# Format the log y-axis labels cleanly instead of scientific notation (e.g., 10^4 becomes 10,000)
from matplotlib.ticker import FuncFormatter
ax.get_yaxis().set_major_formatter(FuncFormatter(lambda x, p: format(int(x), ',')))

# Refine ticks
ax.set_xticks(years)
ax.grid(True, which="both", linestyle=':', alpha=0.5, color='gray') # 'both' ensures major and minor log grid lines appear
ax.legend(loc='center left', fontsize=12, frameon=True, shadow=True, facecolor='white')

# Set vertical boundaries to encompass both thousands (seats) and billions (population) cleanly
ax.set_ylim(5000, 5000000000)

plt.tight_layout()
plt.show()
