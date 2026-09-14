import matplotlib.pyplot as plt

# 1. Define the Data (Estimated GDP per capita in USD)
# G7 Countries Data
g7_data = {
    "United States": 85000,
    "Canada": 54000,
    "Germany": 53000,
    "United Kingdom": 50000,
    "France": 47000,
    "Italy": 39000,
    "Japan": 35000,
}

# BRICS Countries Data (including recent expanded members)
brics_data = {
    "UAE": 53000,
    "Saudi Arabia": 33000,
    "Russia": 14000,
    "China": 13500,
    "Brazil": 10500,
    "South Africa": 6000,
    "Indonesia": 5500,
    "Egypt": 3800,
    "Iran": 3500,
    "India": 2700,
    "Ethiopia": 1100,
}

# Sort the data from highest to lowest so the bars look clean
g7_sorted = dict(sorted(g7_data.items(), key=lambda item: item[1]))
brics_sorted = dict(sorted(brics_data.items(), key=lambda item: item[1]))

# 2. Setup the Subplots
# We're creating two separate side-by-side axes in one clean layout
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7), sharex=False)
fig.suptitle(
    "GDP Per Capita Comparison: G7 vs BRICS (USD)",
    fontsize=16,
    fontweight="bold",
    y=0.98,
)

# 3. Plot G7 Countries (Left Plot)
g7_color = "#1f77b4"  # Deep Blue
ax1.barh(
    list(g7_sorted.keys()),
    list(g7_sorted.values()),
    color=g7_color,
    edgecolor="black",
    height=0.6,
)
ax1.set_title("G7 Countries", fontsize=13, fontweight="bold", pad=15)
ax1.set_xlabel("GDP per Capita (USD)", fontsize=11)
ax1.grid(axis="x", linestyle="--", alpha=0.5)

# Add values on top of the bars for clarity
for index, value in enumerate(g7_sorted.values()):
    ax1.text(
        value + 1000,
        index,
        f"${value:,}",
        va="center",
        fontsize=10,
        fontweight="semibold",
    )

# 4. Plot BRICS Countries (Right Plot)
brics_color = "#d62728"  # Crimson Red
ax2.barh(
    list(brics_sorted.keys()),
    list(brics_sorted.values()),
    color=brics_color,
    edgecolor="black",
    height=0.6,
)
ax2.set_title("BRICS Countries", fontsize=13, fontweight="bold", pad=15)
ax2.set_xlabel("GDP per Capita (USD)", fontsize=11)
ax2.grid(axis="x", linestyle="--", alpha=0.5)

# Add values on top of the bars for clarity
for index, value in enumerate(brics_sorted.values()):
    ax2.text(
        value + 500,
        index,
        f"${value:,}",
        va="center",
        fontsize=10,
        fontweight="semibold",
    )

# 5. Clean up layout aesthetics
plt.tight_layout()

# Show the chart
plt.show()
