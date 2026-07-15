import matplotlib.pyplot as plt

# Data
periods = ["1100 CE", "1757", "1947", "2021", "2026"]
ranks = [1, 10, 100, 132, 148]

# Create figure with a professional size
fig, ax = plt.subplots(figsize=(10, 6))

# Use a professional color palette (Deep Teal/Navy)
bar_color = "#2c3e50"
bars = ax.bar(periods, ranks, color=bar_color, alpha=0.85, width=0.6)

# Add labels above each bar with better formatting
for bar, rank in zip(bars, ranks):
    label = f"Rank ~{rank}" if rank <= 100 else f"Rank {rank}"
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 2,
        label,
        ha="center",
        va="bottom",
        fontsize=18,
        fontweight="bold",
        color="#34495e",
    )

# Title and Labels
ax.set_title(
    "India's GDP Per Capita Rank Through History",
    fontsize=20,
    fontweight="bold",
    pad=45,
)
ax.set_ylabel("Global Rank (Lower is Better)", fontsize=11, labelpad=15)

# Add a subtle subtitle for context - adjusted position to avoid title overlap
ax.text(
    0.5,
    1.02,
    "Illustrative milestones showing India's relative economic position",
    transform=ax.transAxes,
    ha="center",
    fontsize=11,
    color="#666666",
    style="italic",
)

# Adjust y-axis to provide breathing room at the top
ax.set_ylim(0, max(ranks) * 1.15)

# Add horizontal grid lines for readability
ax.yaxis.grid(True, linestyle="--", alpha=0.6)
ax.set_axisbelow(True)

# Clean up spines (borders)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_alpha(0.3)
ax.spines["bottom"].set_alpha(0.3)

# Customize ticks for a cleaner look
ax.tick_params(axis="both", which="major", labelsize=10, colors="#2c3e50")

# Add a source/note at the bottom
plt.figtext(
    0.99,
    0.01,
    "Source: Illustrative Historical Milestones",
    ha="right",
    fontsize=8,
    color="#7f8c8d",
    style="italic",
)

plt.tight_layout()
import os

os.makedirs(
    os.path.join(os.path.dirname(__file__), "..", "..", "assets"), exist_ok=True
)
plt.savefig(
    os.path.join(
        os.path.dirname(__file__), "..", "..", "assets", "india_gdppc_rank.png"
    ),
    dpi=100,
)
plt.show()
