import matplotlib.pyplot as plt
import pandas as pd

# 1. Prepare historical macroeconomic data
# Figures are in Billions of USD (Nominal values matching historic reporting eras)
data_india = {
    "Year": [
        1947,
        1950,
        1960,
        1965,
        1970,
        1975,
        1980,
        1985,
        1990,
        1991,
        1992,
        1995,
        2000,
        2004,
        2008,
        2010,
        2013,
        2015,
        2018,
        2020,
        2021,
        2022,
        2023,
        2024,
        2025,
        2026,
    ],
    "Forex_Reserves_USD_Billion": [
        1.5,
        2.1,
        0.6,
        0.5,
        0.7,
        1.5,
        4.0,
        4.5,
        1.2,
        1.1,
        5.6,
        20.8,
        38.0,
        113.0,
        310.0,
        279.0,
        304.0,
        351.0,
        413.0,
        586.0,
        633.0,
        563.0,
        623.0,
        640.0,
        688.0,
        692.87,
    ],
    "GDP_USD_Billion": [
        20.0,
        25.0,
        37.03,
        59.37,
        62.40,
        97.05,
        186.18,
        231.87,
        321.26,
        270.11,
        288.21,
        360.50,
        468.42,
        709.12,
        1198.90,
        1708.46,
        1856.70,
        2103.59,
        2702.93,
        2671.39,
        3150.30,
        3501.00,
        3761.00,
        3930.00,
        3956.07,
        4300.0,
    ],
}

data_china = {
    "Year": [
        1950,
        1960,
        1965,
        1970,
        1975,
        1980,
        1985,
        1990,
        1991,
        1992,
        1995,
        2000,
        2004,
        2008,
        2010,
        2013,
        2015,
        2018,
        2020,
        2021,
        2022,
        2023,
        2024,
        2025,
        2026,
    ],
    "Forex_Reserves_USD_Billion": [
        0.15,
        0.10,
        0.11,
        0.18,
        0.47,
        2.5,
        11.9,
        28.6,
        42.6,
        19.4,
        73.6,
        165.6,
        609.9,
        1946.0,
        2847.3,
        3821.3,
        3330.4,
        3072.7,
        3216.5,
        3250.2,
        3127.7,
        3238.0,
        3240.0,
        3300.0,
        3420.0,
    ],
    "GDP_USD_Billion": [
        30.0,
        59.7,
        70.4,
        92.6,
        163.6,
        191.1,
        309.5,
        360.9,
        383.4,
        426.9,
        734.5,
        1211.3,
        1955.3,
        4598.2,
        6087.2,
        9607.2,
        11061.6,
        13894.8,
        14687.7,
        17734.1,
        17963.2,
        17794.8,
        18530.0,
        19200.0,
        19800.0,
    ],
}

# 2. Construct DataFrames and compute ratio
df_india = pd.DataFrame(data_india)
df_india["Forex_as_Percent_of_GDP"] = (
    df_india["Forex_Reserves_USD_Billion"] / df_india["GDP_USD_Billion"]
) * 100

df_china = pd.DataFrame(data_china)
df_china["Forex_as_Percent_of_GDP"] = (
    df_china["Forex_Reserves_USD_Billion"] / df_china["GDP_USD_Billion"]
) * 100

# 3. Create the plot
plt.figure(figsize=(13, 7))
plt.plot(
    df_india["Year"],
    df_india["Forex_as_Percent_of_GDP"],
    marker="o",
    color="#008080",
    linewidth=2.5,
    markersize=5,
    label="India (Forex % of GDP)",
)
plt.plot(
    df_china["Year"],
    df_china["Forex_as_Percent_of_GDP"],
    marker="s",
    color="#DE2910",
    linewidth=2.5,
    markersize=5,
    label="China (Forex % of GDP)",
)

# 4. Annotate all individual data points for India and China
for idx, row in df_india.iterrows():
    year = int(row["Year"])
    val = row["Forex_as_Percent_of_GDP"]
    if year <= 1981:
        plt.annotate(
            f"{val:.1f}%",
            xy=(year, val),
            xytext=(0, 6),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=6.5,
            color="#004D4D",
            fontweight="bold",
        )
    else:
        plt.annotate(
            f"{val:.1f}%",
            xy=(year, val),
            xytext=(0, -20),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=6.5,
            color="#004D4D",
            fontweight="bold",
        )

for idx, row in df_china.iterrows():
    year = int(row["Year"])
    val = row["Forex_as_Percent_of_GDP"]
    # Offset China labels downwards to avoid overlapping when curves are close
    if year <= 1981:
        plt.annotate(
            f"{val:.1f}%",
            xy=(year, val),
            xytext=(0, -10),
            textcoords="offset points",
            ha="center",
            va="top",
            fontsize=6.5,
            color="#8B0000",
            fontweight="bold",
        )
    else:
        plt.annotate(
            f"{val:.1f}%",
            xy=(year, val),
            xytext=(0, 16),
            textcoords="offset points",
            ha="center",
            va="top",
            fontsize=6.5,
            color="#8B0000",
            fontweight="bold",
        )

# 5. Format and polish chart elements
plt.title(
    "Foreign Exchange Reserves as a Percentage of GDP: India vs. China (1947–2026)",
    fontsize=14,
    fontweight="bold",
    pad=15,
)
plt.xlabel("Year", fontsize=11, fontweight="bold")
plt.ylabel("Forex Reserves (% of GDP)", fontsize=11, fontweight="bold")
plt.xlim(1945, 2028)
max_val = max(
    df_india["Forex_as_Percent_of_GDP"].max(), df_china["Forex_as_Percent_of_GDP"].max()
)
plt.ylim(-2, max_val + 7)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(loc="upper left")

# 6. Render plot visualization
plt.tight_layout()
plt.show()
