import matplotlib.pyplot as plt

# Data
countries = [
    "India (Solar PV)",
    "China (Onshore Wind)",
    "Vietnam (Solar - Ground)",
    "Vietnam (Wind - Onshore)",
    "India (Biomass)",
    "China (Biomass)",
    "USA (Solar PV)",
    "USA (Onshore Wind)",
    "UK (Offshore Wind)",
    "Germany (Solar PV)",
]
prices = [0.049, 0.033, 0.0709, 0.085, 0.060, 0.062, 0.057, 0.037, 0.086, 0.077]

# Identify western countries by index for coloring
western_indices = [6, 7, 8, 9]

# Set colors: green for non-western, orange for western countries
colors = [
    "seagreen" if i not in western_indices else "orange" for i in range(len(countries))
]

# Create the plot
plt.figure(figsize=(12, 7))
bars = plt.barh(countries, prices, color=colors)
plt.xlabel("LCOE (USD per kWh)")
plt.title(
    "Renewable Energy Costs by Country (2023)\nWestern Countries Highlighted in Orange"
)
plt.gca().invert_yaxis()
plt.grid(axis="x", linestyle="--", alpha=0.7)

# Annotate bars
for bar in bars:
    width = bar.get_width()
    plt.text(
        width + 0.002, bar.get_y() + bar.get_height() / 2, f"${width:.3f}", va="center"
    )

plt.tight_layout()
plt.show()
