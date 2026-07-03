import matplotlib.pyplot as plt

# Defined in constant 2021 international dollars (PPP)
years = [-6000, 1600, 1825, 1950, 1990, 2022]
gdp_values = [1.6e9, 770e9, 1.75e12, 12.4e12, 51.0e12, 164.0e12]
milestone_labels = ['$1.6 Billion', '$770 Billion', '$1.75 Trillion', '$12.4 Trillion', '$51 Trillion', '$164 Trillion']

# Projections based on the growth rate from the last period (1990 to 2022)
# Growth factor = 164 / 51 = 3.2157 times in 32 years.
# Annual growth rate r = (3.2157)**(1/32) - 1 ≈ 3.725%
# Let's project to $1 Quadrillion (1e15) and $10 Quadrillion (1e16)
# Year for $1 Quadrillion: 2022 + log(1000/164) / log(1.03725) ≈ 2022 + 49.7 ≈ 2072
# Year for $10 Quadrillion: 2022 + log(10000/164) / log(1.03725) ≈ 2022 + 112.5 ≈ 2135
proj_years = [2022, 2072, 2135]
proj_gdp_values = [164.0e12, 1e15, 10e15]
proj_milestone_labels = ['$1 Quadrillion', '$10 Quadrillion']

# Set up the plot layout and size
plt.figure(figsize=(12, 8))

# Plot the historical timeline using a solid line with markers
plt.plot(years, gdp_values, marker='o', linestyle='-', color='#1f77b4', linewidth=2, markersize=8, label='Historical GDP')

# Plot the projection timeline using a dotted line with markers
plt.plot(proj_years, proj_gdp_values, marker='o', linestyle='--', color='#d62728', linewidth=2, markersize=8, label='Projected Trend (~3.7% annual growth)')

# Use a logarithmic scale for the Y-axis to easily visualize exponential growth
plt.yscale('log')

# Format the X-axis labels to handle BCE/CE notation cleanly
def format_year(x, pos):
    if x < 0:
        return f"{abs(int(x))} BCE"
    return f"{int(x)} CE"

plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(format_year))

# Set explicit Y-axis ticks matching our milestones
all_gdp_values = gdp_values + proj_gdp_values[1:]
all_milestone_labels = milestone_labels + proj_milestone_labels
plt.yticks(all_gdp_values, all_milestone_labels)

# Add titles and axis labels
plt.title("Timeline of World GDP & Projections\n(Constant 2021 International Dollars, PPP-adjusted)", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Year / Era", fontsize=12)
plt.ylabel("Global GDP (Log Scale)", fontsize=12)

# Annotate each historical point on the chart for direct scannability
for year, gdp, label in zip(years, gdp_values, milestone_labels):
    year_str = f"{abs(year)} BCE" if year < 0 else f"{year}"
    # Avoid overlapping
    if year == 2022:
        xytext_val = (-85, 10)
    elif year == 1990:
        xytext_val = (-85, -15)
    else:
        xytext_val = (10, 5)
        
    plt.annotate(f"{label}\n({year_str})", 
                 xy=(year, gdp), 
                 xytext=xytext_val, 
                 textcoords='offset points', 
                 fontsize=9,
                 fontweight='semibold',
                 bbox=dict(boxstyle="round,pad=0.3", fc="yellow", alpha=0.2))

# Annotate projection milestones
for year, gdp, label in zip(proj_years[1:], proj_gdp_values[1:], proj_milestone_labels):
    year_str = f"{year}"
    if year == 2135:
        xytext_val = (-105, -15)
    else:
        xytext_val = (-105, 10)
        
    plt.annotate(f"{label}\n({year_str} CE)", 
                 xy=(year, gdp), 
                 xytext=xytext_val, 
                 textcoords='offset points', 
                 fontsize=9,
                 fontweight='semibold',
                 bbox=dict(boxstyle="round,pad=0.3", fc="orange", alpha=0.2))

# Adjust limits slightly for better spacing
plt.xlim(-7000, 2200)

# Add background grids for better tracking
plt.grid(True, which="both", ls="--", alpha=0.5)

# Add legend
plt.legend(loc='upper left', fontsize=11)

# Render and display the visualization
plt.tight_layout()
plt.savefig("C:/Users/ishan/.gemini/antigravity-cli/brain/0d25c235-1f49-4fae-beb6-63eb151d8c75/world_GDP_projected.png", dpi=150)
print("Saved successfully!")
