import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1. Prepare data for 30 major economies
# GDP per Capita represents current PPP (International Dollars)
# R&D intensity represents total R&D expenditure as a % of GDP
data = {
    "Country": [
        "United States",
        "China",
        "Japan",
        "Germany",
        "United Kingdom",
        "India",
        "France",
        "Italy",
        "Canada",
        "Brazil",
        "Russia",
        "South Korea",
        "Australia",
        "Mexico",
        "Spain",
        "Indonesia",
        "Saudi Arabia",
        "Netherlands",
        "Turkey",
        "Switzerland",
        "Poland",
        "Sweden",
        "Belgium",
        "Argentina",
        "Thailand",
        "Austria",
        "Israel",
        "Singapore",
        "South Africa",
        "Norway",
    ],
    "GDP_per_Capita_PPP": [
        80000,
        23000,
        48000,
        64000,
        55000,
        9000,
        56000,
        54000,
        58000,
        18000,
        34000,
        53000,
        63000,
        22000,
        47000,
        15000,
        67000,
        70000,
        39000,
        86000,
        43000,
        65000,
        66000,
        26000,
        21000,
        68000,
        52000,
        134000,
        16000,
        95000,
    ],
    "RD_Percent_GDP": [
        3.6,
        2.6,
        3.4,
        3.1,
        2.9,
        0.6,
        2.2,
        1.3,
        1.7,
        1.2,
        0.9,
        5.2,
        1.9,
        0.3,
        1.4,
        0.3,
        0.6,
        2.3,
        1.4,
        3.4,
        1.5,
        3.6,
        3.4,
        0.5,
        1.2,
        3.2,
        5.6,
        2.2,
        0.6,
        1.6,
    ],
}

df = pd.DataFrame(data)

# 2. Set style and figure details
sns.set_theme(style="whitegrid")
plt.figure(figsize=(14, 9))

# 3. Create the scatter plot
scatter = sns.scatterplot(
    data=df,
    x="GDP_per_Capita_PPP",
    y="RD_Percent_GDP",
    s=140,
    color="#1f77b4",
    alpha=0.8,
    edgecolor="w",
    linewidth=1.5,
)

# 4. Fit a linear trendline (excluding extreme outlier Singapore for trend balance if preferred, included here)
x = df["GDP_per_Capita_PPP"]
y = df["RD_Percent_GDP"]
m, b = np.polyfit(x, y, 1)
plt.plot(
    x,
    m * x + b,
    color="#ff7f0e",
    linestyle="--",
    linewidth=2,
    label=f"Trendline (r = {df['GDP_per_Capita_PPP'].corr(df['RD_Percent_GDP']):.2f})",
)

# 5. Dynamic text adjustment avoiding overlaps for clear visualization
for i in range(df.shape[0]):
    # Add subtle padding adjustments based on specific country positions
    x_offset = 1200
    y_offset = 0.03
    if df["Country"][i] in ["Singapore", "Israel", "South Korea"]:
        y_offset = -0.12  # prevent text clips or label crowding

    plt.text(
        df["GDP_per_Capita_PPP"][i] + x_offset,
        df["RD_Percent_GDP"][i] + y_offset,
        df["Country"][i],
        horizontalalignment="left",
        size="medium",
        color="black",
        weight="semibold",
        alpha=0.85,
    )

# 6. Customize chart labels and titles
plt.title(
    "Global Innovation Engine: R&D Intensity vs Wealth",
    fontsize=18,
    weight="bold",
    pad=20,
)
plt.xlabel("GDP per Capita, PPP (Current International $)", fontsize=13, labelpad=12)
plt.ylabel("Research & Development Spending (% of GDP)", fontsize=13, labelpad=12)
plt.xlim(0, 145000)
plt.ylim(0, 6.2)
plt.legend(loc="upper left", fontsize=12)

# 7. Display chart
plt.tight_layout()
plt.show()
