import matplotlib.pyplot as plt
import numpy as np

# Complete 21-year macroeconomic dataset (Historical + Projected)
years = np.array(list(range(2016, 2037)))
india_ppp = np.array([5835, 6182, 6615, 6971, 6524, 7311, 8295, 9170, 10074, 11467, 
                      12800, 13908, 14927, 16010, 17160, 18380, 19670, 21040, 22490, 24030, 25660])
eu_ppp = np.array([43620, 45840, 47760, 49350, 46810, 50840, 54560, 56930, 59210, 61050, 
                   62466, 64450, 66480, 68540, 70630, 72750, 74900, 77080, 79300, 81550, 83840])
multiples = ["7.48x", "7.42x", "7.22x", "7.08x", "7.18x", "6.95x", "6.58x", "6.21x", "5.88x", "5.32x", 
             "4.88x", "4.63x", "4.45x", "4.28x", "4.12x", "3.96x", "3.81x", "3.66x", "3.53x", "3.39x", "3.27x"]

fig, ax = plt.subplots(figsize=(16, 10))

# 1. Plot Historical Lines (2016 to 2026 - Indices 0 to 10)
ax.plot(years[:11], india_ppp[:11], color='#FF9933', linestyle='-', marker='o', linewidth=2.5, label='India PPP (Historical)')
ax.plot(years[:11], eu_ppp[:11], color='#003399', linestyle='-', marker='o', linewidth=2.5, label='EU PPP (Historical)')

# 2. Plot Projection Lines (2026 to 2036 - Indices 10 to 20)
ax.plot(years[10:], india_ppp[10:], color='#FF9933', linestyle=':', marker='o', linewidth=2.5, label='India PPP (Projected)')
ax.plot(years[10:], eu_ppp[10:], color='#003399', linestyle=':', marker='o', linewidth=2.5, label='EU PPP (Projected)')

# 3. Add Annotations for every single coordinate point
for i in range(len(years)):
    # India Labels (placed slightly below the point to prevent chart overlapping)
    ax.annotate(f"${india_ppp[i]:,}", (years[i], india_ppp[i]), textcoords="offset points", 
                xytext=(0, -15), ha='center', fontsize=8, color='#B35300', weight='bold')
    # EU Labels (placed slightly above the point)
    ax.annotate(f"${eu_ppp[i]:,}", (years[i], eu_ppp[i]), textcoords="offset points", 
                xytext=(0, 10), ha='center', fontsize=8, color='#001A4D', weight='bold')

# 4. Vertical Double-Headed Separator Arrows indicating the Multiple gaps
# Showcasing key milestone transitions: start (2016), current baseline (2026), and terminal year (2036)
gap_years = [0, 10, 20] 
for idx in gap_years:
    # Drawing the vertical double-headed arrow
    ax.annotate('', xy=(years[idx], india_ppp[idx]), xytext=(years[idx], eu_ppp[idx]),
                arrowprops=dict(arrowstyle='<->', color='#800080', lw=2.5, ls='--'))
    
    # Calculate middle point of the vertical line to anchor the text label cleanly
    mid_y = (india_ppp[idx] + eu_ppp[idx]) / 2
    ax.text(years[idx] + 0.2, mid_y, f"Gap:\n{multiples[idx]}", color='#800080', 
            weight='bold', fontsize=11, bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))

# Formatting layout details
ax.set_title('Macroeconomic Convergence: India vs. European Union GDP per Capita (PPP)', fontsize=15, weight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12, labelpad=10)
ax.set_ylabel('GDP per Capita (Current International Dollars)', fontsize=12, labelpad=10)
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)
ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
ax.grid(True, linestyle='--', alpha=0.4)
ax.legend(loc='upper left', fontsize=11, framealpha=0.9)

# Vertical marker separating actual history from future modeling forecasts
ax.axvline(x=2026, color='gray', linestyle='--', alpha=0.7, linewidth=1.5)
ax.text(2026.1, 30000, '2026 Baseline', color='gray', rotation=90, weight='bold')

plt.tight_layout()
plt.show()
