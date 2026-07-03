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

# Projection 2: Accelerating Growth Rate
# Historically, the growth rate has been increasing.
# Let's model a growth rate that starts at 3.725% in 2022 and increases by 0.05 percentage points per year (or 0.5% per decade).
# r(t) = 0.03725 + 0.0005 * (t - 2022)
# GDP(t) = 164e12 * exp(0.03725 * x + 0.00025 * x^2) where x = t - 2022
# Crossing 1 Quadrillion: x ≈ 38.6 years -> Year 2061
# Crossing 10 Quadrillion: x ≈ 73.8 years -> Year 2096
years_acc = [2022, 2061, 2096]
gdp_acc = [164.0e12, 1e15, 10e15]

# Generate dense curves for plotting the projection lines smoothly
t_range_const = np.linspace(2022, 2135, 100)
x_const = t_range_const - 2022
gdp_curve_const = 164.0e12 * (1.03725 ** x_const)

t_range_acc = np.linspace(2022, 2096, 100)
x_acc = t_range_acc - 2022
gdp_curve_acc = 164.0e12 * np.exp(0.03725 * x_acc + 0.00025 * (x_acc ** 2))

# Set up the plot layout and size
plt.figure(figsize=(13, 9))

# Plot historical data
plt.plot(years, gdp_values, marker='o', linestyle='-', color='#1f77b4', linewidth=2.5, markersize=8, label='Historical GDP')

# Plot Projection 1 (Constant growth rate)
plt.plot(t_range_const, gdp_curve_const, linestyle=':', color='#d62728', linewidth=2, label='Constant Trend (~3.7% growth)')
plt.scatter(years_const[1:], gdp_const[1:], color='#d62728', marker='o', s=60, zorder=5)

# Plot Projection 2 (Accelerating growth rate)
plt.plot(t_range_acc, gdp_curve_acc, linestyle='--', color='#2ca02c', linewidth=2, label='Accelerating Trend (+0.05% growth/yr)')
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
        xytext_val = (-90, 10)
    elif year == 1990:
        xytext_val = (-90, -15)
    else:
        xytext_val = (10, 5)
        
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
    xytext_val = (-125, 10) if year == 2096 else (-125, -25)
    plt.annotate(f"{label}\n({year} CE)\n[Accelerating]", 
                 xy=(year, gdp), 
                 xytext=xytext_val, 
                 textcoords='offset points', 
                 fontsize=9,
                 fontweight='semibold',
                 color='#1b5e20',
                 bbox=dict(boxstyle="round,pad=0.3", fc="#e8f5e9", ec="#2ca02c", alpha=0.8))

# Adjust limits to fit the new years
plt.xlim(-7000, 2180)

# Add grids
plt.grid(True, which="both", ls="--", alpha=0.4)

# Legend
plt.legend(loc='upper left', fontsize=11)

# Render and display
plt.tight_layout()
plt.show()



