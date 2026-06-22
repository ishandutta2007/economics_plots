import matplotlib.pyplot as plt

# Dataset: R&D spending as a % of GDP (1996 - 2026)
years = [1996, 2000, 2010, 2020, 2022, 2026]

# Data points based on historical World Bank, 

china_rd = [0.56, 0.89, 1.76, 2.40, 2.55, 2.75]
usa_rd = [2.40, 2.72, 2.74, 3.12, 3.45, 3.45]
south_korea_rd = [2.26, 2.18, 3.47, 4.80, 5.21, 5.15]
israel_rd = [2.66, 3.92, 3.93, 5.53, 6.02, 6.30]
india_rd = [0.60, 0.74, 0.79, 0.64, 0.65, 0.64]

# Create the figure layout
plt.figure(figsize=(12, 7))

# Plot lines with custom markers and styles
plt.plot(years, israel_rd, marker='^', color='#0038A8', linewidth=2.5, linestyle='-', label='Israel')
plt.plot(years, south_korea_rd, marker='d', color='#000000', linewidth=2.5, linestyle='-', label='South Korea')
plt.plot(years, usa_rd, marker='s', color='#1F77B4', linewidth=2.5, linestyle='--', label='USA')
plt.plot(years, china_rd, marker='o', color='#D62728', linewidth=2.5, linestyle='--', label='China')
plt.plot(years, india_rd, marker='v', color='#FF9933', linewidth=2.5, linestyle=':', label='India')

# Visual styling
plt.title('Global R&D Expenditure Comparison as a % of GDP (1996-2026)', fontsize=14, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('R&D Spending (% of GDP)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(fontsize=11, loc='upper left')

# Formulate dictionary for easy label loop allocation
latest_data = {
    'Israel': (israel_rd[-1], '#0038A8'),
    'S. Korea': (south_korea_rd[-1], '#000000'),
    'USA': (usa_rd[-1], '#1F77B4'),
    'China': (china_rd[-1], '#D62728'),
    'India': (india_rd[-1], '#FF9933')
}

# Attach current 2026 tracking numbers to graph pointers
for country, (val, color) in latest_data.items():
    plt.annotate(f'{val}% {country}', 
                 xy=(years[-1], val), 
                 xytext=(8, -3), 
                 textcoords='offset points', 
                 color=color, 
                 fontweight='bold',
                 fontsize=10)

# Render and align margins
plt.xlim(1995, 2031) # Extend x-axis slightly rightward to make space for labels
plt.tight_layout()
plt.show()
