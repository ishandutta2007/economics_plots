import matplotlib.pyplot as plt
import pandas as pd

# 1. Prepare historical macroeconomic data
# Figures are in Billions of USD (Nominal values matching historic reporting eras)
data = {
    "Year": [
        1947, 1950, 1960, 1965, 1970, 1975, 1980, 1985, 
        1990, 1991, 1992, 1995, 2000, 2004, 2008, 2010, 
        2013, 2015, 2018, 2020, 2021, 2022, 2023, 2024, 2025, 2026
    ],
    "Forex_Reserves_USD_Billion": [
        1.5, 2.1, 0.6, 0.5, 0.7, 1.5, 4.0, 4.5, 
        1.2, 1.1, 5.6, 20.8, 38.0, 113.0, 310.0, 279.0, 
        304.0, 351.0, 413.0, 586.0, 633.0, 563.0, 623.0, 640.0, 688.0, 692.87
    ],
    "GDP_USD_Billion": [
        20.0, 25.0, 37.03, 59.37, 62.40, 97.05, 186.18, 231.87, 
        321.26, 270.11, 288.21, 360.50, 468.42, 709.12, 1198.90, 1708.46, 
        1856.70, 2103.59, 2702.93, 2671.39, 3150.30, 3501.00, 3761.00, 3930.00, 3956.07, 4300.0
    ]
}

# 2. Construct DataFrame and compute ratio
df = pd.DataFrame(data)
df["Forex_as_Percent_of_GDP"] = (df["Forex_Reserves_USD_Billion"] / df["GDP_USD_Billion"]) * 100

# 3. Create the plot
plt.figure(figsize=(12, 6.5))
plt.plot(
    df["Year"], df["Forex_as_Percent_of_GDP"], 
    marker="o", color="#008080", linewidth=2.5, markersize=6, label="Forex Reserves (% of GDP)"
)

# 4. Highlight key structural economic pivot points and annotate all data points
pivots = {
    1991: ("1991 Crisis\n(1.1B Reserves)", "#D9534F"),
    2004: ("Crossed 100B\nReserves", "#F0AD4E"),
    2026: ("Current Era\n(692B Reserves)", "#5CB85C")
}

for year, (label, color) in pivots.items():
    val = df.loc[df["Year"] == year, "Forex_as_Percent_of_GDP"].values[0]
    plt.axvline(x=year, color=color, linestyle="--", alpha=0.7)
    plt.annotate(
        label, xy=(year, val), xytext=(year - 4, val + 2.5),
        arrowprops=dict(facecolor='black', arrowstyle='->', lw=0.8),
        fontsize=8, fontweight='bold', bbox=dict(boxstyle="round,pad=0.3", fc="yellow", alpha=0.3)
    )

# Annotate each individual data point with its Forex as % of GDP value
for idx, row in df.iterrows():
    year = int(row["Year"])
    val = row["Forex_as_Percent_of_GDP"]
    plt.annotate(
        f"{val:.1f}%",
        xy=(year, val),
        xytext=(0, 6),
        textcoords="offset points",
        ha="center",
        va="bottom",
        fontsize=7,
        alpha=0.85
    )

# 5. Format and polish chart elements
plt.title("India's Foreign Exchange Reserves as a Percentage of GDP (1947–2026)", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Year", fontsize=11, fontweight='bold')
plt.ylabel("Forex Reserves (% of GDP)", fontsize=11, fontweight='bold')
plt.xlim(1945, 2028)
plt.ylim(0, df["Forex_as_Percent_of_GDP"].max() + 5)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(loc="upper left")

# 6. Render plot visualization
plt.tight_layout()
plt.show()
