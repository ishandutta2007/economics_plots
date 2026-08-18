import matplotlib.pyplot as plt

# ============================================================
# India and China GDP data: 1990–2024
# GDP values are in trillion current US$ / international $
# ============================================================

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

# ------------------------------------------------------------
# INDIA
# ------------------------------------------------------------

india_nominal = [
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

india_ppp = [
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

# ------------------------------------------------------------
# CHINA
# ------------------------------------------------------------

china_nominal = [
    0.360,
    0.383,
    0.493,
    0.617,
    0.564,
    0.734,
    0.864,
    0.958,
    1.025,
    1.090,
    1.211,
    1.339,
    1.471,
    1.660,
    1.955,
    2.304,
    2.752,
    3.550,
    4.594,
    5.101,
    6.087,
    7.552,
    8.532,
    9.570,
    10.476,
    11.062,
    11.233,
    12.310,
    13.895,
    14.280,
    14.687,
    17.821,
    17.963,
    17.794,
    18.744,
]

china_ppp = [
    1.605,
    1.760,
    1.962,
    2.186,
    2.427,
    2.687,
    2.987,
    3.309,
    3.670,
    4.090,
    4.501,
    4.967,
    5.461,
    6.060,
    6.747,
    7.434,
    8.320,
    9.333,
    10.308,
    11.145,
    12.548,
    14.175,
    15.532,
    16.988,
    18.131,
    19.292,
    20.815,
    22.348,
    24.651,
    25.935,
    27.101,
    29.677,
    31.584,
    33.830,
    38.190,
]

# ============================================================
# Calculate PPP multiples
# ============================================================

india_multiple = [ppp / nominal for ppp, nominal in zip(india_ppp, india_nominal)]

china_multiple = [ppp / nominal for ppp, nominal in zip(china_ppp, china_nominal)]

# ============================================================
# Plot
# ============================================================

plt.figure(figsize=(18, 10))

plt.plot(years, india_multiple, marker="o", linewidth=2, markersize=5, label="India")

plt.plot(years, china_multiple, marker="o", linewidth=2, markersize=5, label="China")

# ============================================================
# Annotate EVERY point
# ============================================================

for year, value in zip(years, india_multiple):
    plt.annotate(
        f"{value:.2f}×",
        (year, value),
        xytext=(0, 9),
        textcoords="offset points",
        ha="center",
        fontsize=7,
    )

for year, value in zip(years, china_multiple):
    plt.annotate(
        f"{value:.2f}×",
        (year, value),
        xytext=(0, -14),
        textcoords="offset points",
        ha="center",
        fontsize=7,
    )

# ============================================================
# Formatting
# ============================================================

plt.title(
    "PPP GDP / Nominal GDP Multiple: India vs China (1990–2024)",
    fontsize=18,
    fontweight="bold",
)

plt.xlabel("Year", fontsize=13)

plt.ylabel("PPP GDP / Nominal GDP (×)", fontsize=13)

plt.xticks(years, rotation=45)

plt.grid(True, linestyle="--", alpha=0.4)

plt.legend(fontsize=12, loc="best")

plt.tight_layout()

# Save high-resolution image
# plt.savefig(
#     "india_china_ppp_multiple_1990_2024.png",
#     dpi=300,
#     bbox_inches="tight"
# )

plt.show()
