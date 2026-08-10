import matplotlib.pyplot as plt

# 1. Define the dataset (Deaths converted to Millions)
decades = [
    "1900–09",
    "1910–19",
    "1920–29",
    "1930–39",
    "1940–49",
    "1950–59",
    "1960–69",
    "1970–79",
    "1980–89",
    "1990–199",
    "2000–09",
    "2010–19",
    "2020–24*",
]

deaths_millions = [
    0.75,  # 750k
    30.0,  # 30M (WWI)
    3.0,  # 3M
    12.5,  # 12.5M
    77.5,  # 77.5M (WWII)
    5.0,  # 5M
    4.0,  # 4M
    5.5,  # 5.5M
    2.5,  # 2.5M
    5.5,  # 5.5M (Congo/Rwanda)
    1.5,  # 1.5M
    1.25,  # 1.25M
    0.8,  # 800k (Partial decade)
]

# 2. Initialize the plot layout
plt.figure(figsize=(12, 6), dpi=100)
bars = plt.bar(
    decades, deaths_millions, color="#b22222", edgecolor="#4a0000", alpha=0.9, width=0.7
)

# Add a trend line (3-decade rolling mean)
rolling_mean = []
for i in range(len(deaths_millions)):
    start = max(0, i - 1)
    end = min(len(deaths_millions), i + 2)
    window = deaths_millions[start:end]
    rolling_mean.append(sum(window) / len(window))

plt.plot(
    decades,
    rolling_mean,
    color="#1a1a1a",
    linestyle="-",
    linewidth=2.5,
    alpha=0.8,
    label="3-Decade Trend",
)
plt.legend(loc="upper right")

# 3. Visual Styling & Labels
plt.title(
    "Global War-Related Deaths by Decade (1900–2024)\nBased on Mean Estimates of Total Excess Mortality",
    fontsize=14,
    fontweight="bold",
    pad=15,
    color="#2c3e50",
)
plt.xlabel("Decade", fontsize=11, fontweight="bold", labelpad=10)
plt.ylabel(
    "Estimated Total Deaths (in Millions)", fontsize=11, fontweight="bold", labelpad=10
)
plt.grid(axis="y", linestyle=":", alpha=0.6)

# 4. Attach Value Labels to Each Bar
for bar in bars:
    height = bar.get_height()
    # Format labels below 1M cleanly as decimals (e.g., 0.75M)
    label_text = f"{height:.2f}M" if height < 1.0 else f"{height:.1f}M"

    plt.text(
        bar.get_x() + bar.get_width() / 2.0,
        height + 1.2,
        label_text,
        ha="center",
        va="bottom",
        fontsize=9,
        fontweight="bold",
        color="#333333",
    )

# 5. Clean up borders and view limits
plt.ylim(0, 85)
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)

# Adjust layout and execute
plt.tight_layout()
plt.show()
