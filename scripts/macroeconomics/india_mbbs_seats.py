import matplotlib.pyplot as plt

# 1. Historical Dataset
years = [1996, 2000, 2005, 2010, 2015, 2020, 2021, 2022, 2023, 2024, 2025, 2026]
intake_capacity = [13000, 18000, 25500, 34000, 54500, 83400, 91800, 98600, 108900, 118100, 128900, 136939]
population_billions = [0.971, 1.050, 1.150, 1.230, 1.310, 1.380, 1.390, 1.400, 1.420, 1.430, 1.440, 1.450]

# 2. Initialize Side-by-Side Subplots (1 Row, 2 Columns)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

color_intake = '#1f77b4'  # Deep Blue
color_pop = '#d62728'     # Vivid Crimson

# =========================================================================
# LEFT PANEL: MBBS INTAKE CAPACITY
# =========================================================================
ax1.plot(years, intake_capacity, color=color_intake, marker='o', linewidth=3, markersize=7, label="Intake Capacity")
ax1.set_title("India's Annual MBBS Intake Capacity", fontsize=13, fontweight='bold', color=color_intake, pad=15)
ax1.set_xlabel("Year", fontsize=11, fontweight='bold')
ax1.set_ylabel("Seats Available", fontsize=11, fontweight='bold')
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)
ax1.yaxis.set_major_formatter('{x:,.0f}')
ax1.grid(True, linestyle=':', alpha=0.5)

# Annotate points for Intake Capacity
for x, y in zip(years, intake_capacity):
    ax1.annotate(f"{y:,.0f}", 
                 xy=(x, y), 
                 xytext=(0, 10), 
                 textcoords='offset points', 
                 ha='center', va='bottom',
                 fontsize=8.5, fontweight='bold', color=color_intake,
                 bbox=dict(boxstyle='round,pad=0.2', fc='#edf8ff', alpha=0.8, ec=color_intake, lw=0.5))

# Vertical Broken Dotted Delta Indicator at 2026 Axis Level
# Lower segment (1996 baseline height to text box)
ax1.plot([2026, 2026], [13000, 50000], color=color_intake, linestyle=":", linewidth=2, marker='v', markevery=[0])
# Upper segment (text box to 2026 peak height)
ax1.plot([2026, 2026], [90000, 136939], color=color_intake, linestyle=":", linewidth=2, marker='^', markevery=[1])

# Text callout bridging the break in the vertical line
ax1.text(2026, 70000, "10.5x Growth", 
         color=color_intake, fontsize=10, fontweight='bold', ha='center', va='center',
         bbox=dict(boxstyle='square,pad=0.3', fc='white', alpha=1.0, ec=color_intake, lw=1))

ax1.set_ylim(0, 160000)

# =========================================================================
# RIGHT PANEL: TOTAL POPULATION GROWTH
# =========================================================================
ax2.plot(years, population_billions, color=color_pop, marker='s', linestyle='--', linewidth=2.5, markersize=7, label="Total Population")
ax2.set_title("India's Total Population Growth Curve", fontsize=13, fontweight='bold', color=color_pop, pad=15)
ax2.set_xlabel("Year", fontsize=11, fontweight='bold')
ax2.set_ylabel("Population (in Billions)", fontsize=11, fontweight='bold')
ax2.set_xticks(years)
ax2.set_xticklabels(years, rotation=45)
ax2.grid(True, linestyle=':', alpha=0.5)

# Annotate points for Population
for x, y in zip(years, population_billions):
    ax2.annotate(f"{y:.3f}B", 
                 xy=(x, y), 
                 xytext=(0, -18), 
                 textcoords='offset points', 
                 ha='center', va='top',
                 fontsize=8.5, fontweight='bold', color=color_pop,
                 bbox=dict(boxstyle='round,pad=0.2', fc='#fff5f5', alpha=0.8, ec=color_pop, lw=0.5))

# Vertical Broken Dotted Delta Indicator at 2026 Axis Level
# Lower segment (1996 baseline height to text box)
ax2.plot([2026, 2026], [0.971, 1.130], color=color_pop, linestyle=":", linewidth=2, marker='v', markevery=[0])
# Upper segment (text box to 2026 peak height)
ax2.plot([2026, 2026], [1.270, 1.450], color=color_pop, linestyle=":", linewidth=2, marker='^', markevery=[1])

# Text callout bridging the break in the vertical line
ax2.text(2026, 1.200, "1.49x Growth", 
         color=color_pop, fontsize=10, fontweight='bold', ha='center', va='center',
         bbox=dict(boxstyle='square,pad=0.3', fc='white', alpha=1.0, ec=color_pop, lw=1))

ax2.set_ylim(0.8, 1.65)

# =========================================================================
# GLOBAL CANVAS ADJUSTMENTS
# =========================================================================
plt.suptitle("Side-by-Side Divergence Analysis: Medical Infrastructure vs. Population (1996–2026)", 
             fontsize=15, fontweight='bold', y=0.98)

plt.tight_layout()
plt.show()
