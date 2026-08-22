import matplotlib.pyplot as plt

# Data split into historical/current (solid line) and projected/target (dotted line)
years_hist = [2010, 2012, 2014, 2016, 2018, 2020, 2022, 2024, 2025, 2026]
share_hist = [26.6, 27.2, 32.0, 31.3, 33.5, 36.3, 40.9, 43.4, 50.0, 54.4]

years_proj = [2026, 2030]
share_proj = [54.4, 62.5]

# Initialize plot
plt.figure(figsize=(12, 7))

# Plot historical and current trend line (Solid)
plt.plot(years_hist, share_hist, color='#1f77b4', linestyle='-', linewidth=2.5, marker='o', label='Historical / Actual')

# Plot projected trend line (Dotted)
plt.plot(years_proj, share_proj, color='#ff7f0e', linestyle='--', linewidth=2.5, marker='s', label='Projected Target')

# Graph aesthetics
plt.title("India's Non-Fossil Fuel Power Capacity Share (2010 - 2030)", fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Non-Fossil Capacity Share (%)', fontsize=12)
plt.xlim(2008, 2032)
plt.ylim(20, 70)
plt.xticks(list(range(2010, 2032, 2)))
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper left', fontsize=11)

# Annotate every single historical point
for year, share in zip(years_hist, share_hist):
    plt.annotate(f"{share}%", 
                 (year, share), 
                 textcoords="offset points", 
                 xytext=(0, 10), 
                 ha='center', 
                 fontsize=9, 
                 fontweight='bold',
                 color='#1f77b4')

# Annotate the final target projection point (avoiding repeating 2026)
plt.annotate(f"{share_proj[1]}%", 
             (years_proj[1], share_proj[1]), 
             textcoords="offset points", 
             xytext=(0, 10), 
             ha='center', 
             fontsize=9, 
             fontweight='bold',
             color='#ff7f0e')

# Layout adjustments and display
plt.tight_layout()
plt.show()
