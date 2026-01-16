import matplotlib.pyplot as plt
import numpy as np

# Years for the X-axis
years_hist = np.arange(2015, 2026)
years_proj = np.arange(2025, 2036)

# Data (Estimated values in GW based on current trends)
china_hist = [520, 580, 650, 728, 790, 934, 1063, 1200, 1450, 1750, 2050]
china_proj = [2050, 2250, 2450, 2650, 2850, 3050, 3250, 3450, 3650, 3850, 4050]

us_hist = [210, 230, 250, 275, 300, 335, 370, 410, 445, 485, 525]
us_proj = [525, 570, 620, 675, 735, 800, 870, 945, 1025, 1110, 1200]

india_hist = [80, 95, 110, 125, 140, 160, 180, 210, 245, 285, 330]
india_proj = [330, 380, 435, 495, 560, 630, 705, 785, 870, 960, 1050]

# Combined data for annotation indexing
china_full = china_hist + china_proj[1:]
us_full = us_hist + us_proj[1:]
india_full = india_hist + india_proj[1:]

# Color Palette
color_china = '#de2910' # Red
color_us = '#3c3b6e'    # Dark Blue
color_india = '#ff9933' # Saffron/Orange

plt.figure(figsize=(14, 8))

# Plotting Curves (Solid for History, Dotted for Projection)
plt.plot(years_hist, china_hist, color=color_china, linewidth=2.5, label='China (Hist)')
plt.plot(years_proj, china_proj, color=color_china, linewidth=2.5, linestyle=':', label='China (Proj)')

plt.plot(years_hist, us_hist, color=color_us, linewidth=2.5, label='U.S. (Hist)')
plt.plot(years_proj, us_proj, color=color_us, linewidth=2.5, linestyle=':', label='U.S. (Proj)')

plt.plot(years_hist, india_hist, color=color_india, linewidth=2.5, label='India (Hist)')
plt.plot(years_proj, india_proj, color=color_india, linewidth=2.5, linestyle=':', label='India (Proj)')

# Annotation years
target_years = [2020, 2025, 2030, 2035]

def add_value_labels(data, color, offset_y):
    for yr in target_years:
        idx = yr - 2015
        val = data[idx]
        plt.text(yr, val + offset_y, f'{val} GW', color=color, 
                 ha='center', va='bottom', fontsize=9, fontweight='bold',
                 bbox=dict(facecolor='white', alpha=0.6, edgecolor='none', pad=1))
        plt.plot(yr, val, 'o', color=color, markersize=4)

# Apply annotations with slightly different offsets to avoid overlap
add_value_labels(china_full, color_china, 100)
add_value_labels(us_full, color_us, 60)
add_value_labels(india_full, color_india, -150) # Offset below the line

# Formatting
plt.title('Growth & 10-Year Projection of Renewable Energy Capacity', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Installed Capacity ($GW$)', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.5)
plt.legend(loc='upper left', ncol=3, frameon=True)

plt.xticks(np.arange(2015, 2036, 5))
plt.xlim(2014, 2036)
plt.ylim(0, 4500)

plt.tight_layout()
plt.savefig('renewable_capacity_comparison.png')
plt.show()