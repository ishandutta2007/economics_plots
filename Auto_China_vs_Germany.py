import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import numpy as np

# Historical and projected data points
# Data is approximate for intermediate years to show the trend
data = {
    # 'Year': [2020, 2021, 2022, 2023, 2024, 2025, 2030],
    # 'German Brands': [24.0, 21.0, 18.0, 16.0, 15.0, 13.1, 10.0],
    # 'Chinese Brands': [36.0, 41.2, 50.0, 58.0, 65.1, 69.5, 76.0]
    "Year": [2020, 2021, 2022, 2023, 2024, 2030],
    "Chinese Brands": [32, 32.5, 33, 33, 34, 45],  # Approximate share
    "German Brands": [5.1, 4.8, 4.5, 4.5, 4.4, 3],  # Approximate share
}

df = pd.DataFrame(data)

# Interpolate data for smoother curves
# Generate many more points between the min and max year for a smooth line
x_years = np.linspace(df["Year"].min(), df["Year"].max(), 300)

# Create smooth lines for German Brands
spl_german = make_interp_spline(df["Year"], df["German Brands"], k=2)
y_german_smooth = spl_german(x_years)

# Create smooth lines for Chinese Brands
spl_chinese = make_interp_spline(df["Year"], df["Chinese Brands"], k=2)
y_chinese_smooth = spl_chinese(x_years)

plt.figure(figsize=(12, 7))

# Plotting the smooth, interpolated data
plt.plot(
    x_years,
    y_german_smooth,
    label="German Brands Market Share (Interpolated)",
    color="red",
    linestyle="-",
    alpha=0.7,
)
plt.plot(
    x_years,
    y_chinese_smooth,
    label="Chinese Brands Market Share (Interpolated)",
    color="blue",
    linestyle="-",
    alpha=0.7,
)

# Plotting and annotating the original data points
plt.scatter(df["Year"], df["German Brands"], color="red", zorder=5)
for i, txt in enumerate(df["German Brands"]):
    plt.annotate(
        f"{txt}%",
        (df["Year"][i], df["German Brands"][i]),
        textcoords="offset points",
        xytext=(0, 10),
        ha="center",
        fontsize=9,
        color="red",
    )

plt.scatter(df["Year"], df["Chinese Brands"], color="blue", zorder=5)
for i, txt in enumerate(df["Chinese Brands"]):
    plt.annotate(
        f"{txt}%",
        (df["Year"][i], df["Chinese Brands"][i]),
        textcoords="offset points",
        xytext=(0, -15),
        ha="center",
        fontsize=9,
        color="blue",
    )

# Highlighting the projection line
plt.axvline(x=2030, color="gray", linestyle="--", label="Projection Year")

# Adding labels, title, and grid
plt.title("Automotive Market Share: German vs. Chinese Brands (2020-2030 Projected)")
plt.xlabel("Year")
plt.ylabel("Market Share (%)")
plt.legend()
plt.grid(True, linestyle=":", alpha=0.6)
plt.ylim(0, 50)  # Adjust Y-axis limit for better visualization
plt.xticks(data["Year"])  # Ensure only relevant years are shown on x-axis

# Display the plot
plt.show()
