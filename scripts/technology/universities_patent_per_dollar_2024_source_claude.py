import os
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

file_path_without_ext = os.path.splitext(os.path.abspath(__file__))[0]
filename_without_ext = os.path.basename(file_path_without_ext)
script_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = Path(__file__).resolve().parent.parent.parent / "assets"
output_path = os.path.join(assets_dir, f"{filename_without_ext}.png")

# Data from the table
# Notes:
#   - IISc Bangalore: 111 patents granted in FY2023-24 (NIRF 2025 submission)
#   - IISc research: NIRF 2025 reports Rs.1,111.85 Cr (~$134M) sponsored research
data = {
    "University": [
        "MIT",
        "Stanford",
        "Oxford",
        "Cambridge",
        "Harvard",
        "Caltech",
        "IIT Madras",
        "IISc Bangalore",
        "Tsinghua",
    ],
    "Patents_Granted_2024": [295, 199, 57, 75, 155, 143, 435, 111, 900],
    "Research_Grants_USD_M": [2379, 2200, 1039, 790, 1020, 445.2, 138, 134, 2750],
}

df = pd.DataFrame(data)

# Country mapping and colors
university_country = {
    "MIT": "USA",
    "Stanford": "USA",
    "Harvard": "USA",
    "Caltech": "USA",
    "Oxford": "UK",
    "Cambridge": "UK",
    "IIT Madras": "India",
    "IISc Bangalore": "India",
    "Tsinghua": "China",
}

country_colors = {
    "USA": "#1f77b4",
    "UK": "#2ca02c",
    "India": "#ff7f0e",
    "China": "#d62728",
}

df["Country"] = df["University"].map(university_country)

# Patents granted per $1 million of research grants
df["Universities_Patent_Per_Dollar"] = (
    df["Patents_Granted_2024"] / df["Research_Grants_USD_M"]
)

# Sort for better visualization
df = df.sort_values("Universities_Patent_Per_Dollar", ascending=False)

# Plot
import matplotlib

matplotlib.use("Agg")  # Non-interactive backend to prevent blocking
plt.figure(figsize=(11, 7))
bar_colors = df["Country"].map(country_colors)
bars = plt.bar(
    df["University"],
    df["Universities_Patent_Per_Dollar"],
    color=bar_colors,
    edgecolor="black",
    linewidth=0.7,
)

# Grid
plt.grid(axis="y", linestyle="--", alpha=0.5, zorder=0)
for bar in bars:
    bar.set_zorder(3)

# Legend (one entry per country)
from matplotlib.patches import Patch

legend_handles = [
    Patch(facecolor=color, edgecolor="black", label=country)
    for country, color in country_colors.items()
]
plt.legend(
    handles=legend_handles,
    title="Country",
    title_fontsize=12,
    fontsize=11,
    loc="upper right",
)

plt.title(
    "Patents Granted per $1 Million Research Grant (2024)",
    fontsize=15,
    fontweight="bold",
    pad=15,
)
plt.ylabel(
    "Patents per $1M Research Funding", fontsize=12, fontweight="medium", labelpad=10
)
# plt.xlabel("University", fontsize=12, fontweight="medium", labelpad=10)
plt.figtext(
    0.5,
    0.01,
    "Data Sources: NAI Top 100, NSF HERD, Official University Reports",
    wrap=True,
    horizontalalignment="left",
    fontsize=9,
    style="italic",
)

# Value labels on top of the bars
for bar, value in zip(bars, df["Universities_Patent_Per_Dollar"]):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        value + 0.05,
        f"{value:.2f}",
        ha="center",
        va="bottom",
        fontsize=11,
        fontweight="bold",
    )

plt.xticks(rotation=45, ha="right", fontsize=16, fontweight="bold")
plt.yticks(fontsize=11)
plt.ylim(0, df["Universities_Patent_Per_Dollar"].max() + 0.4)  # Leave room for labels
plt.tight_layout()
plt.savefig(output_path, dpi=300)
# plt.show() - Commented out to prevent GUI hanging, but saves the file

# Optional: print exact values
print(df[["University", "Universities_Patent_Per_Dollar"]].to_string(index=False))
