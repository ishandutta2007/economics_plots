import matplotlib.pyplot as plt
import pandas as pd

# 1. Prepare the historical dataset (Values in Trillions of current USD)
data = {
    "Year": [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    "India_GDP": [2.10, 2.29, 2.65, 2.70, 2.84, 2.67, 3.15, 3.42, 3.57, 3.94],
    "India_Wealth": [
        7.01,
        7.70,
        8.98,
        10.56,
        12.61,
        12.83,
        14.22,
        15.36,
        16.01,
        17.40,
    ],
    "China_GDP": [
        11.06,
        11.23,
        12.31,
        13.89,
        14.28,
        14.69,
        17.82,
        17.96,
        17.79,
        18.53,
    ],
    "China_Wealth": [
        40.70,
        44.40,
        51.87,
        57.60,
        65.40,
        74.87,
        85.10,
        84.48,
        91.08,
        95.00,
    ],
    "USA_GDP": [
        18.24,
        18.70,
        19.54,
        20.61,
        21.43,
        21.06,
        23.32,
        25.46,
        27.36,
        29.17,
    ],
    "USA_Wealth": [
        83.50,
        89.20,
        96.50,
        102.79,
        111.00,
        126.34,
        145.80,
        139.87,
        163.90,
        175.00,
    ],
}

df = pd.DataFrame(data)

# 2. Calculate the Asset Turnover Ratio (GDP / Private Wealth) for each country
df["India_Ratio"] = df["India_GDP"] / df["India_Wealth"]
df["China_Ratio"] = df["China_GDP"] / df["China_Wealth"]
df["USA_Ratio"] = df["USA_GDP"] / df["USA_Wealth"]

# 3. Plot the data
plt.figure(figsize=(10, 6))

plt.plot(
    df["Year"],
    df["India_Ratio"],
    marker="o",
    linewidth=2,
    color="#FF9933",
    label="India",
)
plt.plot(
    df["Year"],
    df["China_Ratio"],
    marker="s",
    linewidth=2,
    color="#DE2910",
    label="China",
)
plt.plot(
    df["Year"],
    df["USA_Ratio"],
    marker="^",
    linewidth=2,
    color="#002868",
    label="United States",
)

# 4. Enhance the chart details
plt.title(
    "National Asset Turnover Ratio Over Time (2015–2024)\n[Nominal GDP / Net Total Private Wealth]",
    fontsize=14,
    fontweight="bold",
    pad=15,
)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Ratio (GDP per Dollar of Asset Value)", fontsize=12)
plt.xticks(df["Year"])  # Ensure all years show explicitly
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(fontsize=11, loc="upper right")

# 5. Clean layout adjustments and visualization
plt.tight_layout()
plt.show()
