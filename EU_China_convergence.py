import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Corrected data alignment (2000-2023 = 24 years)
years = np.arange(2000, 2024)  # Matches 24 data points in your arrays
china_gdp = np.array([1255, 1548, 2009, 2610, 3443, 4444, 5585, 6896, 
                     8229, 9543, 10540, 11270, 11890, 12510, 13130, 13850,
                     14620, 15440, 16310, 17240, 18230, 19290, 20420, 21610])  # 2000-2023

eu_gdp = np.array([28120, 28910, 29740, 30460, 31420, 32350, 33520, 34780,
                  36100, 37420, 38210, 38650, 40210, 41730, 43685, 45620,
                  47610, 49650, 51740, 53880, 56070, 58310, 60600, 62940])  # 2000-2023

# Projection parameters (2024-2070)
future_years = np.arange(2023, 2071)
china_growth = 0.04
eu_growth = 0.014

# Rest of the code remains the same as previous version
china_proj = [china_gdp[-1]] * len(future_years)
eu_proj = [eu_gdp[-1]] * len(future_years)

for i in range(1, len(future_years)):
    china_proj[i] = china_proj[i-1] * (1 + china_growth)
    eu_proj[i] = eu_proj[i-1] * (1 + eu_growth)

# Find convergence point
convergence_point = None
for i, (c, e) in enumerate(zip(china_proj, eu_proj)):
    if c >= e:
        convergence_point = (2023 + i, c)
        break

# Plot configuration
plt.figure(figsize=(12, 7))
plt.title("China-EU GDP Per Capita(PPP) Convergence Projection", fontsize=14, pad=20)
plt.xlabel("Year", fontsize=12)
plt.ylabel("GDP Per Capita (USD)", fontsize=12)
plt.grid(True, alpha=0.3)

plt.yscale('log')

# Plot lines with enhanced styling
china_line, = plt.plot(years, china_gdp, 'g-', lw=2.5, label='China Historical')
eu_line, = plt.plot(years, eu_gdp, 'b-', lw=2.5, label='EU Historical')
plt.plot(future_years, china_proj, 'g--', lw=2, label='China Projection (4% CAGR)')
plt.plot(future_years, eu_proj, 'b--', lw=2, label='EU Projection (1.4% CAGR)')

# Add convergence annotation with formatted tooltip
if convergence_point:
    conv_year, conv_value = convergence_point
    plt.scatter(conv_year, conv_value, color='red', s=100, zorder=5)
    
    # Format value with commas and country labels
    formatted_value = f"${conv_value:,.0f}"
    annotation_text = (f"({formatted_value})\n{conv_year}")
    
    plt.annotate(annotation_text,
                 (conv_year, conv_value),
                 xytext=(15, -45),
                 textcoords='offset points',
                 arrowprops=dict(arrowstyle="->", color='red'),
                 fontsize=10,
                 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="red", lw=1))

# Add value labels for latest actual data
last_actual_year = 2023
plt.text(last_actual_year, china_gdp[-1], 
         f"China\n${china_gdp[-1]:,.0f}", 
         ha='right', va='bottom', fontsize=9)
plt.text(last_actual_year, eu_gdp[-1], 
         f"EU\n${eu_gdp[-1]:,.0f}", 
         ha='right', va='bottom', fontsize=9)

plt.legend(loc='upper left', frameon=True)
plt.xticks(np.arange(1990, 2071, 5), rotation=45)
plt.ylim(0, 300000)
plt.tight_layout()
plt.show()
