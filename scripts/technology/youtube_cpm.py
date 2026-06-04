import matplotlib.pyplot as plt
import numpy as np

# GDP per capita data (Nominal - in US$)
years_gdp = [
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
]
gdp_per_capita = [
    47043.0,
    47081.0,
    46040.0,
    48442.0,
    50103.0,
    51603.0,
    53101.0,
    55052.0,
    56803.0,
    57904.0,
    59598.0,
    61797.0,
    63540.0,
    63578.0,
    70248.0,
    76394.0,
    80034.0,
    84590,
    89105,
]

# YouTube CPM data (Interpolated)
years_cpm = list(range(2013, 2026))
cpm_2013 = 7.60
cpm_2025 = 15.34
cpm_values = np.interp(years_cpm, [2013, 2025], [cpm_2013, cpm_2025])

# Creating the plot with two y-axes
fig, ax1 = plt.subplots(figsize=(14, 7))

color = "tab:red"
ax1.set_xlabel("Year")
ax1.set_ylabel("GDP Per Capita (US$)", color=color)
ax1.plot(
    years_gdp,
    gdp_per_capita,
    marker="o",
    linestyle="-",
    color=color,
    label="GDP Per Capita",
)
ax1.tick_params(axis="y", labelcolor=color)
ax1.grid(True)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = "tab:blue"
ax2.set_ylabel("Estimated YouTube CPM (US$)", color=color)
ax2.plot(
    years_cpm,
    cpm_values,
    marker="x",
    linestyle="--",
    color=color,
    label="Estimated YouTube CPM",
)
ax2.tick_params(axis="y", labelcolor=color)

plt.title("US GDP Per Capita vs. Estimated Average YouTube CPM (2007-2025)")
fig.tight_layout()

# Combine legends from both axes
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc="upper left")

plt.xticks(list(range(min(years_gdp), max(years_gdp) + 1)))
plt.show()
