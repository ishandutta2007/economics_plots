import os
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

file_path_without_ext = os.path.splitext(os.path.abspath(__file__))[0]
filename_without_ext = os.path.basename(file_path_without_ext)
script_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = Path(__file__).resolve().parent.parent.parent / "assets"
output_path = os.path.join(assets_dir, f"{filename_without_ext}.png")

# Data for 2025
# Patents: NAI CY2025 (U.S. utility patents) where available;
#          official university reports for IIT Madras;
#          estimates for Oxford, Cambridge, Tsinghua (see notes below)
# Research: Official FY2025 reports, converted to USD where needed
#
# Notes:
#   - Oxford/Cambridge: Not on NAI Top 100. Oxford ~60 est. (from OUI filings),
#     Cambridge ~80 est. (from Cambridge Enterprise data). Both report filings, not grants.
#   - Tsinghua: NAI gives 126 U.S. utility patents only. Total global patents
#     estimated ~900 (consistent with 2024 AI/ML patent volume). Using 900 for
#     comparability with 2024 dataset.
#   - IIT Madras: 221 patents granted in FY2024-25 (official, 207 Indian + 14 intl.)
#   - IIT Madras research: NIRF 2025 reports Rs.1,128.82 Cr (~$136M) sponsored research
#   - IISc Bangalore: 176 patents granted in FY2024-25 (NIRF 2026 submission)
#   - IISc research: NIRF 2026 reports Rs.1,070.02 Cr (~$128M) sponsored research
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
    "Patents_Granted_2025": [291, 201, 60, 80, 157, 129, 221, 176, 900],
    "Research_Grants_USD_M": [2206, 2300, 1042, 803, 1005, 445, 136, 128, 2750],
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
    df["Patents_Granted_2025"] / df["Research_Grants_USD_M"]
)

# Sort for better visualization
df = df.sort_values("Universities_Patent_Per_Dollar", ascending=False)

# Plot
plt.figure(figsize=(10, 6))
bar_colors = df["Country"].map(country_colors)
bars = plt.bar(df["University"], df["Universities_Patent_Per_Dollar"], color=bar_colors)

# Legend (one entry per country)
from matplotlib.patches import Patch
legend_handles = [Patch(facecolor=color, label=country) for country, color in country_colors.items()]
plt.legend(handles=legend_handles, title="Country")

plt.title("Patents Granted per $1 Million Research Grant (2025)")
plt.ylabel("Patents per $1M Research Funding")
plt.xlabel("University")
plt.figtext(
    0.85,
    0.01,
    "Data Sources: NAI Top 100, NSF HERD, Official University Reports",
    wrap=True,
    horizontalalignment="center",
    fontsize=7,
)

# Value labels
for bar, value in zip(bars, df["Universities_Patent_Per_Dollar"]):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        value,
        f"{value:.2f}",
        ha="center",
        va="bottom",
    )

plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig(output_path)
plt.show()

# Optional: print exact values
print(df[["University", "Universities_Patent_Per_Dollar"]].to_string(index=False))
