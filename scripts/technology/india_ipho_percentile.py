import matplotlib.pyplot as plt
import pandas as pd

# Historical IPhO Data for India (1998 - 2026)
# Format: (Year, India's Unofficial Rank, Total Participating Countries)
# Note: 2020 is omitted as the competition was cancelled due to the pandemic.
ipho_data = [
    (1998, 15, 56),
    (1999, 20, 62),
    (2000, 14, 63),
    (2001, 11, 65),
    (2002, 8, 66),
    (2003, 7, 54),
    (2004, 16, 71),
    (2005, 11, 73),
    (2006, 14, 86),
    (2007, 10, 69),
    (2008, 6, 82),
    (2009, 4, 68),
    (2010, 9, 79),
    (2011, 6, 84),
    (2012, 16, 81),
    (2013, 8, 83),
    (2014, 8, 85),
    (2015, 11, 82),
    (2016, 8, 84),
    (2017, 5, 88),
    (2018, 1, 86),
    (2019, 7, 78),
    (2021, 5, 76),
    (2022, 6, 75),
    (2023, 5, 80),
    (2024, 4, 43),
    (2025, 5, 87),
    (2026, 1, 87),
]

# Create DataFrame
df = pd.DataFrame(ipho_data, columns=["Year", "Rank", "Total_Countries"])

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

# Specifically label the all-time high water mark (2018)
# Assuming you have isolated the 2018 and 2026 data points
best_2018 = df[df["Year"] == 2018].iloc[0]
best_2026 = df[df["Year"] == 2026].iloc[0]

# 1. Anchor the text at a shared coordinate so both arrows originate from the exact same spot
text_x = 2022
text_y = best_2018["Percentile"] + 2

# 2. Main Annotation (Contains the Text + Arrow pointing to 2018)
plt.annotate(
    f"🏆 Historic Peak!\nRank {int(best_2018['Rank'])} of {int(best_2018['Total_Countries'])}\n({best_2018['Percentile']:.0f}th Percentile)",
    xy=(2018, best_2018["Percentile"]),
    xytext=(text_x, text_y),
    arrowprops=dict(color="#e74c3c", arrowstyle="->", connectionstyle="arc3,rad=-0.1"),
    fontsize=11,
    fontweight="bold",
    color="#e74c3c",
    ha="center",
    fontname="Segoe UI Emoji",
)

# 3. Ghost Annotation (Empty Text + Arrow pointing to 2026)
plt.annotate(
    "",  # An empty string prevents overlapping text rendering
    xy=(2026, best_2026["Percentile"]),
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
    "India's IPhO Performance Percentile (1998-2026)\nRelative Positioning to Overall Pool Size",
    fontsize=16,
    fontweight="bold",
    pad=15,
)
plt.xlabel("Year", fontsize=12, labelpad=10)
plt.ylabel("Competitive Percentile (%) — Higher is Better", fontsize=12, labelpad=10)
plt.xlim(ipho_data[0][0] - 1, ipho_data[-1][0] + 1)
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
