import pandas as pd
import matplotlib.pyplot as plt

# --- Data Preparation ---
# Population and area data for G20 countries (most recent available).
# The European Union and African Union are excluded as they are regional bodies.
# All listed countries have populations well over 10 million.
g20_data = {
    "Country": [
        "Argentina",
        "Australia",
        "Brazil",
        "Canada",
        "China",
        "France",
        "Germany",
        "India",
        "Indonesia",
        "Italy",
        "Japan",
        "Mexico",
        "Russia",
        "Saudi Arabia",
        "South Africa",
        "South Korea",
        "Turkey",
        "United Kingdom",
        "United States",
        "Netherlands",
    ],
    "Population": [
        47070000,
        27880000,
        212000000,
        41000000,
        1425000000,
        68600000,
        84000000,
        1442000000,
        282000000,
        59000000,
        124520000,
        129740000,
        144000000,
        34570000,
        63210000,
        51710000,
        85330000,
        68000000,
        335000000,
        17900000,
    ],
    "Area_km2": [
        2780085,
        7688287,
        8515767,
        9984670,
        9388211,
        632702,
        357596,
        2973190,
        1811570,
        301340,
        377975,
        1960000,
        16376870,
        2149690,
        1220000,
        100339,
        783562,
        241930,
        9147420,
        41543,
    ],
}

df = pd.DataFrame(g20_data)

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
