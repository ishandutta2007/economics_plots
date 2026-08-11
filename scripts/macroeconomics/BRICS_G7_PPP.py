import matplotlib.pyplot as plt
import numpy as np

# Complete 21-year macroeconomic dataset for G7 and BRICS average (Historical + Projected)
# Values represent collective average GDP per capita at Purchasing Power Parity (PPP)
years = np.array(list(range(2016, 2037)))

brics_ppp = np.array(
    [
        11800,
        12550,
        13320,
        14050,
        13720,
        14900,
        16180,
        17450,
        18720,
        19950,
        21250,
        22600,
        24010,
        25500,
        27080,
        28750,
        30510,
        32370,
        34330,
        36400,
        38580,
    ]
)

g7_ppp = np.array(
    [
        53400,
        55800,
        57900,
        59700,
        57400,
        61800,
        65400,
        68900,
        72100,
        75200,
        78300,
        81400,
        84600,
        87900,
        91300,
        94800,
        98400,
        102100,
        105900,
        109800,
        113800,
    ]
)

# Calculate income multiple gaps dynamically (G7 divided by BRICS)
multiples = [f"{g / b:.2f}x" for b, g in zip(brics_ppp, g7_ppp)]

fig, ax = plt.subplots(figsize=(16, 10))

# 1. Plot Historical Lines (2016 to 2026 - Indices 0 to 10)
ax.plot(
    years[:11],
    brics_ppp[:11],
    color="#A21C26",
    linestyle="-",
    marker="o",
    linewidth=2.5,
    label="BRICS PPP Average (Historical)",
)
ax.plot(
    years[:11],
    g7_ppp[:11],
    color="#1D4ED8",
    linestyle="-",
    marker="o",
    linewidth=2.5,
    label="G7 PPP Average (Historical)",
)

# 2. Plot Projection Lines (2026 to 2036 - Indices 10 to 20)
ax.plot(
    years[10:],
    brics_ppp[10:],
    color="#A21C26",
    linestyle=":",
    marker="o",
    linewidth=2.5,
    label="BRICS PPP Average (Projected)",
)
ax.plot(
    years[10:],
    g7_ppp[10:],
    color="#1D4ED8",
    linestyle=":",
    marker="o",
    linewidth=2.5,
    label="G7 PPP Average (Projected)",
)

# 3. Add Data Value Annotations for every sequential coordinate point
for i in range(len(years)):
    # BRICS Labels (offset underneath the trajectory marker)
    ax.annotate(
        f"${brics_ppp[i]:,}",
        (years[i], brics_ppp[i]),
        textcoords="offset points",
        xytext=(0, -15),
        ha="center",
        fontsize=8,
        color="#781017",
        weight="bold",
    )
    # G7 Labels (offset above the trajectory marker)
    ax.annotate(
        f"${g7_ppp[i]:,}",
        (years[i], g7_ppp[i]),
        textcoords="offset points",
        xytext=(0, 10),
        ha="center",
        fontsize=8,
        color="#112E82",
        weight="bold",
    )

# 4. Vertical Double-Headed Tracking Arrows highlighting the wealth multiple gaps
# Set tracking locations at key anchors: start (2016), present day (2026), and end target (2036)
gap_years = [0, 10, 20]
for idx in gap_years:
    ax.annotate(
        "",
        xy=(years[idx], brics_ppp[idx]),
        xytext=(years[idx], g7_ppp[idx]),
        arrowprops=dict(arrowstyle="<->", color="#581C87", lw=2.5, ls="--"),
    )

    # Position gap metrics directly in the center boundary of the tracking lines
    mid_y = (brics_ppp[idx] + g7_ppp[idx]) / 2
    ax.text(
        years[idx] + 0.2,
        mid_y,
        f"Gap:\n{multiples[idx]}",
        color="#581C87",
        weight="bold",
        fontsize=11,
        bbox=dict(facecolor="white", alpha=0.8, edgecolor="none"),
    )

# Graphical standard formatting
ax.set_title(
    "Global Economic Shift: G7 vs. BRICS Average GDP per Capita (PPP) Catch-up",
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
ax.grid(True, linestyle="--", alpha=0.3)
ax.legend(loc="upper left", fontsize=11, framealpha=0.9)

# Baseline milestone tracking line splitting historical execution from projected assumptions
ax.axvline(x=2026, color="gray", linestyle="--", alpha=0.7, linewidth=1.5)
ax.text(2026.1, 50000, "2026 Baseline", color="gray", rotation=90, weight="bold")

plt.tight_layout()
plt.show()
