import matplotlib.pyplot as plt
import pandas as pd

# 1. Define the data extracted from the plot
# fmt: off
# This entire block will not be formatted by Ruff
data = {
    'Year':           [1,   1000, 1500, 1600, 1700, 1820, 1850, 1870, 1900, 1913, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2017],
    'OTHERS':         [12,  12,   11,   9,    9,    8,    7,    5,    4,    4,    2,    2,    3,    4,    5,    5,    5,    5,    6],
    'FRANCE':         [3,   3,    4,    4,    5,    5,    6,    7,    6,    5,    3,    5,    4,    4,    3,    3,    3,    3,    2],
    'UNITED KINGDOM': [1,   2,    2,    3,    4,    6,    9,   12,   11,   10,   7,    6,    5,    4,    3,    2,    2,    2,    2],
    'SPAIN':          [3,   2,    3,    3,    4,    4,    6,    6,    6,    4,    1,    1,    1,    1,    1,    1,    1,    1,    1],
    'ITALY':          [4,   4,    5,    6,    6,    6,    6,    6,    6,    4,    3,    2,    2,    2,    2,    2,    2,    1,    1],
    'GERMANY':        [2,   2,    3,    3,    4,    4,    7,    7,    8,    10,   8,    4,    4,    4,    4,    4,    4,    3,    3],
    'RUSSIA':         [3,   3,    2,    2,    2,    2,    5,    7,    9,    10,    7,    4,    4,    4,    4,    4,    3,    3,    3],
    'JAPAN':          [1,   2,    3,    4,    5,    6,    5,    2,    3,    4,    5,    3,    4,    6,    7,    8,    8,    7,    6],
    'INDIA':          [40,  37,   32,   28,   28,   18,   16,   16,   14,   12,   12,   7,    6,    6,    5,    6,    6,    7,    8],
    'CHINA':          [30,  33,   34,   37,   32,   40,   30,   24,   16,   15,   14,   8,    8,    7,    7,    7,    11,  17,    18],
    'UNITED STATES':  [1,   1,    1,    1,    1,    1,    4,    9,    18,   23,   28,   40,   39,   36,   35,   33,   31,   25,   22]
}
# fmt: on

# 2. Create a Pandas DataFrame
df = pd.DataFrame(data)
df = df.set_index("Year")

# 3. Define the stacking order (bottom to top) and colors
# This order must match the legend from bottom to top
columns = [
    "UNITED STATES",
    "FRANCE",
    "UNITED KINGDOM",
    "SPAIN",
    "ITALY",
    "GERMANY",
    "RUSSIA",
    "JAPAN",
    "INDIA",
    "CHINA",
    "OTHERS",
]

# Approximate colors from the chart
colors = [
    "#000080",  # US (Navy)
    "#4169E1",  # FRANCE (RoyalBlue)
    "#800080",  # UK (Purple)
    "#006400",  # SPAIN (DarkGreen)
    "#FFD700",  # ITALY (Gold)
    "#000000",  # GERMANY (Black)
    "#48D1CC",  # RUSSIA (MediumTurquoise)
    "#E67E22",  # JAPAN (Carrot)
    "#F39C12",  # INDIA (Orange)
    "#C0392B",  # CHINA (Pomegranate)
    "#F5DEB3",  # ANCIENT (Wheat)
]

# 4. Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Generate the stackplot using index positions for x-axis
x_positions = range(len(df.index))
ax.stackplot(x_positions, df[columns].T, labels=columns, colors=colors, alpha=0.9)

# 5. Customize the plot to match the original
ax.set_title("Share of GDP (WORLD POWERS)", fontsize=16, fontweight="bold")
ax.set_ylabel("Share of GDP (%)", fontsize=12)
ax.set_xlabel("Year", fontsize=12)

# Set Y-axis limits and ticks
ax.set_ylim(0, 100)
ax.set_yticks(range(0, 101, 10))
ax.set_yticklabels([f"{y}%" for y in range(0, 101, 10)])

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
    bbox_to_anchor=(1.0, 0.5),
    fontsize=11,
)

# Remove the top and right spines
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Adjust layout to prevent legend from being cut off
plt.tight_layout(rect=[0, 0, 0.85, 1])

# 6. Show the plot
plt.show()
