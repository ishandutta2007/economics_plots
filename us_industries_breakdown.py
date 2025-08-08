import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Historical data (approximations based on search results and economic trends)
years = np.array([1925, 1950, 1975, 2000, 2025])
agriculture = np.array([12.0, 7.0, 3.0, 1.2, 0.8])  # :cite[1]:cite[2]:cite[7]
industry = np.array([35.0, 40.0, 32.0, 22.0, 18.9])  # :cite[1]:cite[3]
services = np.array([53.0, 53.0, 65.0, 76.8, 80.2])  # :cite[1]:cite[3]:cite[8]
mining = np.array([6.0, 4.5, 3.5, 1.8, 1.5])  # :cite[4]

# Create smooth curves
years_smooth = np.linspace(years.min(), years.max(), 300)
ag_spline = make_interp_spline(years, agriculture)(years_smooth)
ind_spline = make_interp_spline(years, industry)(years_smooth)
serv_spline = make_interp_spline(years, services)(years_smooth)
mining_spline = make_interp_spline(years, mining)(years_smooth)

# Plot configuration
plt.figure(figsize=(14, 8))
plt.plot(years_smooth, serv_spline, '#4E79A7', linewidth=3, label='Services')
plt.plot(years_smooth, ind_spline, '#F28E2B', linewidth=3, label='Industry')
plt.plot(years_smooth, ag_spline, '#59A14F', linewidth=3, label='Agriculture')
plt.plot(years_smooth, mining_spline, '#E15759', linewidth=3, label='Mining')

# Highlight key data points
plt.scatter(years, services, color='#4E79A7', s=80, zorder=5)
plt.scatter(years, industry, color='#F28E2B', s=80, zorder=5)
plt.scatter(years, agriculture, color='#59A14F', s=80, zorder=5)
plt.scatter(years, mining, color='#E15759', s=80, zorder=5)

# Annotate recent values
plt.annotate(f'Services: {services[-1]}% (2023)', xy=(2025, 82), 
             xytext=(2020, 85), arrowprops=dict(arrowstyle='->'))
plt.annotate(f'Industry: {industry[-1]}% (2023)', xy=(2025, 18.9), 
             xytext=(1990, 30), arrowprops=dict(arrowstyle='->'))
plt.annotate(f'Agriculture: {agriculture[-1]}% (2023)', xy=(2025, 0.8), 
             xytext=(1980, 5), arrowprops=dict(arrowstyle='->'))
plt.annotate(f'Mining: {mining[-1]}% (2023)', xy=(2025, 1.5), 
             xytext=(1960, 3), arrowprops=dict(arrowstyle='->'))

# Add economic milestones
plt.axvline(1929, color='gray', linestyle='--', alpha=0.5)
plt.text(1929, 90, 'Great Depression', rotation=90, ha='right', va='top')

plt.axvline(1945, color='gray', linestyle='--', alpha=0.5)
plt.text(1945, 90, 'Post-WWII Boom', rotation=90, ha='right', va='top')

plt.axvline(2008, color='gray', linestyle='--', alpha=0.5)
plt.text(2008, 90, 'Financial Crisis', rotation=90, ha='right', va='top')

# Formatting
plt.title('U.S. Economic Sector Shares as Percentage of GDP (1925-2025)', fontsize=16, pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Percentage of GDP', fontsize=12)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.grid(True, linestyle='--', alpha=0.3)
plt.ylim(0, 100)
plt.xlim(1920, 2030)

plt.figtext(0.5, 0.01, "Data sources: [1] U.S. Bureau of Economic Analysis [2] USDA [3] Statista [4] FRED Mining Data", 
            ha="center", fontsize=9, style='italic')

plt.tight_layout()
plt.show()