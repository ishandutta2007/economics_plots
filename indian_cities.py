import matplotlib.pyplot as plt
import numpy as np

# Modelled historical GDP estimates (USD Billions)
# Note: Early years are approximations based on state-share and historical narratives.
years = [1960, 1980, 1991, 2000, 2010, 2020, 2025]

# Kolkata Metro Estimates (Proxy based on West Bengal trajectory)
kolkata_gdp = [12, 18, 25, 45, 90, 140, 150]

# Bengaluru Metro Estimates (Proxy based on Karnataka trajectory)
bengaluru_gdp = [1, 4, 10, 35, 75, 110, 133]

durgapur_gdp = [0.45, 0.88, 1.35, 2.10, 4.80, 6.15, 8.50]

plt.figure(figsize=(10, 6))
plt.plot(
    years,
    kolkata_gdp,
    marker="o",
    linestyle="-",
    color="blue",
    label="Kolkata (Est. Metro GDP)",
)
plt.plot(
    years,
    bengaluru_gdp,
    marker="s",
    linestyle="--",
    color="green",
    label="Bengaluru (Est. Metro GDP)",
)
plt.plot(
    years,
    durgapur_gdp,
    marker="x",
    linestyle="--",
    color="black",
    label="Durgapur (Est. Metro GDP)",
)

# Annotate Kolkata points
for year, gdp in zip(years, kolkata_gdp):
    plt.annotate(
        f"${gdp}B",
        xy=(year, gdp),
        xytext=(0, 8),
        textcoords="offset points",
        ha="center",
        fontsize=8,
        color="blue",
    )

# Annotate Bengaluru points
for year, gdp in zip(years, bengaluru_gdp):
    plt.annotate(
        f"${gdp}B",
        xy=(year, gdp),
        xytext=(0, -12),
        textcoords="offset points",
        ha="center",
        fontsize=8,
        color="green",
    )

# Annotate Durgapur points
for year, gdp in zip(years, durgapur_gdp):
    plt.annotate(
        f"${gdp}B",
        xy=(year, gdp),
        xytext=(0, -12),
        textcoords="offset points",
        ha="center",
        fontsize=8,
        color="black",
    )

plt.title(
    "Estimated Historical GDP Growth: Kolkata vs. Bengaluru (1960-2025)", fontsize=14
)
plt.xlabel("Year", fontsize=12)
plt.ylabel("GDP in USD Billions", fontsize=12)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend()

# Highlight the crossover period
plt.annotate(
    "IT Boom Crossover",
    xy=(2015, 115),
    xytext=(1995, 120),
    arrowprops=dict(facecolor="black", shrink=0.05),
    fontsize=10,
)

plt.show()
