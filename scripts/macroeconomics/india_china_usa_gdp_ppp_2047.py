import matplotlib.pyplot as plt
import numpy as np

# Data configuration (in Trillions of USD - Current/Inflated terms)
countries = ["China 🇨🇳", "United States 🇺🇸", "India 🇮🇳"]
years = ["2026", "2047"]

# GDP Metrics: [2026 Value, 2047 Value]
nominal_data = {
    "China 🇨🇳": [20.8, 52.0],
    "United States 🇺🇸": [32.4, 51.5],
    "India 🇮🇳": [4.2, 33.5],
}

ppp_data = {
    "China 🇨🇳": [44.3, 103.0],
    "United States 🇺🇸": [32.4, 51.5],
    "India 🇮🇳": [18.9, 103.0],
}

# Setup the side-by-side plot layout
fig, axes = plt.subplots(1, 2, figsize=(15, 6), sharey=False)
colors = ["#1f77b4", "#aec7e8"]  # 2026 vs 2047 color scheme
x = np.arange(len(countries))
width = 0.35

# --- Plot 1: Nominal GDP ---
axes[0].bar(
    x - width / 2,
    [nominal_data[c][0] for c in countries],
    width,
    label="2026",
    color=colors[0],
    edgecolor="grey",
)
axes[0].bar(
    x + width / 2,
    [nominal_data[c][1] for c in countries],
    width,
    label="2047 (Projected)",
    color=colors[1],
    edgecolor="grey",
)
axes[0].set_title(
    "Nominal GDP Growth (Current $)", fontsize=14, fontweight="bold", pad=15
)
axes[0].set_ylabel("GDP in Trillions ($)", fontsize=12)
axes[0].set_xticks(x)
axes[0].set_xticklabels(countries, fontsize=11)
axes[0].grid(axis="y", linestyle="--", alpha=0.7)
axes[0].legend(fontsize=11)

# Add data labels inside Nominal bars
for i, c in enumerate(countries):
    axes[0].text(
        i - width / 2,
        nominal_data[c][0] + 1,
        f"${nominal_data[c][0]}T",
        ha="center",
        va="bottom",
        fontsize=10,
    )
    axes[0].text(
        i + width / 2,
        nominal_data[c][1] + 1,
        f"${nominal_data[c][1]}T",
        ha="center",
        va="bottom",
        fontsize=10,
        fontweight="bold",
    )

# --- Plot 2: PPP GDP ---
axes[1].bar(
    x - width / 2,
    [ppp_data[c][0] for c in countries],
    width,
    label="2026",
    color=colors[0],
    edgecolor="grey",
)
axes[1].bar(
    x + width / 2,
    [ppp_data[c][1] for c in countries],
    width,
    label="2047 (Projected)",
    color=colors[1],
    edgecolor="grey",
)
axes[1].set_title("PPP GDP Growth (Current $)", fontsize=14, fontweight="bold", pad=15)
axes[1].set_xticks(x)
axes[1].set_xticklabels(countries, fontsize=11)
axes[1].grid(axis="y", linestyle="--", alpha=0.7)
axes[1].legend(fontsize=11)

# Add data labels inside PPP bars
for i, c in enumerate(countries):
    axes[1].text(
        i - width / 2,
        ppp_data[c][0] + 2,
        f"${ppp_data[c][0]}T",
        ha="center",
        va="bottom",
        fontsize=10,
    )
    axes[1].text(
        i + width / 2,
        ppp_data[c][1] + 2,
        f"${ppp_data[c][1]}T",
        ha="center",
        va="bottom",
        fontsize=10,
        fontweight="bold",
    )

# Global plot layout settings
plt.suptitle(
    "Global Superpower Economic Shift (2026 vs 2047)",
    fontsize=16,
    fontweight="bold",
    y=1.02,
)
plt.tight_layout()

# Show the chart layout
plt.show()
