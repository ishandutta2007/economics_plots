import matplotlib.pyplot as plt
import numpy as np

# 1. Historical IIT Dataset (Years 1956 to 2026)
# Data points represent historical milestones and structural changes
years = [
    1956, 1963, 1970, 1980, 1985, 1990, 1995, 2000, 
    2005, 2010, 2013, 2016, 2019, 2022, 2024, 2026
]

# Total seats available across all operational IITs in that year
seats = [
    120, 500, 1000, 1300, 1400, 1800, 2000, 2200, 
    3900, 9500, 9660, 10572, 13604, 16598, 17740, 18951
]

# Total distinct candidates who took the entrance exam
aspirants = [
    3000, 15000, 20000, 28000, 54000, 80000, 90000, 115000, 
    198000, 455571, 1260000, 1200000, 1147125, 905590, 1410000, 1450000
]

# Calculate the precise acceptance rate as a percentage
acceptance_rate = [(s / a) * 100 for s, a in zip(seats, aspirants)]

# 2. Setup the Plotting Canvas
fig, ax1 = plt.subplots(figsize=(12, 7))
ax2 = ax1.twinx()  # Shared X-axis for acceptance rate

# 3. Plot Total Seats and Total Aspirants (Left Y-Axis)
# Logarithmic scale accommodates growth from 100s to millions gracefully
ax1.set_yscale('log')
line1 = ax1.plot(years, aspirants, color='#e74c3c', marker='o', linewidth=2.5, label='Total Aspirants (Log Scale)')
line2 = ax1.plot(years, seats, color='#3498db', marker='s', linewidth=2.5, label='Total IIT Seats (Log Scale)')

# 4. Plot Acceptance Rate (Right Y-Axis)
line3 = ax2.plot(years, acceptance_rate, color='#2ecc71', linestyle='--', marker='^', linewidth=2, label='Acceptance Rate (%)')

# Annotate Aspirants
for i, txt in enumerate(aspirants):
    ax1.annotate(f'{txt:,}', (years[i], aspirants[i]), textcoords="offset points", xytext=(0,12), ha='center', fontsize=8, color='#c0392b', fontweight='bold', bbox=dict(boxstyle="round,pad=0.2", fc="white", ec='#e74c3c', alpha=0.85))

# Annotate Seats
for i, txt in enumerate(seats):
    ax1.annotate(f'{txt:,}', (years[i], seats[i]), textcoords="offset points", xytext=(0,-18), ha='center', fontsize=8, color='#2980b9', fontweight='bold', bbox=dict(boxstyle="round,pad=0.2", fc="white", ec='#3498db', alpha=0.85))

# Annotate Acceptance Rate
for i, txt in enumerate(acceptance_rate):
    ax2.annotate(f'{txt:.2f}%', (years[i], acceptance_rate[i]), textcoords="offset points", xytext=(0,12), ha='center', fontsize=8, color='#27ae60', fontweight='bold', bbox=dict(boxstyle="round,pad=0.2", fc="white", ec='#2ecc71', alpha=0.85))

# 5. Labels and Grid Formatting
ax1.set_xlabel('Year', fontsize=12, fontweight='bold', labelpad=10)
ax1.set_ylabel('Number of People (Seats / Aspirants)', color='#2c3e50', fontsize=12, fontweight='bold')
ax2.set_ylabel('Acceptance Rate (%)', color='#27ae60', fontsize=12, fontweight='bold')

# Ensure tick values are completely legible
ax1.get_xaxis().set_major_formatter(plt.FuncFormatter(lambda x, p: format(int(x), ',')))
ax1.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, p: format(int(x), ',')))

# Highlight specific timeline eras using background shading
ax1.axvspan(1956, 1962, color='gray', alpha=0.08, label='Early Era')
ax1.axvspan(2000, 2005, color='orange', alpha=0.05, label='Screening Test Era')
ax1.axvspan(2013, 2026, color='blue', alpha=0.04, label='Two-Tier JEE Era')

# 6. Title and Legend Layout
plt.title('70-Year Evolution of IIT Admissions: Seats, Aspirants & Selectivity (1956–2026)', fontsize=14, fontweight='bold', pad=15)
lines = line1 + line2 + line3
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left', frameon=True, shadow=True)

# Turn on background grid
ax1.grid(True, which="both", ls="--", alpha=0.5)

# Save the plot
plt.tight_layout()
plt.savefig("assets/jee_acceptance_rate.png", dpi=400)

plt.show()
