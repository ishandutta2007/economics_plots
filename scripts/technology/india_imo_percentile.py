import matplotlib.pyplot as plt
import pandas as pd

# Historical IMO Data for India (1989 - 2026)
# Format: (Year, India's Rank, Total Participating Countries)
# Note: 2020 is omitted as India did not participate due to the pandemic.
imo_data = [
    (1989, 25, 50),
    (1990, 17, 54),
    (1991, 10, 56),
    (1992, 21, 56),
    (1993, 15, 73),
    (1994, 16, 69),
    (1995, 24, 73),
    (1996, 14, 75),
    (1997, 21, 82),
    (1998, 7, 76),
    (1999, 18, 81),
    (2000, 14, 82),
    (2001, 7, 83),
    (2002, 9, 84),
    (2003, 15, 82),
    (2004, 14, 85),
    (2005, 36, 91),
    (2006, 35, 90),
    (2007, 25, 93),
    (2008, 31, 97),
    (2009, 28, 104),
    (2010, 36, 95),
    (2011, 23, 101),
    (2012, 11, 100),
    (2013, 29, 97),
    (2014, 39, 101),
    (2015, 37, 104),
    (2016, 34, 109),
    (2017, 52, 111),
    (2018, 28, 107),
    (2019, 15, 112),
    (2021, 26, 107),
    (2022, 24, 104),
    (2023, 9, 112),
    (2024, 4, 108),
    (2025, 7, 115),
    (2026, 7, 117),
]

# Create DataFrame
df = pd.DataFrame(imo_data, columns=["Year", "Rank", "Total_Countries"])

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
top_milestones = df[df["Rank"] / df["Total_Countries"] <= 0.10]
plt.scatter(
    top_milestones["Year"],
    top_milestones["Percentile"],
    color="#e74c3c",
    s=120,
    zorder=5,
    label="Top 10 Finishes",
)

# Specifically label the all-time high water mark (2024)
best_2024 = df[df["Year"] == 2024].iloc[0]
plt.annotate(
    f"🏆 Historic Peak!\nRank {int(best_2024['Rank'])} of {int(best_2024['Total_Countries'])}\n({best_2024['Percentile']:.1f}th Percentile)",
    xy=(2024, best_2024["Percentile"]),
    xytext=(2019, best_2024["Percentile"] - 6),
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
    "India's IMO Performance Percentile (1989-2026)\nRelative Positioning to Overall Pool Size",
    fontsize=16,
    fontweight="bold",
    pad=15,
)
plt.xlabel("Year", fontsize=12, labelpad=10)
plt.ylabel("Competitive Percentile (%) — Higher is Better", fontsize=12, labelpad=10)
plt.xlim(imo_data[0][0] - 1, imo_data[-1][0] + 1)
plt.ylim(minpct - 6, 103)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(loc="lower left", fontsize=11)

# Informative visual anchor for the 2020 gap
plt.axvspan(2019.5, 2020.5, color="#ecf0f1", alpha=0.7, zorder=1)
plt.text(
    2020,
    55,
    "2020\nNo Participation",
    color="#7f8c8d",
    fontsize=9,
    ha="center",
    fontweight="bold",
)

plt.tight_layout()
plt.show()
