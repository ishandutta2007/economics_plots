import matplotlib.pyplot as plt
import numpy as np

# Defined in constant 2021 international dollars (PPP)
years = [-6000, 1600, 1825, 1950, 1990, 2022]
gdp_values = [1.6e9, 770e9, 1.75e12, 12.4e12, 51.0e12, 164.0e12]
milestone_labels = ['$1.6 Billion', '$770 Billion', '$1.75 Trillion', '$12.4 Trillion', '$51 Trillion', '$164 Trillion']

# Projections to reach
proj_milestone_labels = ['$1 Quadrillion', '$10 Quadrillion']

# Projection 1: Constant Growth Rate (~3.725% annual growth based on 1990-2022)
years_const = [2022, 2072, 2135]
gdp_const = [164.0e12, 1e15, 10e15]

# Projection 2: Accelerating Growth Rate (calculated dynamically)
# Fit a quadratic curve to the log of the modern GDP data (1825 to 2022)
modern_mask = [y >= 1825 for y in years]
modern_years = np.array(years)[modern_mask]
modern_gdp = np.array(gdp_values)[modern_mask]

# log(GDP) = C*t^2 + B*t + A
C, B, A = np.polyfit(modern_years, np.log(modern_gdp), 2)

# Dynamic acceleration (rate of change of the annual growth rate = 2 * C)
acceleration = 2 * C

# Solve for the exact years when the quadratic model crosses $1 Quadrillion and $10 Quadrillion
years_acc = [2022]
gdp_acc = [164.0e12]
for target in [1e15, 10e15]:
    target_log = np.log(target)
    roots = np.roots([C, B, A - target_log])
    future_roots = [r for r in roots if r > 2022]
    years_acc.append(int(round(future_roots[0])))
    gdp_acc.append(target)

# Generate dense curves for plotting the projection lines smoothly
t_range_const = np.linspace(2022, years_const[-1], 100)
x_const = t_range_const - 2022
gdp_curve_const = 164.0e12 * (1.03725 ** x_const)

# For the accelerating projection, we follow the quadratic model from 2022 onwards
t_range_acc = np.linspace(2022, years_acc[-1], 100)
gdp_curve_acc = np.exp(C * (t_range_acc ** 2) + B * t_range_acc + A)

# Set up the plot layout and size
plt.figure(figsize=(13, 9))

# Plot historical data
plt.plot(years, gdp_values, marker='o', linestyle='-', color='#1f77b4', linewidth=2.5, markersize=8, label='Historical GDP')

# Plot Projection 1 (Constant growth rate)
plt.plot(t_range_const, gdp_curve_const, linestyle=':', color='#d62728', linewidth=2, label='Constant Trend (~3.7% growth)')
plt.scatter(years_const[1:], gdp_const[1:], color='#d62728', marker='o', s=60, zorder=5)

# Plot Projection 2 (Accelerating growth rate)
plt.plot(t_range_acc, gdp_curve_acc, linestyle='--', color='#2ca02c', linewidth=2, label=f'Accelerating Trend (dynamic fit, +{acceleration*100:.4f}% growth/yr)')
plt.scatter(years_acc[1:], gdp_acc[1:], color='#2ca02c', marker='s', s=60, zorder=5)

# Use logarithmic scale on Y axis
plt.yscale('log')

# Format the X-axis labels
def format_year(x, pos):
    if x < 0:
        return f"{abs(int(x))} BCE"
    return f"{int(x)} CE"

plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(format_year))

# Set explicit Y-axis ticks matching milestones
all_gdp_values = gdp_values + [1e15, 10e15]
all_milestone_labels = milestone_labels + ['$1 Quadrillion', '$10 Quadrillion']
plt.yticks(all_gdp_values, all_milestone_labels)

# Add titles and axis labels
plt.title("Timeline of World GDP & Alternative Projections\n(Constant 2021 International Dollars, PPP-adjusted)", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Year / Era", fontsize=12)
plt.ylabel("Global GDP (Log Scale)", fontsize=12)

# Annotate historical points
for year, gdp, label in zip(years, gdp_values, milestone_labels):
    year_str = f"{abs(year)} BCE" if year < 0 else f"{year}"
    # Adjust annotation positions to prevent overlaps
    if year == 2022:
        xytext_val = (-70, 10)
    elif year == 1990:
        xytext_val = (-70, -15)
    else:
        xytext_val = (10, -10)
        
    plt.annotate(f"{label}\n({year_str})", 
                 xy=(year, gdp), 
                 xytext=xytext_val, 
                 textcoords='offset points', 
                 fontsize=9,
                 fontweight='semibold',
                 bbox=dict(boxstyle="round,pad=0.3", fc="yellow", alpha=0.15))

# Annotate Projection 1 (Constant Growth)
for year, gdp, label in zip(years_const[1:], gdp_const[1:], proj_milestone_labels):
    xytext_val = (10, -15) if year == 2135 else (10, 5)
    plt.annotate(f"{label}\n({year} CE)\n[Constant 3.7%]", 
                 xy=(year, gdp), 
                 xytext=xytext_val, 
                 textcoords='offset points', 
                 fontsize=9,
                 fontweight='semibold',
                 color='#8c1d1d',
                 bbox=dict(boxstyle="round,pad=0.3", fc="#fbebeb", ec="#d62728", alpha=0.8))

# Annotate Projection 2 (Accelerating Growth)
for year, gdp, label in zip(years_acc[1:], gdp_acc[1:], proj_milestone_labels):
    # First (2060 CE) should be higher, last (2102 CE) should be lower
    xytext_val = (-95, -15) if year == years_acc[-1] else (-95, 5)
    plt.annotate(f"{label}\n({year} CE)\n[Accelerating]", 
                 xy=(year, gdp), 
                 xytext=xytext_val, 
                 textcoords='offset points', 
                 fontsize=9,
                 fontweight='semibold',
                 color='#1b5e20',
                 bbox=dict(boxstyle="round,pad=0.3", fc="#e8f5e9", ec="#2ca02c", alpha=0.8))

# Adjust limits to fit the new years
plt.xlim(-7000, max(years_const[-1], years_acc[-1]) + 50)

# Add grids
plt.grid(True, which="both", ls="--", alpha=0.4)

# Legend
plt.legend(loc='upper left', fontsize=11)

# Render and display
plt.tight_layout()
plt.show()




