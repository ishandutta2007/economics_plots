import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# 1. Historical Dataset (World Bank High-Income GNI per Capita Thresholds)
historical_years = np.array(
    [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027]
)
historical_thresholds = np.array(
    [12055, 12375, 12535, 12695, 13205, 13845, 14005, 13935, 14375, 14375]
)

# 2. Linear Regression & Future Timeline Extension
slope, intercept, r_value, p_value, std_err = linregress(
    historical_years, historical_thresholds
)
projection_years = np.arange(2028, 2048)

all_years = np.concatenate((historical_years, projection_years))
projected_thresholds = slope * all_years + intercept

# Define the evaluation intervals explicitly to avoid list lookup compilation errors
projection_milestones = [2030, 2035, 2040, 2047]

# 3. Configure Visual Layout Styles
plt.figure(figsize=(14, 8))
plt.style.use(
    "seaborn-v0_8-whitegrid"
    if "seaborn-v0_8-whitegrid" in plt.style.available
    else "default"
)

# Plot Observed vs Projected Curves
plt.plot(
    historical_years,
    historical_thresholds,
    marker="o",
    linestyle="-",
    color="#1f77b4",
    linewidth=2.5,
    markersize=6,
    label="World Bank Historical Data",
)

plt.plot(
    all_years,
    projected_thresholds,
    linestyle="--",
    color="#ff7f0e",
    linewidth=2,
    label=f"Trend Projection to 2047 (R² = {r_value**2:.2f})",
)
plt.scatter(
    projection_years,
    slope * projection_years + intercept,
    color="#ff7f0e",
    facecolors="none",
    edgecolors="#ff7f0e",
    s=30,
)

# 4. Annotating Data Coordinates
# Historical labels (Annotate every single observation point)
for year, value in zip(historical_years, historical_thresholds):
    plt.text(
        year,
        value + 200,
        f"${value:,}",
        ha="center",
        va="bottom",
        fontsize=8,
        color="#1f77b4",
        fontweight="bold",
    )

# Projection labels (LINE 37 - Fixed syntax looking up the defined list variable)
for year, value in zip(all_years, projected_thresholds):
    if year in projection_milestones:
        plt.text(
            year,
            value - 450,
            f"${int(value):,}",
            ha="center",
            va="top",
            fontsize=8,
            color="#e36209",
            fontweight="bold",
        )

# 5. Graph Framing, Ranges and Legends
plt.axvline(x=2027, color="#7f7f7f", linestyle=":", alpha=0.8)
plt.fill_between(
    all_years,
    10000,
    22000,
    where=(all_years > 2027),
    color="#ff7f0e",
    alpha=0.04,
    label="Projection Window",
)
plt.text(
    2027.5,
    10800,
    "← Observed | Projected →",
    color="#555555",
    fontsize=10,
    fontstyle="italic",
)

plt.title(
    "World Bank High-Income Threshold: Historical & Projected Trend to 2047",
    fontsize=14,
    fontweight="bold",
    pad=20,
)
plt.xlabel("Fiscal Year (FY)", fontsize=11, labelpad=10)
plt.ylabel("GNI per Capita Threshold (USD)", fontsize=11, labelpad=10)

plt.xticks(np.arange(2018, 2049, 2), rotation=45)
plt.xlim(2017, 2048)
plt.ylim(10500, 21500)
plt.gca().get_yaxis().set_major_formatter(
    plt.FuncFormatter(lambda x, loc: f"${int(x):,}")
)
plt.legend(loc="upper left", frameon=True, facecolor="white", edgecolor="none")

plt.tight_layout()
plt.show()
