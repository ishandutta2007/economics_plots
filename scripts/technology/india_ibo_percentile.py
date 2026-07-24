import matplotlib.pyplot as plt
import pandas as pd

# Historical IBO Data for India (2000 - 2026)
# Format: (Year, India's Unofficial Team Rank, Total Participating Countries)
ibo_data = [
    (2000, 18, 38),
    (2001, 14, 38),
    (2002, 11, 40),
    (2003, 10, 45),
    (2004, 11, 48),
    (2005, 9, 50),
    (2006, 12, 55),
    (2007, 10, 49),
    (2008, 11, 55),
    (2009, 3, 56),
    (2010, 14, 60),
    (2011, 12, 58),
    (2012, 7, 59),
    (2013, 15, 62),
    (2014, 16, 61),
    (2015, 18, 61),
    (2016, 17, 68),
    (2017, 15, 64),
    (2018, 8, 68),
    (2019, 15, 73),
    (2021, 11, 76),
    (2022, 14, 65),
    (2023, 1, 76),
    (2024, 16, 73),
    (2025, 12, 75),
    (2026, 11, 78),
]


# Create DataFrame
df = pd.DataFrame(ibo_data, columns=["Year", "Rank", "Total_Countries"])

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

# Specifically label the all-time high water mark (2023)
best_2023 = df[df["Year"] == 2023].iloc[0]
plt.annotate(
    f"🏆 Historic Peak!\nRank {int(best_2023['Rank'])} of {int(best_2023['Total_Countries'])}\n({best_2023['Percentile']:.1f}th Percentile)",
    xy=(2023, best_2023["Percentile"]),
    xytext=(2018, best_2023["Percentile"] - 6),
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
    "India's IBO Performance Percentile (1989-2026)\nRelative Positioning to Overall Pool Size",
    fontsize=16,
    fontweight="bold",
    pad=15,
)
plt.xlabel("Year", fontsize=12, labelpad=10)
plt.ylabel("Competitive Percentile (%) — Higher is Better", fontsize=12, labelpad=10)
plt.xlim(ibo_data[0][0] - 1, ibo_data[-1][0] + 1)
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
