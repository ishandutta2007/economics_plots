import matplotlib.pyplot as plt
import numpy as np

# Chronological years from 1991 to 2025
years = np.arange(1991, 2026)

# 1. World Average Baseline Real GDP Growth (%)
world_growth = np.array(
    [
        1.23,
        2.06,
        1.86,
        3.42,
        3.18,
        3.59,
        4.00,
        2.78,
        3.58,
        4.57,
        2.03,
        2.32,
        3.07,
        4.50,
        4.06,
        4.49,
        4.43,
        2.09,
        -1.33,
        4.52,
        3.31,
        2.75,
        2.89,
        3.17,
        3.13,
        2.79,
        3.45,
        3.29,
        2.68,
        -2.89,
        6.49,
        3.44,
        2.86,
        2.90,
        2.92,
    ]
)

# 2. China Real GDP Growth (%)
china_growth = np.array(
    [
        9.4,
        14.3,
        13.9,
        13.1,
        11.0,
        10.0,
        9.3,
        7.9,
        7.7,
        8.6,
        8.3,
        9.2,
        10.1,
        10.1,
        11.4,
        12.7,
        14.2,
        9.7,
        9.4,
        10.6,
        9.5,
        7.9,
        7.8,
        7.5,
        7.0,
        6.8,
        6.9,
        6.8,
        6.1,
        2.3,
        8.6,
        3.1,
        5.4,
        5.0,
        5.0,
    ]
)

# 3. India Real GDP Growth (%)
india_growth = np.array(
    [
        1.1,
        5.5,
        4.8,
        6.7,
        7.6,
        7.6,
        4.0,
        6.2,
        8.8,
        3.8,
        4.8,
        3.8,
        7.9,
        7.9,
        9.3,
        9.3,
        9.8,
        3.9,
        8.5,
        10.3,
        5.2,
        5.5,
        6.4,
        7.4,
        8.0,
        8.3,
        6.8,
        6.5,
        3.9,
        -5.8,
        9.7,
        7.6,
        7.2,
        7.1,
        7.7,
    ]
)

# 4. United States Real GDP Growth (%)
usa_growth = np.array(
    [
        -0.1,
        3.5,
        2.8,
        4.0,
        2.7,
        3.8,
        4.4,
        4.5,
        4.8,
        4.1,
        1.0,
        1.7,
        2.8,
        3.8,
        3.5,
        2.9,
        1.9,
        -0.1,
        -2.6,
        2.7,
        1.6,
        2.3,
        1.8,
        2.5,
        2.9,
        1.8,
        2.5,
        3.0,
        2.6,
        -2.2,
        5.8,
        1.9,
        2.5,
        2.8,
        2.1,
    ]
)

# 5. European Union Real GDP Growth (%)
eu_growth = np.array(
    [
        1.4,
        1.1,
        -0.4,
        2.6,
        2.4,
        1.8,
        2.6,
        3.0,
        2.7,
        3.9,
        2.1,
        1.3,
        1.5,
        2.5,
        2.1,
        3.4,
        3.1,
        0.7,
        -4.3,
        2.2,
        1.8,
        -0.7,
        -0.1,
        1.6,
        2.3,
        2.0,
        2.8,
        2.1,
        1.8,
        -5.6,
        5.4,
        3.4,
        0.7,
        1.1,
        1.5,
    ]
)

# Calculate Growth Premiums (Country Growth Rate - World Growth Rate)
china_delta = china_growth - world_growth
india_delta = india_growth - world_growth
usa_delta = usa_growth - world_growth
eu_delta = eu_growth - world_growth

# Expand canvas size significantly to ensure all 140 annotations display clearly
plt.figure(figsize=(22, 12))
plt.style.use(
    "seaborn-v0_8-whitegrid"
    if "seaborn-v0_8-whitegrid" in plt.style.available
    else "default"
)

# Plot the 4 curves with unique markers
plt.plot(
    years,
    china_delta,
    color="#de211b",
    label="China - World",
    linewidth=2.5,
    marker="o",
    markersize=5,
)
plt.plot(
    years,
    india_delta,
    color="#ff9933",
    label="India - World",
    linewidth=2.5,
    marker="s",
    markersize=5,
)
# plt.plot(
#     years,
#     usa_delta,
#     color="#0a36af",
#     label="USA - World",
#     linewidth=2.0,
#     linestyle="--",
#     marker="^",
#     markersize=5,
# )
# plt.plot(
#     years,
#     eu_delta,
#     color="#17becf",
#     label="EU - World",
#     linewidth=2.0,
#     linestyle=":",
#     marker="d",
#     markersize=5,
# )

# Horizontal zero baseline reference
plt.axhline(
    0,
    color="#222222",
    linestyle="-",
    linewidth=2,
    alpha=0.9,
    label="World Average Baseline",
)

# Apply unique offsets to separate labels and minimize spatial overlaps
for idx, x in enumerate(years):
    # China: Positioned above the line
    plt.annotate(
        f"{china_delta[idx]:+.1f}",
        (x, china_delta[idx]),
        textcoords="offset points",
        xytext=(0, 9),
        ha="center",
        fontsize=12,
        color="#9c0f0a",
        fontweight="bold",
    )

    # India: Positioned below the line
    plt.annotate(
        f"{india_delta[idx]:+.1f}",
        (x, india_delta[idx]),
        textcoords="offset points",
        xytext=(0, -13),
        ha="center",
        fontsize=12,
        color="#b35300",
        fontweight="bold",
    )

    # # USA: Alternated or shifted slightly left to clear visual lanes
    # plt.annotate(
    #     f"{usa_delta[idx]:+.1f}",
    #     (x, usa_delta[idx]),
    #     textcoords="offset points",
    #     xytext=(-6, 8),
    #     ha="right",
    #     fontsize=7.5,
    #     color="#06216b",
    #     alpha=0.9,
    # )

    # # EU: Alternated or shifted slightly right to avoid colliding with USA points
    # plt.annotate(
    #     f"{eu_delta[idx]:+.1f}",
    #     (x, eu_delta[idx]),
    #     textcoords="offset points",
    #     xytext=(6, -11),
    #     ha="left",
    #     fontsize=7.5,
    #     color="#007a87",
    #     alpha=0.9,
    # )

# Grid layout calibration
plt.title(
    "Net Growth ie substracting world average (1991 - 2025)",
    fontsize=18,
    pad=25,
    fontweight="bold",
)
plt.xlabel("Year", fontsize=14, labelpad=12)
plt.ylabel(
    "Growth Rate Margin vs. World Baseline (Percentage Points)",
    fontsize=14,
    labelpad=12,
)

plt.xticks(years, rotation=45, fontsize=11)
plt.yticks(fontsize=11)
plt.xlim(1990, 2026)
plt.ylim(-8.5, 15.0)
plt.grid(True, linestyle=":", alpha=0.6)

# Render legend panel
plt.legend(
    loc="upper right",
    frameon=True,
    facecolor="white",
    edgecolor="#bbbbbb",
    shadow=True,
    fontsize=12,
)
plt.tight_layout()

# Display plot
plt.show()
