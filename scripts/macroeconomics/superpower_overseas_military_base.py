import matplotlib.pyplot as plt

# Timeline spanning key geopolitical eras from Post-WWII to 2026
years = [1945, 1967, 1991, 1998, 2011, 2026]

# Historical base estimates based on global defense tracking data
# Sources:
# US: Blaker (1990) historical series; DoD Base Structure Reports; Vine (2015) "Base Nation"
# Russia/USSR: PONARS Eurasia; CIA archives; defence24.com — USSR relied on Warsaw Pact
#              continental forces + limited overseas access agreements, not sovereign bases
# UK: Post-imperial drawdown; ~145 sites (2026) per investigative research, incl. allied facilities
# China: Djibouti base opened Aug 2017 (first ever); Ream Naval Base (Cambodia) de facto ~2021+
# India: Farkhor AB (Tajikistan) closed 2022; Agaléga Island (Mauritius) inaugurated 2024
base_counts = {
    "United States": [2000, 1014, 800, 725, 900, 750],
    "Russia/USSR": [40, 40, 35, 10, 15, 25],
    "United Kingdom": [500, 180, 90, 60, 50, 60],
    "China": [0.5, 0.5, 0.5, 0.5, 1, 8],   # 0 → 0.5 for log scale (no overseas bases)
    "India": [0.5, 0.5, 0.5, 1, 1, 4],      # 0 → 0.5 for log scale (no overseas bases)
}

# Single-axis figure
fig, ax = plt.subplots(figsize=(14, 8))

# Plot all lines on the single axis
line_us = ax.plot(
    years,
    base_counts["United States"],
    color="#d62728",
    linestyle="-",
    marker="o",
    linewidth=2.5,
    label="United States",
)
line_ru = ax.plot(
    years,
    base_counts["Russia/USSR"],
    color="#1f77b4",
    linestyle="--",
    marker="s",
    linewidth=2,
    label="Russia/USSR",
)
line_uk = ax.plot(
    years,
    base_counts["United Kingdom"],
    color="#2ca02c",
    linestyle="-.",
    marker="^",
    linewidth=2,
    label="United Kingdom",
)
line_ch = ax.plot(
    years,
    base_counts["China"],
    color="#ff7f0e",
    linestyle=":",
    marker="d",
    linewidth=2,
    label="China",
)
line_in = ax.plot(
    years,
    base_counts["India"],
    color="#9467bd",
    linestyle="-",
    marker="x",
    linewidth=2,
    label="India",
)


# Helper function to dynamically add labels to each point to avoid overlaps
def annotate_points(ax, x_data, y_data, color, offset_y=10, position="top"):
    for x, y in zip(x_data, y_data):
        # Skip placeholder values used to avoid log(0)
        display_label = "<1" if y == 0.5 else f"{y}"

        # Determine label position relative to data point
        xy_text = (0, offset_y) if position == "top" else (0, -offset_y)
        va = "bottom" if position == "top" else "top"

        ax.annotate(
            display_label,
            (x, y),
            textcoords="offset points",
            xytext=xy_text,
            ha="center",
            va=va,
            fontsize=9,
            fontweight="bold",
            color=color,
            bbox=dict(
                boxstyle="round,pad=0.2", fc="white", ec=color, alpha=0.7, lw=0.5
            ),
        )


# Annotate each curve
annotate_points(ax, years, base_counts["United States"], "#d62728", offset_y=12, position="top")
annotate_points(ax, years, base_counts["Russia/USSR"], "#1f77b4", offset_y=12, position="top")
annotate_points(ax, years, base_counts["United Kingdom"], "#2ca02c", offset_y=12, position="bottom")

# Adjusting offsets slightly for overlapping modern Asian postures
annotate_points(ax, years[-2:], base_counts["China"][-2:], "#ff7f0e", offset_y=14, position="top")
annotate_points(ax, years[-2:], base_counts["India"][-2:], "#9467bd", offset_y=14, position="bottom")

# Labeling and axis boundaries
ax.set_xlabel("Year", fontsize=11, fontweight="bold", labelpad=10)
ax.set_ylabel("Number of Overseas Military Bases (log scale)", fontsize=11, fontweight="bold")

ax.set_yscale("log")
ax.set_ylim(0.3, 3000)
plt.xlim(1940, 2032)

# Single combined legend
lines = line_us + line_ru + line_uk + line_ch + line_in
labels = [l.get_label() for l in lines]
ax.legend(
    lines,
    labels,
    loc="upper right",
    frameon=True,
    facecolor="white",
    edgecolor="#cccccc",
)

# Visual styling
plt.title(
    "Global Overseas Military Base Trajectories (1945 – 2026)\n"
    "Sources: Blaker (1990), DoD Base Structure Reports, PONARS Eurasia, Vine (2015)",
    fontsize=13,
    fontweight="bold",
    pad=20,
)
ax.grid(True, linestyle="--", alpha=0.3)

plt.tight_layout()
plt.show()
