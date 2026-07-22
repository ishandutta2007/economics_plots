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
    "United States": [2000, 1014, 800, 725, 900, 750],  # Left Axis
    "Russia/USSR": [40, 40, 35, 10, 15, 25],  # Right Axis
    "United Kingdom": [500, 180, 90, 60, 50, 60],  # Right Axis
    "China": [0, 0, 0, 0, 1, 8],  # Right Axis
    "India": [0, 0, 0, 1, 1, 4],  # Right Axis
}

# Create a figure with dual y-axes due to the massive scale disparity of the U.S.
fig, ax1 = plt.subplots(figsize=(14, 8))
ax2 = ax1.twinx()

# Plot lines and store reference handles
line_us = ax1.plot(
    years,
    base_counts["United States"],
    color="#d62728",
    linestyle="-",
    marker="o",
    linewidth=2.5,
    label="United States (Left)",
)
line_ru = ax2.plot(
    years,
    base_counts["Russia/USSR"],
    color="#1f77b4",
    linestyle="--",
    marker="s",
    linewidth=2,
    label="Russia/USSR (Right)",
)
line_uk = ax2.plot(
    years,
    base_counts["United Kingdom"],
    color="#2ca02c",
    linestyle="-.",
    marker="^",
    linewidth=2,
    label="United Kingdom (Right)",
)
line_ch = ax2.plot(
    years,
    base_counts["China"],
    color="#ff7f0e",
    linestyle=":",
    marker="d",
    linewidth=2,
    label="China (Right)",
)
line_in = ax2.plot(
    years,
    base_counts["India"],
    color="#9467bd",
    linestyle="-",
    marker="x",
    linewidth=2,
    label="India (Right)",
)


# Helper function to dynamically add labels to each point to avoid overlaps
def annotate_points(ax, x_data, y_data, color, offset_y=10, position="top"):
    for x, y in zip(x_data, y_data):
        # Determine label position relative to data point
        xy_text = (0, offset_y) if position == "top" else (0, -offset_y)
        va = "bottom" if position == "top" else "top"

        ax.annotate(
            f"{y}",
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


# Annotate each curve using specialized positions to maximize legibility
annotate_points(
    ax1, years, base_counts["United States"], "#d62728", offset_y=12, position="top"
)
annotate_points(
    ax2, years, base_counts["Russia/USSR"], "#1f77b4", offset_y=12, position="top"
)
annotate_points(
    ax2, years, base_counts["United Kingdom"], "#2ca02c", offset_y=12, position="bottom"
)

# Adjusting offsets slightly for overlapping modern Asian postures
annotate_points(
    ax2, years[-2:], base_counts["China"][-2:], "#ff7f0e", offset_y=14, position="top"
)
annotate_points(
    ax2,
    years[-2:],
    base_counts["India"][-2:],
    "#9467bd",
    offset_y=14,
    position="bottom",
)

# Labeling and axis boundaries
ax1.set_xlabel("Year", fontsize=11, fontweight="bold", labelpad=10)
ax1.set_ylabel(
    "U.S. Overseas Bases Scale", color="#d62728", fontsize=11, fontweight="bold"
)
ax2.set_ylabel(
    "Other Nations Bases Scale", color="#333333", fontsize=11, fontweight="bold"
)

ax1.set_ylim(500, 2300)
ax2.set_ylim(-20, 600)
plt.xlim(1940, 2032)

# Merge legends from both axes into a single box
lines = line_us + line_ru + line_uk + line_ch + line_in
labels = [l.get_label() for l in lines]
ax1.legend(
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
ax1.grid(True, linestyle="--", alpha=0.3)

plt.tight_layout()
plt.show()
