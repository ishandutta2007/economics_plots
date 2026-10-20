import matplotlib.pyplot as plt
import numpy as np

# Yearly data from CAMET / Ministry of Transport reports
years = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
total_urt_km = [
    3618.0, 4152.8, 5033.0, 5761.4, 6736.2, 
    7978.2, 9206.8, 10292.0, 11224.5, 12160.8, 12925.5
]
metro_only_km = [
    2658.0, 3169.0, 3884.0, 4354.0, 5180.0, 
    6302.8, 7209.7, 8012.9, 8543.1, 9273.3, 10004.8
]

# Calculate annual additions
annual_growth = [0] + [total_urt_km[i] - total_urt_km[i-1] for i in range(1, len(total_urt_km))]

# Set plot aesthetics
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 10), sharex=True, gridspec_kw={'height_ratios': [2, 1]})

# --- Subplot 1: Cumulative Network Length ---
ax1.plot(years, total_urt_km, marker='o', linewidth=2.5, color='#1f77b4', label='Total Urban Rail Transit (CAMET)')
ax1.plot(years, metro_only_km, marker='s', linewidth=2.5, linestyle='--', color='#d62728', label='Metro / Subway Only')

# Data point callouts for milestone years
for yr, tot, met in zip(years, total_urt_km, metro_only_km):
    if yr in [2015, 2020, 2022, 2025]:
        ax1.annotate(f"{tot:,.0f} km", (yr, tot), textcoords="offset points", xytext=(0, 8), ha='center', fontweight='bold', color='#1f77b4')
        ax1.annotate(f"{met:,.0f} km", (yr, met), textcoords="offset points", xytext=(0, -14), ha='center', fontweight='bold', color='#d62728')

ax1.set_title("Growth of China's Urban Rail & Metro Network (2015–2025)", fontsize=14, pad=15, fontweight='bold')
ax1.set_ylabel("Operational Length (km)", fontsize=12)
ax1.legend(loc='upper left', frameon=True)
ax1.grid(True, linestyle=':', alpha=0.6)

# --- Subplot 2: Annual Additions ---
bars = ax2.bar(years[1:], annual_growth[1:], color='#2ca02c', alpha=0.8, width=0.6, label='Annual Net Growth (km)')
for bar in bars:
    height = bar.get_height()
    ax2.annotate(f"+{height:.0f}", xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=9)

ax2.set_xlabel("Year", fontsize=12)
ax2.set_ylabel("New Lines Added (km)", fontsize=11)
ax2.set_xticks(years)
ax2.grid(True, linestyle=':', alpha=0.6)
ax2.legend(loc='upper right', frameon=True)

plt.tight_layout()
plt.show()
