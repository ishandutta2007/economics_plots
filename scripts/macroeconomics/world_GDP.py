import matplotlib.pyplot as plt

# Define the historical data milestones
# Note: -6000 represents 6000 BCE
years = [-6000, 1600, 1825, 1950, 1990, 2022]
gdp_values = [1e9, 10e9, 100e9, 1e12, 10e12, 100e12]
milestone_labels = ['$1 Billion', '$10 Billion', '$100 Billion', '$1 Trillion', '$10 Trillion', '$100 Trillion']

# Set up the plot layout and size
plt.figure(figsize=(12, 7))

# Plot the timeline using a line with markers
plt.plot(years, gdp_values, marker='o', linestyle='-', color='#1f77b4', linewidth=2, markersize=8)

# Use a logarithmic scale for the Y-axis to easily visualize exponential growth
plt.yscale('log')

# Format the X-axis labels to handle BCE/CE notation cleanly
def format_year(x, pos):
    if x < 0:
        return f"{abs(int(x))} BCE"
    return f"{int(x)} CE"

plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(format_year))

# Set explicit Y-axis ticks matching our milestones
plt.yticks(gdp_values, milestone_labels)

# Add titles and axis labels
plt.title("Timeline of World GDP Milestones\n(Constant 2021 International Dollars)", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Year / Era", fontsize=12)
plt.ylabel("Global GDP Milestone (Log Scale)", fontsize=12)

# Annotate each point on the chart for direct scannability
for year, gdp, label in zip(years, gdp_values, milestone_labels):
    year_str = f"{abs(year)} BCE" if year < 0 else f"{year}"
    plt.annotate(f"{label}\n({year_str})", 
                 xy=(year, gdp), 
                 xytext=(15, -10) if year == 2022 else (10, 5), 
                 textcoords='offset points', 
                 fontsize=9,
                 fontweight='semibold',
                 bbox=dict(boxstyle="round,pad=0.3", fc="yellow", alpha=0.2))

# Adjust limits slightly for better spacing
plt.xlim(-7000, 2100)

# Add background grids for better tracking
plt.grid(True, which="both", ls="--", alpha=0.5)

# Render and display the visualization
plt.tight_layout()
plt.show()
