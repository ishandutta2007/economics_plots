import matplotlib.pyplot as plt
import pandas as pd

# Historical IOAA Data for India (2007 - 2026)
# Format: (Year, India's Unofficial Team Rank, Total Participating Countries)
ioaa_data = [
    (2007, 3, 21),
    (2008, 2, 22),
    (2009, 2, 19),
    (2010, 2, 22),
    (2011, 4, 26),
    (2012, 3, 27),
    (2013, 5, 35),
    (2014, 4, 37),
    (2015, 4, 39),
    (2016, 1, 41),
    (2017, 3, 46),
    (2018, 5, 37),
    (2019, 4, 47),
    (2021, 2, 47),
    (2022, 3, 44),
    (2023, 2, 50),
    (2024, 4, 52),
    (2025, 1, 64),
    (2026, 2, 63),
]

# Create DataFrame
df = pd.DataFrame(ioaa_data, columns=["Year", "Rank", "Total_Countries"])

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
best_2016 = df[df["Year"] == 2016].iloc[0]
best_2025 = df[df["Year"] == 2025].iloc[0]

# 1. Anchor the text at a shared coordinate so both arrows originate from the exact same spot
text_x = 2021
text_y = best_2016["Percentile"] + 1

# 2. Main Annotation (Contains the Text + Arrow pointing to 2016)
plt.annotate(
    f"🏆 Historic Peak!\nRank {int(best_2016['Rank'])} of {int(best_2016['Total_Countries'])}\n({best_2016['Percentile']:.0f}th Percentile)",
    xy=(2016, best_2016["Percentile"]),
    xytext=(text_x, text_y),
    arrowprops=dict(color="#e74c3c", arrowstyle="->", connectionstyle="arc3,rad=-0.1"),
    fontsize=11,
    fontweight="bold",
    color="#e74c3c",
    ha="center",
    fontname="Segoe UI Emoji",
)

# 3. Ghost Annotation (Empty Text + Arrow pointing to 2025)
plt.annotate(
    "",  # An empty string prevents overlapping text rendering
    xy=(2025, best_2025["Percentile"]),
    xytext=(text_x + 1, text_y),
    arrowprops=dict(
        color="#e74c3c",
        arrowstyle="->",
        connectionstyle="arc3,rad=0.1",
        # Note: Flipped the rad polarity to 0.1 so the arc bows in the opposite direction
    ),
)

# Plot customization
plt.title(
    "India's IOAA Performance Percentile (1989-2026)\nRelative Positioning to Overall Pool Size",
    fontsize=16,
    fontweight="bold",
    pad=15,
)
plt.xlabel("Year", fontsize=12, labelpad=10)
plt.ylabel("Competitive Percentile (%) — Higher is Better", fontsize=12, labelpad=10)
plt.xlim(ioaa_data[0][0] - 1, ioaa_data[-1][0] + 1)
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
