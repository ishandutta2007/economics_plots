import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

# ---------------------------------------------------------
# 1. Define Historical Data Points (Nominal GDP per capita in USD)
# Sources: World Bank, Macrotrends, Maddison Project (estimates), 
# and Govt of India economic history data.
# ---------------------------------------------------------

# USA Data Points (Year: GDP per capita)
usa_data = {
    1937: 721, 1938: 672, 1939: 713, 1940: 779, 1941: 969, 
    1942: 1231, 1943: 1485, 1944: 1622, 1945: 1629, 1946: 1609,
    1947: 1732, 1948: 1872, 1949: 1826, 1950: 1977, 1955: 2574,
    1960: 3001, 1965: 3819, 1970: 5233, 1975: 7801, 1980: 12547,
    1985: 18192, 1990: 23835, 1995: 28690, 2000: 36334, 2005: 44114,
    2010: 48373, 2015: 56803, 2020: 63027, 2021: 69287, 2022: 76398,
    2023: 81695, 2024: 85373, 2025: 92266  # 2025 Estimate
}

# India Data Points (Year: GDP per capita)
# Note: 1937-1947 estimates based on historical stagnation (~0.1% growth).
# 1960+ data from World Bank/Macrotrends.
india_data = {
    1937: 58,   # Estimate based on 1947 figure and low growth
    1947: 60,   # Independence year figure
    1950: 65,   # Estimate
    1960: 82,   # World Bank start
    1965: 119, 1970: 112, 1975: 158, 1980: 267,
    1985: 296, 1990: 368, 1995: 373, 2000: 443,
    2005: 707, 2010: 1357, 2015: 1605, 2020: 1933,
    2021: 2256, 2022: 2410, 2023: 2612, 2024: 2750, 
    2025: 2900  # 2025 Estimate
}

# ---------------------------------------------------------
# 2. Data Processing & Interpolation
# ---------------------------------------------------------

# Create a full range of years
years = np.arange(1937, 2026)

# Helper function to interpolate missing years
def get_interpolated_values(data_dict, target_years):
    known_years = sorted(data_dict.keys())
    known_values = [data_dict[y] for y in known_years]
    # Linear interpolation for gaps
    f = interp1d(known_years, known_values, kind='linear', fill_value="extrapolate")
    return f(target_years)

# Get continuous GDP arrays
usa_gdp_continuous = get_interpolated_values(usa_data, years)
india_gdp_continuous = get_interpolated_values(india_data, years)

# Calculate Ratio (USA / India)
ratio = usa_gdp_continuous / india_gdp_continuous

# ---------------------------------------------------------
# 3. Plotting
# ---------------------------------------------------------

plt.figure(figsize=(12, 6))
plt.plot(years, ratio, color='#2c3e50', linewidth=2.5, label='USA/India GDP Ratio')

# Highlight Key Dates
key_years = [1947, 1991, 2000, 2025]
for year in key_years:
    if year in years:
        val = ratio[year - 1937]
        plt.plot(year, val, 'ro')  # Red dot
        plt.annotate(f"{year}\n{val:.1f}x", 
                     (year, val), 
                     xytext=(0, 10), 
                     textcoords='offset points', 
                     ha='center', 
                     fontsize=9, 
                     fontweight='bold')

# Styling
plt.title('Income Gap: Ratio of USA vs. India GDP Per Capita (1937-2025)', fontsize=14, pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Ratio (USA GDP is X times larger)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.fill_between(years, ratio, color='#3498db', alpha=0.1)  # Shading
plt.axhline(y=np.min(ratio), color='green', linestyle=':', label=f'Min Ratio: {np.min(ratio):.1f}x')
plt.axhline(y=np.max(ratio), color='red', linestyle=':', label=f'Max Ratio: {np.max(ratio):.1f}x')
plt.legend()

plt.tight_layout()
plt.show()
