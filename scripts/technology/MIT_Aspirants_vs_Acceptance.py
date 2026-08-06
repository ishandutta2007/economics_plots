import matplotlib.pyplot as plt
import numpy as np

# 1. Historical MIT Dataset (Years 2000 to 2026)
years = [
    2000, 2015, 2016, 2017, 2018, 2019, 2020,
    2021, 2022, 2023, 2024, 2025, 2026
]

# Total admitted students (approximate incoming class size + yield buffer)
seats = [
    1729, 1519, 1511, 1452, 1464, 1427, 1457,
    1340, 1337, 1259, 1275, 1334, 1299
]

# Total distinct candidates who took the applied
aspirants = [
    10672, 18306, 19020, 20247, 21706, 21312, 20075,
    33240, 33796, 26914, 28232, 29281, 28349
]

# Calculate the precise acceptance rate as a percentage
acceptance_rate = [(s / a) * 100 for s, a in zip(seats, aspirants)]

# 2. Setup the Plotting Canvas
fig, ax1 = plt.subplots(figsize=(12, 7))
ax2 = ax1.twinx()  # Shared X-axis for acceptance rate

# 3. Plot Total Seats and Total Aspirants (Left Y-Axis)
# Logarithmic scale accommodates growth gracefully
ax1.set_yscale('log')
line1 = ax1.plot(years, aspirants, color='#A31F34', marker='o', linewidth=2.5, label='Total Applicants (Log Scale)') # MIT Red
line2 = ax1.plot(years, seats, color='#8A8B8C', marker='s', linewidth=2.5, label='Total Admitted (Log Scale)') # MIT Silver Gray

# 4. Plot Acceptance Rate (Right Y-Axis)
line3 = ax2.plot(years, acceptance_rate, color='#2c3e50', linestyle='--', marker='^', linewidth=2, label='Acceptance Rate (%)') # Dark Gray

# Annotate Applicants
for i, txt in enumerate(aspirants):
    # Only annotate some points to avoid clutter, e.g., first, last, and peaks/dips
    # if i == 0 or i == 7 or i == len(aspirants)-1:
    ax1.annotate(f'{txt:,}', (years[i], aspirants[i]), textcoords="offset points", xytext=(0,12), ha='center', fontsize=8, color='#A31F34', fontweight='bold', bbox=dict(boxstyle="round,pad=0.2", fc="white", ec='#A31F34', alpha=0.85))

# Annotate Admitted
for i, txt in enumerate(seats):
    # if i == 0 or i == len(seats)-1:
    ax1.annotate(f'{txt:,}', (years[i], seats[i]), textcoords="offset points", xytext=(0,-18), ha='center', fontsize=8, color='#8A8B8C', fontweight='bold', bbox=dict(boxstyle="round,pad=0.2", fc="white", ec='#8A8B8C', alpha=0.85))

# Annotate Acceptance Rate
for i, txt in enumerate(acceptance_rate):
    ax2.annotate(f'{txt:.1f}%', (years[i], acceptance_rate[i]), textcoords="offset points", xytext=(0,12), ha='center', fontsize=8, color='#2c3e50', fontweight='bold', bbox=dict(boxstyle="round,pad=0.2", fc="white", ec='#2c3e50', alpha=0.85))

# 5. Labels and Grid Formatting
ax1.set_xlabel('Year', fontsize=12, fontweight='bold', labelpad=10)
ax1.set_ylabel('Number of People (Admitted / Applicants)', color='#2c3e50', fontsize=12, fontweight='bold')
ax2.set_ylabel('Acceptance Rate (%)', color='#2c3e50', fontsize=12, fontweight='bold')

# Ensure tick values are completely legible
ax1.get_xaxis().set_major_formatter(plt.FuncFormatter(lambda x, p: format(int(x), ',')))
ax1.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, p: format(int(x), ',')))

# Highlight specific timeline eras using background shading
ax1.axvspan(2000, 2019, color='gray', alpha=0.08, label='Pre-Pandemic Era')
ax1.axvspan(2020, 2026, color='#A31F34', alpha=0.05, label='Test-Optional & Pandemic Era (2020-2022)')

# 6. Title and Legend Layout
plt.title('25-Year Evolution of MIT Admissions: Admitted, Applicants & Selectivity (2000–2026)', fontsize=14, fontweight='bold', pad=15)
lines = line1 + line2 + line3
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left', frameon=True, shadow=True)

# Turn on background grid
ax1.grid(True, which="both", ls="--", alpha=0.5)

# Save the plot
plt.tight_layout()
plt.savefig("assets/mit_acceptance_rate.png", dpi=400)

plt.show()
