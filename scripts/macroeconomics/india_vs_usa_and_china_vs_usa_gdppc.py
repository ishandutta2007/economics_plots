import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

# ---------------------------------------------------------
# 1. Define Historical Data Points (Nominal GDP per capita in USD)
# ---------------------------------------------------------

usa_data = {
    1937: 721,
    1940: 779,
    1947: 1732,
    1950: 1977,
    1960: 3001,
    1970: 5233,
    1980: 12547,
    1990: 23835,
    2000: 36334,
    2010: 48373,
    2020: 63027,
    2023: 81695,
    2025: 92266,
}

india_data = {
    1937: 58,
    1947: 60,
    1950: 65,
    1960: 82,
    1970: 112,
    1980: 267,
    1990: 368,
    2000: 443,
    2010: 1357,
    2020: 1933,
    2023: 2612,
    2025: 2900,
}

china_data = {
    1937: 68,
    1945: 55,
    1950: 60,
    1960: 89,
    1970: 113,
    1980: 195,
    1990: 318,
    1995: 610,
    2000: 959,
    2005: 1753,
    2010: 4550,
    2015: 8065,
    2020: 10409,
    2023: 12614,
    2025: 14200,
}

# ---------------------------------------------------------
# 2. Interpolation & Calculation
# ---------------------------------------------------------
years = np.arange(1937, 2026)


def interpolate_data(data_dict, target_years):
    known_years = sorted(data_dict.keys())
    known_values = [data_dict[y] for y in known_years]
    f = interp1d(known_years, known_values, kind="linear", fill_value="extrapolate")
    return f(target_years)


usa_gdp = interpolate_data(usa_data, years)
india_gdp = interpolate_data(india_data, years)
china_gdp = interpolate_data(china_data, years)

# Calculate Ratios
ratio_india = usa_gdp / india_gdp
ratio_china = usa_gdp / china_gdp

# ---------------------------------------------------------
# 3. Plotting & Annotating
# ---------------------------------------------------------
plt.figure(figsize=(14, 8))

plt.plot(years, ratio_india, color="#e67e22", linewidth=2.5, label="USA vs. India Gap")
plt.plot(years, ratio_china, color="#c0392b", linewidth=2.5, label="USA vs. China Gap")

# CORRECTION IS HERE: Filled in the milestone years list
milestone_years = [
    1937,
    1947,
    1950,
    1960,
    1970,
    1980,
    1990,
    2000,
    2010,
    2015,
    2020,
    2025,
]

for yr in milestone_years:
    idx = yr - 1937

    # Annotate India Points (Above line)
    plt.plot(yr, ratio_india[idx], "o", color="#e67e22", markersize=5)
    plt.annotate(
        f"{yr}\n{ratio_india[idx]:.1f}x",
        (yr, ratio_india[idx]),
        xytext=(0, -25),
        textcoords="offset points",
        ha="center",
        fontsize=9,
        color="#b35c16",
        fontweight="bold",
    )

    # Annotate China Points (Below line)
    plt.plot(yr, ratio_china[idx], "o", color="#c0392b", markersize=5)
    plt.annotate(
        f"{yr}\n{ratio_china[idx]:.1f}x",
        (yr, ratio_china[idx]),
        xytext=(0, 12),
        textcoords="offset points",
        ha="center",
        fontsize=9,
        color="#962d22",
        fontweight="bold",
    )

# Highlight intersection
cross_idx = np.argwhere((ratio_china < ratio_india) & (years >= 1980))
if len(cross_idx) > 0:
    cross_yr = years[cross_idx[0]][0]
    cross_val = ratio_china[cross_idx[0]][0]
    plt.plot(cross_yr, cross_val, "ko", markersize=7)
    plt.annotate(
        f"China outpaces India's\ncatch-up rate {cross_yr}",
        (cross_yr, cross_val),
        xytext=(-70, 120),
        textcoords="offset points",
        arrowprops=dict(arrowstyle="->", color="black"),
        fontsize=10,
        fontweight="bold",
        bbox=dict(boxstyle="round,pad=0.3", fc="yellow", alpha=0.3),
    )

plt.yscale("log")
plt.title(
    "Historical Wealth Gap: USA GDP Per Capita Multiple vs. India & China (1937-2025)",
    fontsize=14,
    pad=25,
    fontweight="bold",
)
plt.ylabel("Ratio (USA GDP per capita is X times larger)", fontsize=12)
plt.xlabel("Year", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.4)
plt.legend(fontsize=12, loc="upper left")
plt.ylim(-5, 110)
plt.xlim(1932, 2030)

plt.tight_layout()
plt.show()
