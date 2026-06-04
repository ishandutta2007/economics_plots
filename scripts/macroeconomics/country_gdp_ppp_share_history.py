import matplotlib.pyplot as plt
import pandas as pd

# 1. Define the data extracted from the plot
# fmt: off
# This entire block will not be formatted by Ruff
data = {
    'Year':           [1,    1000,  1500,  1600,  1700,  1820,  1850,  1870,  1900,  1913,  1940,  1950,  1960,  1970,  1980,  1990,  2000,  2010,  2017,  2025,  2030],
    'OTHERS':         [21,   21.5,  16,    14,    14,    13,    13,    14,    25,    24,    13,    34,    34,    34,    40,    40,    40,    40.5,    39.5,     37,    37],
    'FRANCE':         [2.5,  2.5,   4,     4,     5,     5,     6,     7,     6,     6,     3,     4,     4,     4,     4.5,   4.2,   3.5,   2.8,   2.4,   2.2,   2.0],
    'UNITED KINGDOM': [1,    1.5,   2,     3,     4,     7,     9,     10,    10,    10,    9,     7,     6,     6,     4.0,   3.8,   3.3,   2.7,   2.4,   2.1,   2.0],
    'SPAIN':          [2.5,  2,     3,     3,     4,     4,     6,     5,     6,     5,     5,     2,     2,     3,     2.4,   2.3,   2.1,   1.8,   1.5,   1.4,   1.2],
    'ITALY':          [2.5,  2.5,   4,     5,     5,     5,     5,     6,     5,     5,     4,     3,     3,     3,     4.7,   4.5,   3.6,   2.6,   2.0,   1.8,   1.6],
    'GERMANY':        [1.5,  1.5,   3,     3,     4,     4,     6,     5,     7,     8,     8,     4,     5,     6,     7.0,   6.4,   5.2,   4,     3.6,   2.9,   2.6],
    'JAPAN':          [1,    1.5,   3,     4,     5,     6,     5,     2,     3,     5,     5,     3,     5.5,   6.5,   7.8,   8.8,   6.7,   4.9,   4.3,   3.2,   2.8],
    'RUSSIA':         [2.5,  2.5,   2,     2,     2,     2,     5,     6,     9,     10,    12,    13,    14,    13,    13.0,  6.9,   3.1,   3.5,   3.1,   3.4,   3.1],
    'INDIA':          [39.5, 36.5,  32,    28,    28,    18,    16,    14,    12,    10,    9,     6,     4,     3,     2.7,   3.4,   4,     5.3,   6.7,   8.5,   9.9],
    'CHINA':          [29.5, 32.5,  34,    37,    32,    40,    30,    24,    16,    12,    10,    7,     6,     4,     3.1,   5.4,   6.7,   12.7,  16.7,  19.7,  22],
    'AUSTRALIA':      [0,    0,     0,     0,     0,     0,     0.1,   0.3,   0.6,   0.6,   0.8,   0.8,   0.9,   1,     1.1,   1.1,   1.1,   1.0,   1.0,   0.95,  0.9],
    'CANADA':         [0,    0,     0,     0.1,   0.1,   0.1,   0.3,   0.9,   1.3,   1.4,   1.5,   2,     2.1,   2.2,   2.2,   2.1,   1.8,   1.5,   1.4,   1.3,   1.2],
    'UNITED STATES':  [0.5,  0.5,   1,     1,     1,     1,     4,     9,     13,    14,    19,    27,    26,    24,    21.7,  21.6,  20.4,  17,    15.7,  15.5,  14]
}
# fmt: on

# 2. Create a Pandas DataFrame
df = pd.DataFrame(data)
df = df.set_index("Year")

# 3. Define the stacking order (bottom to top) and colors
# This order must match the legend from bottom to top
columns = [
    "UNITED STATES",
    "CANADA",
    "AUSTRALIA",
    "FRANCE",
    "UNITED KINGDOM",
    "SPAIN",
    "ITALY",
    "GERMANY",
    "JAPAN",
    "RUSSIA",
    "INDIA",
    "CHINA",
    "OTHERS",
]

# Approximate colors from the chart
colors = [
    "#000080",  # US (Navy)
    "#DC143C",  # CANADA (Crimson)
    "#32CD32",  # AUSTRALIA (LimeGreen)
    "#4169E1",  # FRANCE (RoyalBlue)
    "#800080",  # UK (Purple)
    "#006400",  # SPAIN (DarkGreen)
    "#FFD700",  # ITALY (Gold)
    "#000000",  # GERMANY (Black)
    "#E67E22",  # JAPAN (Carrot)
    "#48D1CC",  # RUSSIA (MediumTurquoise)
    "#F39C12",  # INDIA (Orange)
    "#C0392B",  # CHINA (Pomegranate)
    "#F5DEB3",  # OTHERS (Wheat)
]

# 4. Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Generate the stackplot using index positions for x-axis
x_positions = range(len(df.index))
ax.stackplot(x_positions, df[columns].T, labels=columns, colors=colors, alpha=0.9)

# 5. Customize the plot to match the original
ax.set_title("Share of GDP(PPP) (WORLD POWERS)", fontsize=16, fontweight="bold")
ax.set_ylabel("Share of GDP(PPP) (%)", fontsize=12)
ax.set_xlabel("Year", fontsize=12)

# Set Y-axis limits and ticks
ax.set_ylim(0, 100)
ax.set_yticks(range(0, 101, 10))
ax.set_yticklabels([f"{y}%" for y in range(0, 101, 10)])

# Add y-axis labels on both left and right sides
ax.tick_params(axis="y", which="both", labelleft=True, labelright=True)

# Set X-axis limits and ticks to match the index positions
ax.set_xlim(0, len(df.index) - 1)
ax.set_xticks(x_positions)
ax.set_xticklabels(df.index, rotation=45, ha="right")

# Add legend to the right side of the plot
# We reverse the handles and labels to match the plot's stacking order (top to bottom)
handles, labels = ax.get_legend_handles_labels()
ax.legend(
    handles[::-1],
    labels[::-1],
    loc="center left",
    bbox_to_anchor=(1.15, 0.5),
    fontsize=11,
)

# Remove the top and right spines
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Adjust layout to prevent legend from being cut off
plt.tight_layout(rect=[0, 0, 0.85, 1])

# 6. Show the plot
plt.show()
