import matplotlib.pyplot as plt

# Data
countries = [
    "Iran", "Syria", "Cuba", "Sudan", "Ethiopia",
    "Libya", "Kyrgyzstan", "Angola", "Bhutan", "Iraq"
]
prices = [0.002, 0.003, 0.006, 0.006, 0.006, 0.008, 0.013, 0.014, 0.015, 0.015]

# Create the plot
plt.figure(figsize=(10, 6))
plt.barh(countries, prices, color='skyblue')
plt.xlabel("Electricity Price (USD per kWh)")
plt.title("Top 10 Countries with the Lowest Electricity Prices (2023)")
plt.gca().invert_yaxis()  # Highest rank on top
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Annotate bars
for i, value in enumerate(prices):
    plt.text(value + 0.0005, i, f"${value:.3f}", va='center')

plt.tight_layout()
plt.show()
