import matplotlib.pyplot as plt

# Years from 2014 to 2023
years = list(range(2014, 2024))

# Estimated PM2.5 data (µg/m³) for each country
data = {
    'Bangladesh': [85, 82, 80, 78, 76, 74, 72, 70, 75, 79.9],
    'Pakistan': [80, 78, 76, 74, 72, 70, 68, 70, 72, 73.7],
    'India': [60, 58, 56, 54, 52, 50, 52, 54, 56, 58],
    'Sri Lanka': [30, 28, 26, 24, 22, 20, 22, 24, 26, 28]
}

# Plotting
plt.figure(figsize=(12, 6))
for country, pm_values in data.items():
    plt.plot(years, pm_values, marker='o', label=country)

    # Add label at the latest data point
    latest_year = years[-1]
    latest_value = pm_values[-1]
    label = f"{country} ({latest_value:.1f})"
    plt.text(latest_year + 0.2, latest_value, label, fontsize=9, va='center')

# Plot settings
plt.title('Estimated PM2.5 Levels (2014–2023)')
plt.xlabel('Year')
plt.ylabel('PM2.5 Concentration (µg/m³)')
plt.axhline(y=5, color='gray', linestyle='--', label='WHO Limit (5 µg/m³)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
