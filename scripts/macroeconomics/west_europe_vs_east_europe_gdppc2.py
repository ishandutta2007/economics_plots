import matplotlib.pyplot as plt
import numpy as np

# 1. Historical Dataset (1990 - 2024)
years = np.array(list(range(1990, 2025)))

we_gdp = np.array([
    18000, 18500, 19100, 19650, 20350, 21070, 21750, 22480, 23200, 23900,
    24664, 25400, 26150, 26900, 27850, 28871, 29890, 30950, 32010, 32900,
    33796, 34700, 35620, 36580, 37550, 39561, 40800, 42100, 43450, 44850,
    46309, 48000, 49750, 51000, 52200
])

ee_gdp = np.array([
    2800, 2700, 2850, 3000, 3300, 3608, 3850, 4100, 4300, 4450,
    4649, 4900, 5200, 5480, 5720, 5990, 6350, 6800, 7250, 7500,
    7717, 8100, 8500, 8900, 9400, 9944, 10500, 11100, 11800, 12300,
    12812, 14200, 16500, 18400, 20800
])

# 2. Calculate Growth Trends & Projection using Log-Linear Regression
# log(y) = slope * year + intercept  ==> Exponential growth representation
log_we = np.log(we_gdp)
log_ee = np.log(ee_gdp)

slope_we, intercept_we = np.polyfit(years, log_we, 1)
slope_ee, intercept_ee = np.polyfit(years, log_ee, 1)

# Find exact year of convergence: slope_we * t + int_we = slope_ee * t + int_ee
conv_year = int(np.ceil((intercept_ee - intercept_we) / (slope_we - slope_ee)))
future_years = np.array(list(range(2025, conv_year + 1)))

# Project future values
we_future = np.exp(slope_we * future_years + intercept_we)
ee_future = np.exp(slope_ee * future_years + intercept_ee)

# Combine datasets for unified plot arrays
all_years = np.concatenate((years, future_years))

# 3. Plotting Configuration
plt.figure(figsize=(16, 10))

# Plot historical curves
plt.plot(years, we_gdp, marker='o', color='royalblue', label='Western Europe (Historical)', linewidth=2)
plt.plot(years, ee_gdp, marker='s', color='darkorange', label='Eastern Europe (Historical)', linewidth=2)

# Plot projected convergence curves
plt.plot(future_years, we_future, linestyle=':', color='royalblue', alpha=0.7, linewidth=2, label='Western Europe (Projection)')
plt.plot(future_years, ee_future, linestyle=':', color='darkorange', alpha=0.7, linewidth=2, label='Eastern Europe (Projection)')

# Highlight the convergence intersection point
convergence_value = np.exp(slope_we * conv_year + intercept_we)
plt.scatter(conv_year, convergence_value, color='crimson', zorder=5, s=120, edgecolors='black')
plt.annotate(f'Convergence\nYear: {conv_year}\n~${int(convergence_value):,}',
             xy=(conv_year, convergence_value),
             xytext=(conv_year - 8, convergence_value + 30000),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontweight='bold', bbox=dict(boxstyle="round,pad=0.3", fc="yellow", alpha=0.3))

# 4. Annotate All Historical Data Points
# Utilizing a minor alternate offset to prevent overlap on the log scale
for y, we, ee in zip(years, we_gdp, ee_gdp):
    plt.text(y, we * 1.08, f"${we:,}", fontsize=7, color='blue', ha='center', va='bottom', rotation=45)
    plt.text(y, ee * 0.82, f"${ee:,}", fontsize=7, color='darkred', ha='center', va='top', rotation=45)

# 5. Styling and Customization
plt.yscale('log')
plt.title('GDP per Capita Trend & Convergence Projection (Log Scale)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12, labelpad=10)
plt.ylabel('GDP per Capita (USD) - Logarithmic Scale', fontsize=12, labelpad=10)

# Generate explicit ticks for clarity across the log scale range
plt.xticks(np.arange(1990, conv_year + 5, 5), rotation=45)
y_ticks = [2000, 5000, 10000, 20000, 50000, 100000, 200000]
plt.yticks(y_ticks, [f"${tick:,}" for tick in y_ticks])

plt.grid(True, which="both", ls="--", alpha=0.5)
plt.legend(loc='upper left', fontsize=11)
plt.tight_layout()

# Display the graph
plt.show()
