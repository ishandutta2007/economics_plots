import matplotlib.pyplot as plt
import pandas as pd

# Historical IOI Data for India (2002 - 2026)
# Format: (Year, India's Unofficial Team Rank, Total Participating Countries)
ioi_data = [
    (2002, 33, 77), (2003, 35, 75), (2004, 30, 81), (2005, 34, 72), (2006, 27, 74),
    (2007, 31, 76), (2008, 33, 78), (2009, 36, 78), (2010, 32, 80), (2011, 33, 78),
    (2012, 38, 81), (2013, 29, 77), (2014, 25, 81), (2015, 27, 83), (2016, 26, 80),
    (2017, 30, 83), (2018, 28, 87), (2019, 31, 87), (2020, 24, 87), (2021, 26, 88),
    (2022, 23, 89), (2023, 19, 87), (2024, 18, 91), (2025, 15, 90), (2026, 12, 92)]


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
    f"🏆 Historic Peak!\nRank {int(best_2026['Rank'])} of {int(best_2026['Total_Countries'])}\n({best_2026['Percentile']:.1f}th Percentile)",
    xy=(2026, best_2026["Percentile"]),
    xytext=(2021, best_2026["Percentile"] - 2),
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
    "India's IOI Performance Percentile (1989-2026)\nRelative Positioning to Overall Pool Size",
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
plt.show()
