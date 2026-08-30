import matplotlib.pyplot as plt

# Complete 30-Year Dataset (FY 1997 - FY 2026)
data = [
    {"year": 1997, "tcs_usd_billion": 0.20, "employees": 7850, "india_gdp_pc": 415},
    {"year": 1998, "tcs_usd_billion": 0.29, "employees": 9500, "india_gdp_pc": 413},
    {"year": 1999, "tcs_usd_billion": 0.39, "employees": 12400, "india_gdp_pc": 442},
    {"year": 2000, "tcs_usd_billion": 0.47, "employees": 14510, "india_gdp_pc": 443},
    {"year": 2001, "tcs_usd_billion": 0.68, "employees": 18100, "india_gdp_pc": 452},
    {"year": 2002, "tcs_usd_billion": 0.87, "employees": 21350, "india_gdp_pc": 471},
    {"year": 2003, "tcs_usd_billion": 1.04, "employees": 25202, "india_gdp_pc": 546},
    {"year": 2004, "tcs_usd_billion": 1.56, "employees": 33524, "india_gdp_pc": 628},
    {"year": 2005, "tcs_usd_billion": 2.24, "employees": 45434, "india_gdp_pc": 714},
    {"year": 2006, "tcs_usd_billion": 2.97, "employees": 71000, "india_gdp_pc": 807},
    {"year": 2007, "tcs_usd_billion": 4.30, "employees": 89419, "india_gdp_pc": 1028},
    {"year": 2008, "tcs_usd_billion": 5.70, "employees": 111407, "india_gdp_pc": 999},
    {"year": 2009, "tcs_usd_billion": 6.00, "employees": 143761, "india_gdp_pc": 1101},
    {"year": 2010, "tcs_usd_billion": 6.34, "employees": 160429, "india_gdp_pc": 1358},
    {"year": 2011, "tcs_usd_billion": 8.35, "employees": 202039, "india_gdp_pc": 1458},
    {"year": 2012, "tcs_usd_billion": 10.17, "employees": 238583, "india_gdp_pc": 1444},
    {"year": 2013, "tcs_usd_billion": 11.60, "employees": 276196, "india_gdp_pc": 1449},
    {"year": 2014, "tcs_usd_billion": 13.40, "employees": 300464, "india_gdp_pc": 1574},
    {"year": 2015, "tcs_usd_billion": 15.45, "employees": 319656, "india_gdp_pc": 1606},
    {"year": 2016, "tcs_usd_billion": 16.54, "employees": 353843, "india_gdp_pc": 1733},
    {"year": 2017, "tcs_usd_billion": 17.58, "employees": 387223, "india_gdp_pc": 1981},
    {"year": 2018, "tcs_usd_billion": 19.08, "employees": 394998, "india_gdp_pc": 1997},
    {"year": 2019, "tcs_usd_billion": 20.90, "employees": 424285, "india_gdp_pc": 2101},
    {"year": 2020, "tcs_usd_billion": 22.00, "employees": 448464, "india_gdp_pc": 1928},
    {"year": 2021, "tcs_usd_billion": 22.20, "employees": 488649, "india_gdp_pc": 2238},
    {"year": 2022, "tcs_usd_billion": 25.70, "employees": 592195, "india_gdp_pc": 2390},
    {"year": 2023, "tcs_usd_billion": 28.89, "employees": 614795, "india_gdp_pc": 2411},
    {"year": 2024, "tcs_usd_billion": 29.10, "employees": 601546, "india_gdp_pc": 2501},
    {"year": 2025, "tcs_usd_billion": 30.18, "employees": 607979, "india_gdp_pc": 2690},
    {"year": 2026, "tcs_usd_billion": 30.05, "employees": 584519, "india_gdp_pc": 2813}
]

# Extract arrays and process mathematical metrics
years = [d["year"] for d in data]
india_gdp_pc = [d["india_gdp_pc"] for d in data]
tcs_rev_per_emp = [(d["tcs_usd_billion"] * 1_000_000_000) / d["employees"] for d in data]

# Core Canvas Optimization
fig, ax = plt.subplots(figsize=(16, 10))

# Configure single Y-axis to use base-10 Logarithmic scaling
ax.set_yscale('log')

# Plot Lines on the same axis
color_tcs = '#1f77b4'
color_india = '#e65c00'

ax.plot(years, tcs_rev_per_emp, marker='o', color=color_tcs, linewidth=2.5, label='TCS Revenue/Employee')
ax.plot(years, india_gdp_pc, marker='s', linestyle='--', color=color_india, linewidth=2, label="India GDP per Capita")

# X and Y Axis formatting
ax.set_xlabel("Fiscal Year (FY)", fontsize=12, labelpad=10)
ax.set_ylabel("Value in USD (Log Scale)", fontsize=12)
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# Explicitly format Y-axis ticks to read clearly rather than scientific notation
from matplotlib.ticker import ScalarFormatter
ax.get_yaxis().set_major_formatter(ScalarFormatter())
ax.set_yticks([400, 1000, 2500, 5000, 10000, 25000, 55000])

# Layout Structuring
ax.grid(True, which="both", linestyle='--', alpha=0.3)
plt.title("TCS Corporate Efficiency vs. India National GDP per Capita (Log Scale: 1997 - 2026)", fontsize=15, fontweight='bold', pad=20)

# Annotate TCS Metric Curve
for i, (year, val) in enumerate(zip(years, tcs_rev_per_emp)):
    # Precise positioning optimization using log-friendly relative scaling
    offset_y = 1.08 if i % 2 == 0 else 0.88
    ax.text(year, val * offset_y, f"${val:,.0f}", ha='center', va='center',
            fontsize=8, fontweight='bold', color='#0f3d5f',
            bbox=dict(boxstyle="round,pad=0.15", fc="#e6f2ff", alpha=0.8, ec="none"))

# Annotate National GDP Metric Curve
for i, (year, val) in enumerate(zip(years, india_gdp_pc)):
    offset_y = 0.88 if i % 2 == 0 else 1.08
    ax.text(year, val * offset_y, f"${val:,.0f}", ha='center', va='center',
            fontsize=8, fontweight='bold', color='#803300',
            bbox=dict(boxstyle="round,pad=0.15", fc="#fff2e6", alpha=0.8, ec="none"))

# Calculate and draw gaps for Starting (1997) and Ending (2026) points
# 1997 Gap Data
y1_tcs, y1_ind = tcs_rev_per_emp[0], india_gdp_pc[0]
ratio_1997 = y1_tcs / y1_ind
# 2026 Gap Data
y2_tcs, y2_ind = tcs_rev_per_emp[-1], india_gdp_pc[-1]
ratio_2026 = y2_tcs / y2_ind

# Draw Double-Headed Dotted Arrows signifying the gaps
# '<->' builds the double header; color is set neutral dark gray to stand out cleanly
ax.annotate('', xy=(1997, y1_ind), xytext=(1997, y1_tcs),
            arrowprops=dict(arrowstyle="<->", linestyle=":", color="#333333", linewidth=2))
ax.text(1997 + 0.3, (y1_ind * y1_tcs) ** 0.5, f"Gap:\n{ratio_1997:.1f}x", 
        va='center', ha='left', color='#333333', fontweight='bold', fontsize=10,
        bbox=dict(boxstyle="square,pad=0.2", fc="white", alpha=0.8, ec="gray", lw=0.5))

ax.annotate('', xy=(2026, y2_ind), xytext=(2026, y2_tcs),
            arrowprops=dict(arrowstyle="<->", linestyle=":", color="#333333", linewidth=2))
ax.text(2026 - 0.3, (y2_ind * y2_tcs) ** 0.5, f"Gap:\n{ratio_2026:.1f}x", 
        va='center', ha='right', color='#333333', fontweight='bold', fontsize=10,
        bbox=dict(boxstyle="square,pad=0.2", fc="white", alpha=0.8, ec="gray", lw=0.5))

# Add Legend
ax.legend(loc='upper left', fontsize=11, framealpha=0.9)

plt.tight_layout()
plt.show()
