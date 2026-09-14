import matplotlib.pyplot as plt

# Dataset: R&D spending as a % of GDP (1996 - 2026)
years = [1996, 2000, 2010, 2020, 2022, 2026]

# Data points based on historical World Bank
china_rd = [0.56, 0.89, 1.76, 2.40, 2.55, 2.75]
usa_rd = [2.40, 2.72, 2.74, 3.12, 3.45, 3.45]
south_korea_rd = [2.26, 2.18, 3.47, 4.80, 5.21, 5.15]
israel_rd = [2.66, 3.92, 3.93, 5.53, 6.02, 6.30]
india_rd = [0.60, 0.74, 0.79, 0.64, 0.65, 0.64]

# Create the figure layout (slightly widened to prevent label collisions)
plt.figure(figsize=(14, 8))

# Plot lines with custom markers and styles
plt.plot(
    years,
    israel_rd,
    marker="^",
    color="#0038A8",
    linewidth=2.5,
    linestyle="-",
    label="Israel",
)
plt.plot(
    years,
    south_korea_rd,
    marker="d",
    color="#000000",
    linewidth=2.5,
    linestyle="-",
    label="South Korea",
)
plt.plot(
    years,
    usa_rd,
    marker="s",
    color="#1F77B4",
    linewidth=2.5,
    linestyle="--",
    label="USA",
)
plt.plot(
    years,
    china_rd,
    marker="o",
    color="#D62728",
    linewidth=2.5,
    linestyle="--",
    label="China",
)
plt.plot(
    years,
    india_rd,
    marker="v",
    color="#FF9933",
    linewidth=2.5,
    linestyle=":",
    label="India",
)

# Visual styling
plt.title(
    "Global R&D Expenditure Comparison as a % of GDP (1996-2026)",
    fontsize=14,
    fontweight="bold",
)
plt.xlabel("Year", fontsize=12)
plt.ylabel("R&D Spending (% of GDP)", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend(fontsize=11, loc="upper left")

# Aggregate datasets for clean annotation iteration
all_data = [
    ("Israel", israel_rd, "#0038A8"),
    ("S. Korea", south_korea_rd, "#000000"),
    ("USA", usa_rd, "#1F77B4"),
    ("China", china_rd, "#D62728"),
    ("India", india_rd, "#FF9933"),
]

# Annotate all plotted points
for country, data, color in all_data:
    for i, (year, val) in enumerate(zip(years, data)):
        # Keep country label on the final point, push it to the right
        if i == len(years) - 1:
            label_text = f"{val}% {country}"
            xy_offset = (8, -3)
            align = "left"
        # For all preceding points, just show the value, centered above the marker
        else:
            label_text = f"{val}%"
            if country in ["India","S. Korea"]:
                xy_offset = (0, -18)
            else:
                xy_offset = (0, 8)
            align = "center"

        plt.annotate(
            label_text,
            xy=(year, val),
            xytext=xy_offset,
            textcoords="offset points",
            ha=align,
            color=color,
            fontweight="bold",
            fontsize=9,
        )

# Render and align margins
plt.xlim(
    1994, 2031
)  # Extended x-axis slightly left and right to prevent cut-off annotations
plt.tight_layout()
plt.show()
