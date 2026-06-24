import pandas as pd
import matplotlib.pyplot as plt

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
data = {
    "University": [
        "MIT",
        "Stanford",
        "Oxford",
        "Cambridge",
        "Harvard",
        "Caltech",
        "IIT Madras",
        "Tsinghua"
    ],
    "Patents_Granted_2025": [291, 201, 60, 80, 157, 129, 221, 900],
    "Research_Grants_USD_M": [2206, 2300, 1042, 803, 1005, 445, 136, 2750]
}

df = pd.DataFrame(data)

# Patents granted per $1 million of research grants
df["Universities_Patent_Per_Dollar"] = (
    df["Patents_Granted_2025"] / df["Research_Grants_USD_M"]
)

# Sort for better visualization
df = df.sort_values(
    "Universities_Patent_Per_Dollar",
    ascending=False
)

# Plot
plt.figure(figsize=(10, 6))
bars = plt.bar(
    df["University"],
    df["Universities_Patent_Per_Dollar"]
)

plt.title("Patents Granted per $1 Million Research Grant (2025)")
plt.ylabel("Patents per $1M Research Funding")
plt.xlabel("University")
plt.figtext(0.85, 0.01, "Data Sources: NAI Top 100, NSF HERD, Official University Reports", wrap=True, horizontalalignment='center', fontsize=7)

# Value labels
for bar, value in zip(bars, df["Universities_Patent_Per_Dollar"]):
    plt.text(
        bar.get_x() + bar.get_width()/2,
        value,
        f"{value:.2f}",
        ha="center",
        va="bottom"
    )

plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.show()

# Optional: print exact values
print(
    df[["University", "Universities_Patent_Per_Dollar"]]
    .to_string(index=False)
)
