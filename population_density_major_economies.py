import pandas as pd
import matplotlib.pyplot as plt

# --- Data Preparation ---
# Population and area data for G20 countries (most recent available).
# The European Union and African Union are excluded as they are regional bodies.
# All listed countries have populations well over 10 million.
g20_data = [#("Country", "Population", "Area_km2")
    ("Argentina", 47070000, 2780085),
    ("Australia", 27880000, 7688287),
    ("Brazil", 212000000, 8515767),
    ("Canada", 41000000, 9984670),
    ("China", 1425000000, 9388211),
    ("France", 68600000, 632702),
    ("Germany", 84000000, 357596),
    ("India", 1442000000, 3287263),
    ("Indonesia", 282000000, 1811570),
    ("Italy", 59000000, 301340),
    ("Japan", 124520000, 377975),
    ("Mexico", 129740000, 1960000),
    ("Russia", 144000000, 16376870),
    ("Saudi Arabia", 34570000, 2149690),
    ("South Africa", 63210000, 1220000),
    ("South Korea", 51710000, 100210),
    ("Turkey", 85330000, 783562),
    ("United Kingdom", 68000000, 241930),
    ("United States", 335000000, 9147420),
    ("Netherlands", 17900000, 41543),
]

df = pd.DataFrame(g20_data, columns=["Country", "Population", "Area_km2"])

# Calculate Population Density
df["Density"] = df["Population"] / df["Area_km2"]

# Sort the dataframe by density for a cleaner plot
df_sorted = df.sort_values("Density", ascending=True)


# --- Plotting ---
# Create the figure and axes objects
fig, ax = plt.subplots(figsize=(14, 10))

# Create horizontal bars
bars = ax.barh(
    df_sorted["Country"],
    df_sorted["Density"],
    color=plt.cm.viridis(
        df_sorted["Density"] / max(df_sorted["Density"])
    ),  # Color gradient
)

# --- Formatting and Styling ---
# Set the title and labels
ax.set_title(
    "Population Density of G20 Countries (>10M Population)", fontsize=18, pad=-10
)
ax.set_xlabel("Population Density (People per km²)", fontsize=12)
ax.set_ylabel("")  # No label for y-axis as country names are the labels

# Remove the top and right spines for a modern look
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Add data labels at the end of each bar for clarity
for bar in bars:
    width = bar.get_width()
    label_x_pos = width + 5  # Position label slightly after the bar
    ax.text(
        label_x_pos,
        bar.get_y() + bar.get_height() / 2,
        f"{width:,.1f}",
        va="center",
        ha="left",
        fontsize=9,
        color="black",
    )

# Add a footnote for the data source
footnote_text = "Source: Most recent population and area data from various official and public sources (e.g., World Bank, national statistics offices)."
fig.text(
    0.5, 0.01, footnote_text, ha="center", fontsize=9, style="italic", color="gray"
)


# Adjust layout to make sure everything fits nicely
plt.tight_layout()
plt.subplots_adjust(left=0.2, bottom=0.1)

# Show the plot
plt.show()
