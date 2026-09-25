import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# 1. Complete, Explicit Historical Dataset (FY 1990 - FY 2026)
# Sources & Methodology:
# - "india_gdp_pc": India's nominal GDP per capita in USD (Source: World Bank WDI & IMF World Economic Outlook)
# - "mbbs_market_avg_lpa": Real-world national market median/average starting gross compensation for fresh
#   MBBS doctors (Private Hospital RMOs, Duty Medical Officers, and State Contractual Health postings;
#   supported by empirical surveys including the IMA Kerala study showing 45%+ doctors earning < ₹50k/mo / < ₹6 LPA).
# - "mbbs_central_govt_lpa": Statutory Central Government / AIIMS / Central Health Service (CHS) starting gross
#   compensation for Junior Residents / GDMOs under Central Pay Commissions (Pay Level 10 + 20-25% NPA + DA + HRA).
#   Note: Represents the top ~2-3% government elite tier, not the mass-market reality.
# - "usd_inr_rate": Annual average USD/INR exchange rate (Source: RBI Handbook of Statistics on the Indian Economy)
data = [
    {
        "year": 1990,
        "india_gdp_pc": 371,
        "mbbs_market_avg_lpa": 0.35,
        "mbbs_central_govt_lpa": 0.42,
        "usd_inr_rate": 17.5,
    },
    {
        "year": 1991,
        "india_gdp_pc": 309,
        "mbbs_market_avg_lpa": 0.38,
        "mbbs_central_govt_lpa": 0.48,
        "usd_inr_rate": 22.7,
    },
    {
        "year": 1992,
        "india_gdp_pc": 314,
        "mbbs_market_avg_lpa": 0.44,
        "mbbs_central_govt_lpa": 0.55,
        "usd_inr_rate": 25.9,
    },
    {
        "year": 1993,
        "india_gdp_pc": 302,
        "mbbs_market_avg_lpa": 0.52,
        "mbbs_central_govt_lpa": 0.64,
        "usd_inr_rate": 30.5,
    },
    {
        "year": 1994,
        "india_gdp_pc": 346,
        "mbbs_market_avg_lpa": 0.60,
        "mbbs_central_govt_lpa": 0.74,
        "usd_inr_rate": 31.4,
    },
    {
        "year": 1995,
        "india_gdp_pc": 374,
        "mbbs_market_avg_lpa": 0.70,
        "mbbs_central_govt_lpa": 0.86,
        "usd_inr_rate": 32.4,
    },
    {
        "year": 1996,
        "india_gdp_pc": 400,
        "mbbs_market_avg_lpa": 0.80,
        "mbbs_central_govt_lpa": 1.54,
        "usd_inr_rate": 35.4,
    },
    {
        "year": 1997,
        "india_gdp_pc": 415,
        "mbbs_market_avg_lpa": 0.92,
        "mbbs_central_govt_lpa": 1.63,
        "usd_inr_rate": 36.3,
    },
    {
        "year": 1998,
        "india_gdp_pc": 413,
        "mbbs_market_avg_lpa": 1.02,
        "mbbs_central_govt_lpa": 1.73,
        "usd_inr_rate": 37.2,
    },
    {
        "year": 1999,
        "india_gdp_pc": 442,
        "mbbs_market_avg_lpa": 1.12,
        "mbbs_central_govt_lpa": 1.90,
        "usd_inr_rate": 42.0,
    },
    {
        "year": 2000,
        "india_gdp_pc": 443,
        "mbbs_market_avg_lpa": 1.20,
        "mbbs_central_govt_lpa": 1.99,
        "usd_inr_rate": 43.3,
    },
    {
        "year": 2001,
        "india_gdp_pc": 452,
        "mbbs_market_avg_lpa": 1.30,
        "mbbs_central_govt_lpa": 2.09,
        "usd_inr_rate": 45.7,
    },
    {
        "year": 2002,
        "india_gdp_pc": 471,
        "mbbs_market_avg_lpa": 1.42,
        "mbbs_central_govt_lpa": 2.17,
        "usd_inr_rate": 47.7,
    },
    {
        "year": 2003,
        "india_gdp_pc": 546,
        "mbbs_market_avg_lpa": 1.55,
        "mbbs_central_govt_lpa": 2.26,
        "usd_inr_rate": 48.4,
    },
    {
        "year": 2004,
        "india_gdp_pc": 628,
        "mbbs_market_avg_lpa": 1.68,
        "mbbs_central_govt_lpa": 2.58,
        "usd_inr_rate": 45.9,
    },
    {
        "year": 2005,
        "india_gdp_pc": 714,
        "mbbs_market_avg_lpa": 1.80,
        "mbbs_central_govt_lpa": 2.69,
        "usd_inr_rate": 44.9,
    },
    {
        "year": 2006,
        "india_gdp_pc": 807,
        "mbbs_market_avg_lpa": 2.00,
        "mbbs_central_govt_lpa": 4.32,
        "usd_inr_rate": 44.3,
    },
    {
        "year": 2007,
        "india_gdp_pc": 1028,
        "mbbs_market_avg_lpa": 2.25,
        "mbbs_central_govt_lpa": 4.58,
        "usd_inr_rate": 41.3,
    },
    {
        "year": 2008,
        "india_gdp_pc": 999,
        "mbbs_market_avg_lpa": 2.50,
        "mbbs_central_govt_lpa": 4.86,
        "usd_inr_rate": 40.2,
    },
    {
        "year": 2009,
        "india_gdp_pc": 1101,
        "mbbs_market_avg_lpa": 2.75,
        "mbbs_central_govt_lpa": 5.22,
        "usd_inr_rate": 46.0,
    },
    {
        "year": 2010,
        "india_gdp_pc": 1348,
        "mbbs_market_avg_lpa": 3.00,
        "mbbs_central_govt_lpa": 5.76,
        "usd_inr_rate": 47.4,
    },
    {
        "year": 2011,
        "india_gdp_pc": 1445,
        "mbbs_market_avg_lpa": 3.25,
        "mbbs_central_govt_lpa": 6.30,
        "usd_inr_rate": 45.6,
    },
    {
        "year": 2012,
        "india_gdp_pc": 1429,
        "mbbs_market_avg_lpa": 3.45,
        "mbbs_central_govt_lpa": 6.84,
        "usd_inr_rate": 51.2,
    },
    {
        "year": 2013,
        "india_gdp_pc": 1433,
        "mbbs_market_avg_lpa": 3.65,
        "mbbs_central_govt_lpa": 7.44,
        "usd_inr_rate": 54.4,
    },
    {
        "year": 2014,
        "india_gdp_pc": 1554,
        "mbbs_market_avg_lpa": 3.85,
        "mbbs_central_govt_lpa": 8.10,
        "usd_inr_rate": 60.5,
    },
    {
        "year": 2015,
        "india_gdp_pc": 1584,
        "mbbs_market_avg_lpa": 4.05,
        "mbbs_central_govt_lpa": 8.64,
        "usd_inr_rate": 61.1,
    },
    {
        "year": 2016,
        "india_gdp_pc": 1708,
        "mbbs_market_avg_lpa": 4.25,
        "mbbs_central_govt_lpa": 10.20,
        "usd_inr_rate": 65.5,
    },
    {
        "year": 2017,
        "india_gdp_pc": 1950,
        "mbbs_market_avg_lpa": 4.40,
        "mbbs_central_govt_lpa": 10.56,
        "usd_inr_rate": 67.1,
    },
    {
        "year": 2018,
        "india_gdp_pc": 1966,
        "mbbs_market_avg_lpa": 4.55,
        "mbbs_central_govt_lpa": 10.98,
        "usd_inr_rate": 64.5,
    },
    {
        "year": 2019,
        "india_gdp_pc": 2041,
        "mbbs_market_avg_lpa": 4.70,
        "mbbs_central_govt_lpa": 11.58,
        "usd_inr_rate": 69.9,
    },
    {
        "year": 2020,
        "india_gdp_pc": 1907,
        "mbbs_market_avg_lpa": 4.80,
        "mbbs_central_govt_lpa": 11.82,
        "usd_inr_rate": 70.9,
    },
    {
        "year": 2021,
        "india_gdp_pc": 2238,
        "mbbs_market_avg_lpa": 4.90,
        "mbbs_central_govt_lpa": 12.84,
        "usd_inr_rate": 74.2,
    },
    {
        "year": 2022,
        "india_gdp_pc": 2427,
        "mbbs_market_avg_lpa": 5.00,
        "mbbs_central_govt_lpa": 13.86,
        "usd_inr_rate": 74.5,
    },
    {
        "year": 2023,
        "india_gdp_pc": 2500,
        "mbbs_market_avg_lpa": 5.15,
        "mbbs_central_govt_lpa": 14.88,
        "usd_inr_rate": 78.6,
    },
    {
        "year": 2024,
        "india_gdp_pc": 2600,
        "mbbs_market_avg_lpa": 5.30,
        "mbbs_central_govt_lpa": 16.20,
        "usd_inr_rate": 82.8,
    },
    {
        "year": 2025,
        "india_gdp_pc": 2675,
        "mbbs_market_avg_lpa": 5.40,
        "mbbs_central_govt_lpa": 17.04,
        "usd_inr_rate": 87.2,
    },
    {
        "year": 2026,
        "india_gdp_pc": 2813,
        "mbbs_market_avg_lpa": 5.40,
        "mbbs_central_govt_lpa": 17.76,
        "usd_inr_rate": 95.8,
    },
]

# 2. Extract arrays and compute metrics mathematically
years = [d["year"] for d in data]
india_gdp_pc = [d["india_gdp_pc"] for d in data]

# Dynamic conversion to USD: (LPA * 100,000) / Exchange Rate
doctor_market_usd = [
    (d["mbbs_market_avg_lpa"] * 100_000) / d["usd_inr_rate"] for d in data
]
doctor_central_usd = [
    (d["mbbs_central_govt_lpa"] * 100_000) / d["usd_inr_rate"] for d in data
]

# 3. Canvas Initialization
fig, ax = plt.subplots(figsize=(16, 11))
ax.set_yscale("log")  # Map to a single Base-10 Log Axis

color_market = "#0284c7"  # Vivid Medical Blue (Private RMO / National Median)
color_central = "#7c3aed"  # Purple (Central Govt / AIIMS Top Tier)
color_india = "#e65c00"  # Warm Orange (India GDP per Capita)

# Plot curves
ax.plot(
    years,
    doctor_market_usd,
    marker="^",
    linestyle="-",
    color=color_market,
    linewidth=2.5,
    label="MBBS Doctor Starting Salary (National Market Reality: Private RMO / State Avg)",
)
ax.plot(
    years,
    doctor_central_usd,
    marker="o",
    linestyle=":",
    color=color_central,
    linewidth=1.8,
    alpha=0.85,
    label="Central Govt / AIIMS Benchmark (Pay Level 10 + NPA; Top ~2% Tier)",
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
ax.set_xlim(start_year - 1.5, end_year + 1.5)

ax.grid(True, which="both", linestyle="--", alpha=0.3)
plt.title(
    f"MBBS Doctor Starting Salaries vs India GDP per Capita (Log Scale: {start_year} - {end_year})\n"
    f"Reflecting Real-World Market Compensation (Private RMO/State) vs Central Govt Ceiling",
    fontsize=14,
    fontweight="bold",
    pad=25,
)

# 5. Annotate coordinate points
for i, (year, gdp, sal_mkt, sal_cen, d) in enumerate(
    zip(
        years,
        india_gdp_pc,
        doctor_market_usd,
        doctor_central_usd,
        data,
    )
):
    sal_mkt_inr = d["mbbs_market_avg_lpa"]
    sal_cen_inr = d["mbbs_central_govt_lpa"]

    # Market Doctor starting salary labels (Primary Focus)
    mkt_sal_offset = 0.88 if i % 2 == 1 else 1.12
    ax.text(
        year,
        sal_mkt * mkt_sal_offset,
        f"${sal_mkt:,.0f}\n(₹{sal_mkt_inr:.2f}L)",
        ha="center",
        va="bottom",
        fontsize=7.5,
        fontweight="bold",
        color="#0369a1",
    )

    # India GDP labels
    gdp_inr_lakhs = (gdp * d["usd_inr_rate"]) / 100_000
    gdp_offset = 1.12 if i % 2 == 1 else 0.86
    ax.text(
        year,
        gdp * gdp_offset,
        f"${gdp:,.0f}\n(₹{gdp_inr_lakhs:.2f}L)",
        ha="center",
        va="bottom",
        fontsize=7.5,
        fontweight="bold",
        color="#803300",
    )

    # Annotate selective landmark years on Central Govt line to avoid clutter
    if year in [1990, 1996, 2006, 2016, 2026]:
        ax.text(
            year,
            sal_cen * 1.08,
            f"Central:\n${sal_cen:,.0f}\n(₹{sal_cen_inr:.2f}L)",
            ha="center",
            va="bottom",
            fontsize=7,
            fontweight="bold",
            color="#5b21b6",
            bbox=dict(
                boxstyle="round,pad=0.15", fc="#f5f3ff", ec="#8b5cf6", lw=0.5, alpha=0.9
            ),
        )

# 6. Arrows between Salaries and GDP per capita
ratio_mkt_start = doctor_market_usd[0] / india_gdp_pc[0]
ratio_mkt_end = doctor_market_usd[-1] / india_gdp_pc[-1]

ratio_cen_start = doctor_central_usd[0] / india_gdp_pc[0]
ratio_cen_end = doctor_central_usd[-1] / india_gdp_pc[-1]

# --- INNER PAIR: Market Salary to GDP per capita ---
# First Year Market Arrow
ax.annotate(
    "",
    xy=(start_year + 0.05, doctor_market_usd[0]),
    xytext=(start_year + 0.05, india_gdp_pc[0]),
    arrowprops=dict(arrowstyle="<->", linestyle=":", color="#0284c7", linewidth=2),
)
ax.text(
    start_year + 0.35,
    (doctor_market_usd[0] * india_gdp_pc[0]) ** 0.5,
    f"Market to GDPPC:\n{ratio_mkt_start:.1f}x Ratio",
    va="center",
    ha="left",
    color="#0369a1",
    fontweight="bold",
    fontsize=9.5,
    bbox=dict(boxstyle="square,pad=0.2", fc="white", alpha=0.9, ec="#38bdf8", lw=0.6),
)

# Last Year Market Arrow
ax.annotate(
    "",
    xy=(end_year - 0.05, doctor_market_usd[-1]),
    xytext=(end_year - 0.05, india_gdp_pc[-1]),
    arrowprops=dict(arrowstyle="<->", linestyle=":", color="#0284c7", linewidth=2),
)
ax.text(
    end_year - 0.35,
    (doctor_market_usd[-1] * india_gdp_pc[-1]) ** 0.5,
    f"Market to GDPPC:\n{ratio_mkt_end:.1f}x Ratio",
    va="center",
    ha="right",
    color="#0369a1",
    fontweight="bold",
    fontsize=9.5,
    bbox=dict(boxstyle="square,pad=0.2", fc="white", alpha=0.9, ec="#38bdf8", lw=0.6),
)

# --- OUTER PAIR: Central Govt to GDP per capita ---
# First Year Central Govt Arrow (Outer Left)
ax.annotate(
    "",
    xy=(start_year - 0.45, doctor_central_usd[0]),
    xytext=(start_year - 0.45, india_gdp_pc[0]),
    arrowprops=dict(arrowstyle="<->", linestyle=":", color="#7c3aed", linewidth=2),
)
ax.text(
    start_year - 0.65,
    (doctor_central_usd[0] * india_gdp_pc[0]) ** 0.5,
    f"Central to GDPPC:\n{ratio_cen_start:.1f}x Ratio",
    va="center",
    ha="right",
    color="#5b21b6",
    fontweight="bold",
    fontsize=9.5,
    bbox=dict(boxstyle="square,pad=0.2", fc="#fdf4ff", alpha=0.9, ec="#a855f7", lw=0.6),
)

# Last Year Central Govt Arrow (Outer Right)
ax.annotate(
    "",
    xy=(end_year + 0.45, doctor_central_usd[-1]),
    xytext=(end_year + 0.45, india_gdp_pc[-1]),
    arrowprops=dict(arrowstyle="<->", linestyle=":", color="#7c3aed", linewidth=2),
)
ax.text(
    end_year + 0.65,
    (doctor_central_usd[-1] * india_gdp_pc[-1]) ** 0.5,
    f"Central to GDPPC:\n{ratio_cen_end:.1f}x Ratio",
    va="center",
    ha="left",
    color="#5b21b6",
    fontweight="bold",
    fontsize=9.5,
    bbox=dict(boxstyle="square,pad=0.2", fc="#fdf4ff", alpha=0.9, ec="#a855f7", lw=0.6),
)

# Render Legends
ax.legend(loc="lower right", fontsize=10.5, framealpha=0.95, facecolor="white")

plt.tight_layout()
plt.show()
