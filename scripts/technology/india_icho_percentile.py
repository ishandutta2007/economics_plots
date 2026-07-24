import matplotlib.pyplot as plt
import pandas as pd

# Historical IChO Data for India (1999 - 2026)
# Format: (Year, India's Unofficial Team Rank, Total Participating Countries)
icho_data = [
    (1999, 21, 52), (2000, 10, 53), (2001, 7, 54),  (2002, 10, 57), (2003, 5, 59),
    (2004, 15, 61), (2005, 14, 59), (2006, 17, 67), (2007, 14, 68), (2008, 17, 66),
    (2009, 11, 64), (2010, 22, 68), (2011, 15, 70), (2012, 6, 72),  (2013, 11, 73),
    (2014, 11, 75), (2015, 17, 75), (2016, 21, 75), (2017, 18, 76), (2018, 14, 76),
    (2019, 10, 80), (2021, 12, 85), (2022, 16, 84), (2023, 12, 89), (2024, 19, 90),
    (2025, 6, 90),  (2026, 1, 93)
]

# Create DataFrame
df = pd.DataFrame(icho_data, columns=["Year", "Rank", "Total_Countries"])

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

# Highlight standout historic peaks (Top-10 finishes)
top_milestones = df[df["Rank"] <= 10]
plt.scatter(
    top_milestones["Year"],
    top_milestones["Percentile"],
    color="#e74c3c",
    s=120,
    zorder=5,
    label="Top 10 Finishes",
)

# Specifically label the all-time high water mark (2026)
best_2026 = df[df["Year"] == 2026].iloc[0]
plt.annotate(
    f"🏆 Historic Peak!\nRank {int(best_2026['Rank'])} of {int(best_2026['Total_Countries'])}\n({best_2026['Percentile']:.0f}th Percentile)",
    xy=(2026, best_2026["Percentile"]),
    xytext=(2021, best_2026["Percentile"] - 6),
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
    "India's IChO Performance Percentile (1989-2026)\nRelative Positioning to Overall Pool Size",
    fontsize=16,
    fontweight="bold",
    pad=15,
)
plt.xlabel("Year", fontsize=12, labelpad=10)
plt.ylabel("Competitive Percentile (%) — Higher is Better", fontsize=12, labelpad=10)
plt.xlim(1987, 2028)
plt.ylim(45, 103)
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
