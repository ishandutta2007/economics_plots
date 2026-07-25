import matplotlib.pyplot as plt
import pandas as pd

# Historical IOI Data for India (2003 - 2025)
# Format: (Year, India's Unofficial Team Rank, Total Participating Countries)
# Source: stats.ioinformatics.org (unofficial team rank computed from sum of
# individual scores). India first participated in IOI 2003.
ioi_data = [
    (2003, 29, 69),
    (2004, 27, 81),
    (2005, 15, 72),
    (2006, 27, 74),
    (2007, 28, 77),
    (2008, 32, 78),
    (2009, 24, 78),
    (2010, 18, 80),
    (2011, 36, 78),
    (2012, 51, 81),
    (2013, 25, 77),
    (2014, 21, 81),
    (2015, 24, 83),
    (2016, 18, 80),
    (2017, 30, 83),
    (2018, 70, 87),
    (2019, 33, 87),
    (2020, 19, 87),
    (2021, 20, 88),
    (2022, 20, 88),
    (2023, 11, 87),
    (2024, 13, 91),
    (2025, 29, 84),
]


# Create DataFrame
df = pd.DataFrame(ioi_data, columns=["Year", "Rank", "Total_Countries"])

# Calculate the competitive percentile (Higher is better, 100% = 1st place)
df["Percentile"] = (1 - (df["Rank"] - 1) / df["Total_Countries"]) * 100

# Initialize the plot
plt.figure(figsize=(18, 10))

# Plot the primary percentile path
plt.plot(
    df["Year"],
    df["Percentile"],
    marker="o",
    linestyle="-",
    color="#2c3e50",
    linewidth=2,
    markersize=5,
    alpha=0.8,
    label="India's Performance Percentile",
)

# Annotate every individual data point with its Rank / Total Countries string
prepct = 0
minpct = 101
for i, row in df.iterrows():
    year = int(row["Year"])
    rank = int(row["Rank"])
    total = int(row["Total_Countries"])
    pct = row["Percentile"]

    # Toggle text positions slightly to avoid visual overlap
    if pct > prepct:
        yano = 8
    else:
        yano = -14
    xy_text_offset = (0, yano)  # if rank % 2 == 0 else (0, -14)

    plt.annotate(
        f"{pct:.0f}%ile ({rank}/{total})",
        xy=(year, pct),
        xytext=xy_text_offset,
        textcoords="offset points",
        ha="center",
        fontsize=8,
        color="#34495e",
        weight="semibold",
    )
    prepct = pct
    minpct = min(minpct, pct)

# Highlight standout historic peaks (Top-10 finishes)
top_milestones = df[df["Rank"] / df["Total_Countries"] <= 0.20]
plt.scatter(
    top_milestones["Year"],
    top_milestones["Percentile"],
    color="#e74c3c",
    s=120,
    zorder=5,
    label="Top 10 Finishes",
)

# Specifically label the all-time high water mark (2023)
best_year = df.loc[df["Percentile"].idxmax()]
plt.annotate(
    f"🏆 Historic Peak!\nRank {int(best_year['Rank'])} of {int(best_year['Total_Countries'])}\n({best_year['Percentile']:.1f}th Percentile)",
    xy=(best_year["Year"], best_year["Percentile"]),
    xytext=(best_year["Year"] - 5, best_year["Percentile"] - 2),
    arrowprops=dict(
        facecolor="#e74c3c", arrowstyle="->", connectionstyle="arc3,rad=-0.1"
    ),
    fontsize=11,
    fontweight="bold",
    color="#e74c3c",
    ha="center",
    fontname="Segoe UI Emoji",
)

# Plot customization
plt.title(
    f"India's IOI Performance Percentile ({ioi_data[0][0]} - {ioi_data[-1][0]})\nRelative Positioning to Overall Pool Size",
    fontsize=16,
    fontweight="bold",
    pad=15,
)
plt.xlabel("Year", fontsize=12, labelpad=10)
plt.ylabel("Competitive Percentile (%) — Higher is Better", fontsize=12, labelpad=10)

plt.xlim(ioi_data[0][0] - 1, ioi_data[-1][0] + 1)
plt.ylim(minpct - 6, 103)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(loc="lower left", fontsize=11)

# # Informative visual anchor for the 2020 gap
# plt.axvspan(2019.5, 2020.5, color="#ecf0f1", alpha=0.7, zorder=1)
# plt.text(
#     2020,
#     55,
#     "2020\nNo Participation",
#     color="#7f8c8d",
#     fontsize=9,
#     ha="center",
#     fontweight="bold",
# )

plt.tight_layout()
plt.savefig("assets/india_ioi_percentile.png")
plt.show()
