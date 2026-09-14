import matplotlib.pyplot as plt
import numpy as np

# 1. Prepare the historical IMF growth premium data (EM growth minus DM growth)
years = np.array(
    [
        1992,
        1993,
        1994,
        1995,
        1996,
        1997,
        1998,
        1999,
        2000,
        2001,
        2002,
        2003,
        2004,
        2005,
        2006,
        2007,
        2008,
        2009,
        2010,
        2011,
        2012,
        2013,
        2014,
        2015,
        2016,
        2017,
        2018,
        2019,
        2020,
        2021,
        2022,
        2023,
        2024,
        2025,
        2026,
    ]
)

premium = np.array(
    [
        1.5,
        3.2,
        1.5,
        1.5,
        1.9,
        1.4,
        0.0,
        -0.1,
        1.9,
        2.7,
        3.2,
        4.1,
        4.3,
        4.4,
        5.1,
        5.9,
        5.6,
        6.2,
        4.3,
        4.6,
        4.2,
        3.7,
        2.6,
        1.9,
        2.7,
        2.3,
        2.3,
        1.9,
        2.4,
        1.3,
        1.5,
        2.8,
        2.5,
        2.5,
        2.1,
    ]
)

# 2. Initialize the plot layout
plt.figure(figsize=(16, 9))
plt.plot(
    years,
    premium,
    marker="o",
    color="#3b82f6",
    linewidth=2,
    label="Annual Growth Premium (EM - DM)",
    alpha=0.8,
)

# 3. Generate a smooth long-term trend curve using a 3rd-degree polynomial fit
polynomial_coefficients = np.polyfit(years, premium, 3)
trend_function = np.poly1d(polynomial_coefficients)

# Create a denser set of X-values for a perfectly smooth trend line
smooth_years = np.linspace(years.min(), years.max(), 300)
plt.plot(
    smooth_years,
    trend_function(smooth_years),
    color="#ef4444",
    linestyle="--",
    linewidth=2.5,
    label="Long-term Smoothed Trend",
)

# 4. Annotate every single data point with its percentage value
for i, val in enumerate(premium):
    # Dynamically shift labels slightly to prevent overlap during crisis years
    y_offset = 12 if val >= 0 else -18
    text_color = "#1e3a8a" if val >= 0 else "#991b1b"

    plt.annotate(
        f"{val:+.1f}%",
        (years[i], premium[i]),
        textcoords="offset points",
        xytext=(0, y_offset),
        ha="center",
        fontsize=8.5,
        weight="bold",
        color=text_color,
    )

# 5. Visual styling and labels
plt.title(
    "Emerging Markets vs Developed Markets Real GDP Growth Premium (1992–2026)",
    fontsize=14,
    weight="bold",
    pad=20,
)
plt.xlabel("Year", fontsize=11, labelpad=10)
plt.ylabel("Growth Rate Difference (Percentage Points)", fontsize=11, labelpad=10)

plt.xticks(years, rotation=45)
plt.ylim(minimum := premium.min() - 1, maximum := premium.max() + 1)
plt.grid(True, linestyle=":", alpha=0.5)
plt.axhline(
    0, color="black", linewidth=0.8, linestyle="-", alpha=0.5
)  # Zero line reference
plt.legend(loc="upper right", fontsize=11, frameon=True, shadow=True)

# 6. Show and save the visualization
plt.tight_layout()
plt.show()
