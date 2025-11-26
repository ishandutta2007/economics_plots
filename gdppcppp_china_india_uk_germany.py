import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2025, 2101)

# Define the initial GDP per capita (PPP) values for 2025
india_2025 = 12100
china_2025 = 29191
germany_2025 = 73553
uk_2025 = 63760

# Define the growth rates
india_growth_rate_till_2040 = 0.065  # 6.50%
india_growth_rate_2040_2060 = 0.045  # 4.50%
india_growth_rate_2060_2080 = 0.03  # 3%
india_growth_rate_2080_2100 = 0.02  # 2%

china_growth_rate_till_2040 = 0.045  # 4.5%
china_growth_rate_2040_2060 = 0.03  # 3%
china_growth_rate_2060_2100 = 0.02  # 2%

germany_growth_rate = 0.015  # 1.5%
uk_growth_rate = 0.015  # 1.5%

# Calculate the projected GDP per capita (PPP) values
india_gdp_ppp = []
current_gdp = india_2025
india_gdp_ppp.append(current_gdp)
for year in years[1:]:
    if year <= 2040:
        growth_rate = india_growth_rate_till_2040
    elif year <= 2060:
        growth_rate = india_growth_rate_2040_2060
    elif year <= 2080:
        growth_rate = india_growth_rate_2060_2080
    else:
        growth_rate = india_growth_rate_2080_2100

    current_gdp = current_gdp * (1 + growth_rate)
    india_gdp_ppp.append(current_gdp)

china_gdp_ppp = []
current_gdp = china_2025
china_gdp_ppp.append(current_gdp)
for year in years[1:]:
    if year <= 2040:
        growth_rate = china_growth_rate_till_2040
    elif year <= 2060:
        growth_rate = china_growth_rate_2040_2060
    elif year <= 2080:
        growth_rate = china_growth_rate_2060_2100
    else:
        growth_rate = china_growth_rate_2060_2100

    current_gdp = current_gdp * (1 + growth_rate)
    china_gdp_ppp.append(current_gdp)

germany_gdp_ppp = [
    germany_2025 * ((1 + germany_growth_rate) ** (year - 2025)) for year in years
]
uk_gdp_ppp = [uk_2025 * ((1 + uk_growth_rate) ** (year - 2025)) for year in years]

# Plot the data
plt.figure(figsize=(10, 6))

india_label = f"India ({india_growth_rate_till_2040 * 100:.1f}%(2025-2040)/{india_growth_rate_2040_2060 * 100:.1f}%(2040-2060)/{india_growth_rate_2060_2080 * 100:.1f}%(2060-2080)/{india_growth_rate_2080_2100 * 100:.1f}%(2080-2100))"
china_label = f"China ({china_growth_rate_till_2040 * 100:.1f}%(2025-2040)/{china_growth_rate_2040_2060 * 100:.1f}%(2040-2060)/{china_growth_rate_2060_2100 * 100:.1f}%(2060-2100))"
germany_label = f"Germany ({germany_growth_rate * 100:.1f}%)"
uk_label = f"UK ({uk_growth_rate * 100:.1f}%)"

plt.plot(years, india_gdp_ppp, label=india_label, marker="o", markersize=2)
plt.plot(years, china_gdp_ppp, label=china_label, marker="o", markersize=2)
plt.plot(years, germany_gdp_ppp, label=germany_label, marker="o", markersize=2)
plt.plot(years, uk_gdp_ppp, label=uk_label, marker="o", markersize=2)

# Annotate the points
for i, year in enumerate(years):
    if year % 5 == 0:
        plt.annotate(
            f"{int(india_gdp_ppp[i])}",
            (year, india_gdp_ppp[i]),
            textcoords="offset points",
            xytext=(0, -10),
            ha="center",
            fontsize=8,
        )
        plt.annotate(
            f"{int(china_gdp_ppp[i])}",
            (year, china_gdp_ppp[i]),
            textcoords="offset points",
            xytext=(0, -10),
            ha="center",
            fontsize=8,
        )
        plt.annotate(
            f"{int(germany_gdp_ppp[i])}",
            (year, germany_gdp_ppp[i]),
            textcoords="offset points",
            xytext=(0, 10),
            ha="center",
            fontsize=8,
        )
        plt.annotate(
            f"{int(uk_gdp_ppp[i])}",
            (year, uk_gdp_ppp[i]),
            textcoords="offset points",
            xytext=(0, 10),
            ha="center",
            fontsize=8,
        )

# Add labels and title
plt.xlabel("Year")
plt.ylabel("GDP per Capita (PPP) in USD")
plt.title("Projected GDP per Capita (PPP) till 2100")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
