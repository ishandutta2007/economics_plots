import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# 1. Complete, Explicit Historical Dataset (FY 1990 - FY 2026)
# Sources & Methodology:
# - "india_gdp_pc": India's nominal GDP per capita in USD (Source: World Bank WDI & IMF World Economic Outlook)
# - "tcs_fresher_inr_lpa": Baseline CTC for TCS entry-level tech hires in LPA (Assistant System Engineer-Trainee / "Ninja" track; official CTC from 2018-2026 is ₹3,36,877)
# - "usd_inr_rate": Annual average USD/INR exchange rate (Source: RBI Handbook of Statistics on the Indian Economy)
data = [
    # {
    #     "year": 1990,
    #     "india_gdp_pc": 371,
    #     "tcs_fresher_inr_lpa": 0.45,
    #     "usd_inr_rate": 17.5,
    # },
    # {
    #     "year": 1991,
    #     "india_gdp_pc": 309,
    #     "tcs_fresher_inr_lpa": 0.50,
    #     "usd_inr_rate": 22.7,
    # },
    # {
    #     "year": 1992,
    #     "india_gdp_pc": 314,
    #     "tcs_fresher_inr_lpa": 0.72,
    #     "usd_inr_rate": 25.9,
    # },
    # {
    #     "year": 1993,
    #     "india_gdp_pc": 302,
    #     "tcs_fresher_inr_lpa": 0.96,
    #     "usd_inr_rate": 30.5,
    # },
    # {
    #     "year": 1994,
    #     "india_gdp_pc": 346,
    #     "tcs_fresher_inr_lpa": 1.20,
    #     "usd_inr_rate": 31.4,
    # },
    # {
    #     "year": 1995,
    #     "india_gdp_pc": 374,
    #     "tcs_fresher_inr_lpa": 1.44,
    #     "usd_inr_rate": 32.4,
    # },
    {
        "year": 1996,
        "india_gdp_pc": 400,
        "tcs_fresher_inr_lpa": 1.60,
        "usd_inr_rate": 35.4,
    },
    {
        "year": 1997,
        "india_gdp_pc": 415,
        "tcs_fresher_inr_lpa": 1.80,
        "usd_inr_rate": 36.3,
    },
    {
        "year": 1998,
        "india_gdp_pc": 413,
        "tcs_fresher_inr_lpa": 1.80,
        "usd_inr_rate": 37.2,
    },
    {
        "year": 1999,
        "india_gdp_pc": 442,
        "tcs_fresher_inr_lpa": 1.85,
        "usd_inr_rate": 42.0,
    },
    {
        "year": 2000,
        "india_gdp_pc": 443,
        "tcs_fresher_inr_lpa": 1.85,
        "usd_inr_rate": 43.3,
    },
    {
        "year": 2001,
        "india_gdp_pc": 452,
        "tcs_fresher_inr_lpa": 1.85,
        "usd_inr_rate": 45.7,
    },
    {
        "year": 2002,
        "india_gdp_pc": 471,
        "tcs_fresher_inr_lpa": 2.00,
        "usd_inr_rate": 47.7,
    },
    {
        "year": 2003,
        "india_gdp_pc": 546,
        "tcs_fresher_inr_lpa": 2.10,
        "usd_inr_rate": 48.4,
    },
    {
        "year": 2004,
        "india_gdp_pc": 628,
        "tcs_fresher_inr_lpa": 2.15,
        "usd_inr_rate": 45.9,
    },
    {
        "year": 2005,
        "india_gdp_pc": 714,
        "tcs_fresher_inr_lpa": 2.25,
        "usd_inr_rate": 44.9,
    },
    {
        "year": 2006,
        "india_gdp_pc": 807,
        "tcs_fresher_inr_lpa": 2.40,
        "usd_inr_rate": 44.3,
    },
    {
        "year": 2007,
        "india_gdp_pc": 1028,
        "tcs_fresher_inr_lpa": 3.15,
        "usd_inr_rate": 41.3,
    },
    {
        "year": 2008,
        "india_gdp_pc": 999,
        "tcs_fresher_inr_lpa": 3.15,
        "usd_inr_rate": 40.2,
    },
    {
        "year": 2009,
        "india_gdp_pc": 1101,
        "tcs_fresher_inr_lpa": 3.15,
        "usd_inr_rate": 46.0,
    },
    {
        "year": 2010,
        "india_gdp_pc": 1348,
        "tcs_fresher_inr_lpa": 3.16,
        "usd_inr_rate": 47.4,
    },
    {
        "year": 2011,
        "india_gdp_pc": 1445,
        "tcs_fresher_inr_lpa": 3.16,
        "usd_inr_rate": 45.6,
    },
    {
        "year": 2012,
        "india_gdp_pc": 1429,
        "tcs_fresher_inr_lpa": 3.18,
        "usd_inr_rate": 51.2,
    },
    {
        "year": 2013,
        "india_gdp_pc": 1433,
        "tcs_fresher_inr_lpa": 3.18,
        "usd_inr_rate": 54.4,
    },
    {
        "year": 2014,
        "india_gdp_pc": 1554,
        "tcs_fresher_inr_lpa": 3.18,
        "usd_inr_rate": 60.5,
    },
    {
        "year": 2015,
        "india_gdp_pc": 1584,
        "tcs_fresher_inr_lpa": 3.25,
        "usd_inr_rate": 61.1,
    },
    {
        "year": 2016,
        "india_gdp_pc": 1708,
        "tcs_fresher_inr_lpa": 3.30,
        "usd_inr_rate": 65.5,
    },
    {
        "year": 2017,
        "india_gdp_pc": 1950,
        "tcs_fresher_inr_lpa": 3.33,
        "usd_inr_rate": 67.1,
    },
    {
        "year": 2018,
        "india_gdp_pc": 1966,
        "tcs_fresher_inr_lpa": 3.37,
        "usd_inr_rate": 64.5,
    },
    {
        "year": 2019,
        "india_gdp_pc": 2041,
        "tcs_fresher_inr_lpa": 3.37,
        "usd_inr_rate": 69.9,
    },
    {
        "year": 2020,
        "india_gdp_pc": 1907,
        "tcs_fresher_inr_lpa": 3.37,
        "usd_inr_rate": 70.9,
    },
    {
        "year": 2021,
        "india_gdp_pc": 2238,
        "tcs_fresher_inr_lpa": 3.37,
        "usd_inr_rate": 74.2,
    },
    {
        "year": 2022,
        "india_gdp_pc": 2427,
        "tcs_fresher_inr_lpa": 3.37,
        "usd_inr_rate": 74.5,
    },
    {
        "year": 2023,
        "india_gdp_pc": 2500,
        "tcs_fresher_inr_lpa": 3.37,
        "usd_inr_rate": 78.6,
    },
    {
        "year": 2024,
        "india_gdp_pc": 2600,
        "tcs_fresher_inr_lpa": 3.37,
        "usd_inr_rate": 82.8,
    },
    {
        "year": 2025,
        "india_gdp_pc": 2675,
        "tcs_fresher_inr_lpa": 3.37,
        "usd_inr_rate": 87.2,
    },
    {
        "year": 2026,
        "india_gdp_pc": 2813,
        "tcs_fresher_inr_lpa": 3.37,
        "usd_inr_rate": 95.8,
    },
]

# 2. Extract arrays and compute metrics mathematically
years = [d["year"] for d in data]
india_gdp_pc = [d["india_gdp_pc"] for d in data]

# Dynamic conversion to USD: (LPA * 100,000) / Exchange Rate
tcs_starting_salary_usd = [
    (d["tcs_fresher_inr_lpa"] * 100_000) / d["usd_inr_rate"] for d in data
]

# 3. Canvas Initialization
fig, ax = plt.subplots(figsize=(16, 11))
ax.set_yscale("log")  # Map to a single Base-10 Log Axis

color_tcs = "#1f77b4"
color_india = "#e65c00"
color_salary = "#2ca02c"
color_ias = "#9467bd"

# Plot the 2 curves together
ax.plot(
    years,
    tcs_starting_salary_usd,
    marker="^",
    linestyle="-.",
    color=color_salary,
    linewidth=2,
    label="TCS Fresher Starting Salary",
)
ax.plot(
    years,
    india_gdp_pc,
    marker="s",
    linestyle="--",
    color=color_india,
    linewidth=2,
    label="India GDP per Capita",
)

# 4. Axis Labels and Formatting
ax.set_xlabel("Fiscal Year (FY)", fontsize=12, labelpad=10)
ax.set_ylabel("Value in USD (Log Scale)", fontsize=12)
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)
ax.get_yaxis().set_major_formatter(ScalarFormatter())

start_year = data[0]["year"]
end_year = data[-1]["year"]

ax.grid(True, which="both", linestyle="--", alpha=0.3)
plt.title(
    f"TCS Salaries vs India GDP per Capita (Log Scale: {start_year} - {end_year})",
    fontsize=14,
    fontweight="bold",
    pad=25,
)

# 5. Annotate every single coordinate point
for i, (year, gdp, sal, d) in enumerate(
    zip(
        years,
        india_gdp_pc,
        tcs_starting_salary_usd,
        data,
    )
):
    sal_inr = d["tcs_fresher_inr_lpa"]
    # TCS Fresher starting salary labels
    tcs_sal_offset = 0.92 if i % 2 == 1 else 1.08
    ax.text(
        year,
        sal * tcs_sal_offset,
        f"${sal:,.0f}\n(₹{sal_inr:.2f}L)",
        ha="center",
        va="bottom",
        fontsize=7.5,
        fontweight="bold",
        color="#145214",
    )

    # India GDP labels
    gdp_offset = 1.08 if i % 2 == 1 else 0.88
    ax.text(
        year,
        gdp * gdp_offset,
        f"${gdp:,.0f}",
        ha="center",
        va="bottom",
        fontsize=7.5,
        fontweight="bold",
        color="#803300",
    )

# 7. Arrow between salary and GDP per capita
ratio_withpc_start = tcs_starting_salary_usd[0] / india_gdp_pc[0]
ratio_withpc_end = tcs_starting_salary_usd[-1] / india_gdp_pc[-1]
# First Year Ratio Gap Arrow
ax.annotate(
    "",
    xy=(start_year, tcs_starting_salary_usd[0]),
    xytext=(start_year, india_gdp_pc[0]),
    arrowprops=dict(arrowstyle="<->", linestyle=":", color="#333333", linewidth=2),
)
ax.text(
    start_year + 0.3,
    (tcs_starting_salary_usd[0] * india_gdp_pc[0]) ** 0.5,
    f"Salary Gap:\n{ratio_withpc_start:.1f}x Salary",
    va="center",
    ha="left",
    color="#222222",
    fontweight="bold",
    fontsize=9.5,
    bbox=dict(boxstyle="square,pad=0.2", fc="white", alpha=0.85, ec="gray", lw=0.5),
)

# Last Year Ratio Gap Arrow
ax.annotate(
    "",
    xy=(end_year, tcs_starting_salary_usd[-1]),
    xytext=(end_year, india_gdp_pc[-1]),
    arrowprops=dict(arrowstyle="<->", linestyle=":", color="#333333", linewidth=2),
)
ax.text(
    end_year - 0.3,
    (tcs_starting_salary_usd[-1] * india_gdp_pc[-1]) ** 0.5,
    f"Salary Gap:\n{ratio_withpc_end:.1f}x Salary",
    va="center",
    ha="right",
    color="#222222",
    fontweight="bold",
    fontsize=9.5,
    bbox=dict(boxstyle="square,pad=0.2", fc="white", alpha=0.85, ec="gray", lw=0.5),
)

# Render Legends
ax.legend(loc="lower right", fontsize=11, framealpha=0.95, facecolor="white")

plt.tight_layout()
plt.show()
