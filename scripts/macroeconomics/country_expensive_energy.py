import matplotlib.pyplot as plt

# Data: Residential electricity prices in USD per kWh
countries = [
    "Ireland",
    "Italy",
    "Bahamas",
    "Liechtenstein",
    "United Kingdom",
    "Belgium",
    "Bermuda",
    "Germany",
    "Cayman Islands",
    "Latvia",
    "USA",
    "Canada",
    "Australia",
    "France",
    "China",
    "India",
    "Japan",
]
prices = [
    0.537,
    0.461,
    0.453,
    0.450,
    0.445,
    0.434,
    0.421,
    0.402,
    0.401,
    0.368,
    0.172,
    0.132,
    0.280,
    0.281,
    0.076,
    0.078,
    0.221,
]

# Sort the data by price in descending order
sorted_data = sorted(zip(prices, countries), reverse=True)
sorted_prices, sorted_countries = zip(*sorted_data)

# Create the plot
plt.figure(figsize=(12, 8))
bars = plt.barh(sorted_countries, sorted_prices, color="salmon")
plt.xlabel("Electricity Price (USD per kWh)")
plt.title("Residential Electricity Prices by Country (2023)")
plt.gca().invert_yaxis()  # Highest price on top
plt.grid(axis="x", linestyle="--", alpha=0.7)

# Annotate bars with price values
for bar in bars:
    width = bar.get_width()
    plt.text(
        width + 0.005, bar.get_y() + bar.get_height() / 2, f"${width:.3f}", va="center"
    )

plt.tight_layout()
plt.show()
