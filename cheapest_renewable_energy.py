import matplotlib.pyplot as plt

# Data
countries = [
    "India (Solar PV)",
    "China (Onshore Wind)",
    "Vietnam (Solar - Ground)",
    "Vietnam (Wind - Onshore)",
    "India (Biomass)",
    "China (Biomass)"
]
prices = [0.049, 0.033, 0.0709, 0.085, 0.060, 0.062]

# Create the plot
plt.figure(figsize=(10, 6))
bars = plt.barh(countries, prices, color='seagreen')
plt.xlabel("LCOE (USD per kWh)")
plt.title("Countries with Lowest Renewable Energy Costs (2023)")
plt.gca().invert_yaxis()  # Highest rank on top
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Annotate bars with price values
for bar in bars:
    width = bar.get_width()
    plt.text(width + 0.002, bar.get_y() + bar.get_height()/2,
             f"${width:.3f}", va='center')

plt.tight_layout()
plt.show()
