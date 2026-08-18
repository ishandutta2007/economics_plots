import matplotlib.pyplot as plt

# India GDP data: 1990–2024
years = [
    1990,
    1991,
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
]

nominal_gdp = [
    0.321,
    0.270,
    0.288,
    0.279,
    0.327,
    0.360,
    0.393,
    0.416,
    0.421,
    0.459,
    0.468,
    0.485,
    0.515,
    0.608,
    0.709,
    0.820,
    0.940,
    1.217,
    1.199,
    1.342,
    1.676,
    1.823,
    1.828,
    1.857,
    2.039,
    2.104,
    2.295,
    2.651,
    2.703,
    2.836,
    2.675,
    3.167,
    3.250,
    3.501,
    3.761,
]

ppp_gdp = [
    1.048,
    1.095,
    1.182,
    1.267,
    1.380,
    1.516,
    1.660,
    1.757,
    1.887,
    2.083,
    2.212,
    2.371,
    2.499,
    2.749,
    3.047,
    3.391,
    3.777,
    4.177,
    4.389,
    4.763,
    5.231,
    5.618,
    6.163,
    6.498,
    6.813,
    7.205,
    7.796,
    8.355,
    9.231,
    9.933,
    9.771,
    11.384,
    13.124,
    14.846,
    16.192,
]

# Calculate PPP multiple
ppp_multiple = [ppp / nominal for ppp, nominal in zip(ppp_gdp, nominal_gdp)]

# Create figure
plt.figure(figsize=(16, 9))

plt.plot(years, ppp_multiple, marker="o", linewidth=2, markersize=5)

# Annotate EVERY plotted point
for year, multiple in zip(years, ppp_multiple):
    plt.annotate(
        f"{multiple:.2f}×",
        (year, multiple),
        xytext=(0, 8),
        textcoords="offset points",
        ha="center",
        fontsize=8,
    )

# Labels and title
plt.title(
    "India's PPP GDP Multiple vs Nominal GDP (1990–2024)",
    fontsize=18,
    fontweight="bold",
)

plt.xlabel("Year", fontsize=13)
plt.ylabel("PPP GDP / Nominal GDP (×)", fontsize=13)

# Make x-axis readable
plt.xticks(years, rotation=45)

# Grid
plt.grid(True, linestyle="--", alpha=0.4)

# Add some breathing room around annotations
plt.ylim(min(ppp_multiple) - 0.15, max(ppp_multiple) + 0.25)

plt.tight_layout()

# Save high-resolution image
plt.savefig("india_ppp_multiple_1990_2024.png", dpi=300, bbox_inches="tight")

plt.show()
