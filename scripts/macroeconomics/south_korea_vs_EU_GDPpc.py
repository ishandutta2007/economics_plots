import matplotlib.pyplot as plt
import numpy as np

# 1. Historical data setup (1980 to 2023)
years = np.array([1980, 1990, 2000, 2010, 2020, 2023])
sk_gdp = np.array([1746, 6813, 12710, 24071, 33646, 35674])
eu_gdp = np.array([9300, 15853, 16976, 33120, 34695, 41567])

# 2. Future projections setup (connecting 2023 data to 2026 estimates)
years_proj = np.array([2023, 2026])
sk_proj = np.array([35674, 37500])
eu_proj = np.array([41567, 47000])

# Initialize plot figure size
plt.figure(figsize=(12, 7))

# 3. Plot historical curves (solid lines)
plt.plot(
    years,
    sk_gdp,
    marker="o",
    linewidth=2,
    label="South Korea (Historical)",
    color="#1f77b4",
)
plt.plot(
    years,
    eu_gdp,
    marker="s",
    linewidth=2,
    label="European Union (Historical)",
    color="#ff7f0e",
)

# 4. Plot future projections (dashed lines with slight transparency)
plt.plot(
    years_proj,
    sk_proj,
    linestyle="--",
    marker="o",
    linewidth=2,
    color="#1f77b4",
    alpha=0.6,
    label="South Korea (Projected)",
)
plt.plot(
    years_proj,
    eu_proj,
    linestyle="--",
    marker="s",
    linewidth=2,
    color="#ff7f0e",
    alpha=0.6,
    label="European Union (Projected)",
)

# 5. Annotate historical data points with alternating vertical offsets to avoid overlapping
for y, sk, eu in zip(years, sk_gdp, eu_gdp):
    plt.annotate(
        f"${sk:,}",
        (y, sk),
        textcoords="offset points",
        xytext=(0, 10),
        ha="center",
        fontsize=9,
        color="#1f77b4",
        weight="bold",
    )
    plt.annotate(
        f"${eu:,}",
        (y, eu),
        textcoords="offset points",
        xytext=(0, -18),
        ha="center",
        fontsize=9,
        color="#ff7f0e",
        weight="bold",
    )

# 6. Annotate future 2026 projections (Fixed syntax: removed comma inside the expression)
plt.annotate(
    f"${37500:,}",
    (2026, 37500),
    textcoords="offset points",
    xytext=(0, 10),
    ha="center",
    fontsize=9,
    color="#1f77b4",
    weight="bold",
)
plt.annotate(
    f"${47000:,}",
    (2026, 47000),
    textcoords="offset points",
    xytext=(0, -18),
    ha="center",
    fontsize=9,
    color="#ff7f0e",
    weight="bold",
)

# Customize chart design details
plt.title(
    "GDP per Capita Convergence: South Korea vs. European Union (1980 - 2026)",
    fontsize=14,
    pad=15,
    weight="bold",
)
plt.xlabel("Year", fontsize=11, labelpad=10)
plt.ylabel("Nominal GDP per Capita (USD)", fontsize=11, labelpad=10)
plt.grid(True, linestyle=":", alpha=0.5, color="gray")
plt.gca().yaxis.set_major_formatter(
    plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x)))
)
plt.xlim(1975, 2030)  # Add padding to the x-axis to cleanly display tags
plt.ylim(0, 55000)
plt.legend(loc="upper left", frameon=True, facecolor="white", edgecolor="none")

plt.tight_layout()
plt.show()
