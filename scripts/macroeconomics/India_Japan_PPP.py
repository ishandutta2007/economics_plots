import matplotlib.pyplot as plt
import numpy as np

# Complete 21-year macroeconomic dataset for India and Japan (Historical + Projected)
# Data source: IMF World Economic Outlook Database
years = np.array(list(range(2016, 2037)))

india_ppp = np.array(
    [
        5629,
        6048,
        6592,
        7001,
        6802,
        7840,
        8965,
        9880,
        10747,
        11789,
        12801,
        13819,
        14837,
        15957,
        17175,
        18485,
        19871,
        21361,
        22963,
        24685,
        26536,
    ]
)

japan_ppp = np.array(
    [
        40941,
        42422,
        43198,
        43886,
        43703,
        46312,
        50439,
        52928,
        54369,
        56854,
        59207,
        61213,
        62957,
        64844,
        66841,
        68887,
        70953,
        73081,
        75273,
        77531,
        79856,
    ]
)

# Calculate conversion multiples dynamically for the indicators (Japan divided by India)
multiples = [f"{j / i:.2f}x" for i, j in zip(india_ppp, japan_ppp)]

fig, ax = plt.subplots(figsize=(16, 10))

# 1. Plot Historical Lines (2016 to 2026 - Indices 0 to 10)
ax.plot(
    years[:11],
    india_ppp[:11],
    color="#FF9933",
    linestyle="-",
    marker="o",
    linewidth=2.5,
    label="India PPP (Historical)",
)
ax.plot(
    years[:11],
    japan_ppp[:11],
    color="#BC002D",
    linestyle="-",
    marker="o",
    linewidth=2.5,
    label="Japan PPP (Historical)",
)

# 2. Plot Projection Lines (2026 to 2036 - Indices 10 to 20)
ax.plot(
    years[10:],
    india_ppp[10:],
    color="#FF9933",
    linestyle=":",
    marker="o",
    linewidth=2.5,
    label="India PPP (Projected)",
)
ax.plot(
    years[10:],
    japan_ppp[10:],
    color="#BC002D",
    linestyle=":",
    marker="o",
    linewidth=2.5,
    label="Japan PPP (Projected)",
)

# 3. Add Annotations for every coordinate point
for i in range(len(years)):
    # India Labels (offset below the line)
    ax.annotate(
        f"${india_ppp[i]:,}",
        (years[i], india_ppp[i]),
        textcoords="offset points",
        xytext=(0, -15),
        ha="center",
        fontsize=8,
        color="#B35300",
        weight="bold",
    )
    # Japan Labels (offset above the line)
    ax.annotate(
        f"${japan_ppp[i]:,}",
        (years[i], japan_ppp[i]),
        textcoords="offset points",
        xytext=(0, 10),
        ha="center",
        fontsize=8,
        color="#80001C",
        weight="bold",
    )

# 4. Vertical Double-Headed Separator Arrows indicating the Multiple gaps
# Marking milestones at the start (2016), current baseline (2026), and end target (2036)
gap_years = [0, 10, 20]
for idx in gap_years:
    ax.annotate(
        "",
        xy=(years[idx], india_ppp[idx]),
        xytext=(years[idx], japan_ppp[idx]),
        arrowprops=dict(arrowstyle="<->", color="#4B0082", lw=2.5, ls="--"),
    )

    # Calculate middle point of the vertical line to anchor the text label cleanly
    mid_y = (india_ppp[idx] + japan_ppp[idx]) / 2
    ax.text(
        years[idx] + 0.2,
        mid_y,
        f"Gap:\n{multiples[idx]}",
        color="#4B0082",
        weight="bold",
        fontsize=11,
        bbox=dict(facecolor="white", alpha=0.8, edgecolor="none"),
    )

# Formatting chart features
ax.set_title(
    "Macroeconomic Catch-Up: India vs. Japan GDP per Capita (PPP) Progression",
    fontsize=15,
    weight="bold",
    pad=20,
)
ax.set_xlabel("Year", fontsize=12, labelpad=10)
ax.set_ylabel(
    "GDP per Capita (Current International Dollars)", fontsize=12, labelpad=10
)
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)
ax.get_yaxis().set_major_formatter(
    plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x)))
)
ax.grid(True, linestyle="--", alpha=0.4)
ax.legend(loc="upper left", fontsize=11, framealpha=0.9)

# Vertical marker separating actual history from future modeling forecasts
ax.axvline(x=2026, color="gray", linestyle="--", alpha=0.7, linewidth=1.5)
ax.text(2026.1, 35000, "2026 Baseline", color="gray", rotation=90, weight="bold")

plt.tight_layout()
plt.show()
