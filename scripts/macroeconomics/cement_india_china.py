import matplotlib.pyplot as plt
import pandas as pd

# 1. Prepare the historical and projected dataset
data = {
    "Year": list(range(2000, 2048)),
    "China": [
        # Historical (2000–2025)
        597, 661, 725, 862, 970, 1060, 1240, 1360, 1400, 1650, 1880, 2060, 2180, 2420, 2490,
        2360, 2403, 2320, 2180, 2330, 2395, 2377, 2135, 2020, 1950, 1900,
        # Projected (2026–2047): continued structural decline as economy matures
        1830, 1680, 1540, 1410, 1280, 1150,
        1040, 960, 900, 850, 810, 780, 755, 730, 710, 690, 670, 655, 645, 635, 628, 620
    ],
    "India": [
        # Historical (2000–2025)
        94, 100, 114, 118, 125, 136, 151, 165, 181, 198, 211, 223, 235, 254, 270,
        272, 280, 298, 328, 335, 334, 300, 360, 391, 426, 453,
        # Projected (2026–2047): robust growth driven by urbanisation & infrastructure
        487, 525, 567, 612, 660, 694,
        740, 790, 845, 900, 955, 1010, 1060, 1105, 1150, 1190, 1225, 1255, 1280, 1300, 1312, 1320
    ]
}

df = pd.DataFrame(data)

# Split data into Historical (up to 2025) and Projected (2025 onwards)
# 2025 acts as the bridge connecting both plot lines smoothly
df_hist = df[df["Year"] <= 2025]
df_proj = df[df["Year"] >= 2025]

# 2. Set up the plotting environment
plt.figure(figsize=(24, 11), dpi=100)
plt.grid(True, linestyle="--", alpha=0.5)

# 3. Plot China's lines (Historical = Solid, Projected = Dotted)
plt.plot(df_hist["Year"], df_hist["China"], color="#de2d26", linestyle="-", linewidth=2.5, label="China (Historical)")
plt.plot(df_proj["Year"], df_proj["China"], color="#de2d26", linestyle=":", linewidth=2.5, label="China (Projected)")
plt.scatter(df["Year"], df["China"], color="#de2d26", s=30, zorder=5)

# 4. Plot India's lines (Historical = Solid, Projected = Dotted)
plt.plot(df_hist["Year"], df_hist["India"], color="#1f77b4", linestyle="-", linewidth=2.5, label="India (Historical)")
plt.plot(df_proj["Year"], df_proj["India"], color="#1f77b4", linestyle=":", linewidth=2.5, label="India (Projected)")
plt.scatter(df["Year"], df["India"], color="#1f77b4", s=30, zorder=5)

# 5. Annotate every data point (Alternating offsets prevent overlapping)
for idx, row in df.iterrows():
    year = row["Year"]
    china_val = row["China"]
    india_val = row["India"]
    
    # China labels: Alternates slightly up and down to manage tight spacing
    c_offset = 15 if idx % 2 == 0 else -25
    plt.annotate(
        f"{int(china_val)}", 
        (year, china_val), 
        textcoords="offset points", 
        xytext=(0, c_offset), 
        ha='center', 
        fontsize=7, 
        color="#a50f15",
        weight="bold" if year in [2014, 2047] else "normal"
    )
    
    # India labels: Alternates slightly up and down
    i_offset = 15 if idx % 2 == 0 else -22
    plt.annotate(
        f"{int(india_val)}", 
        (year, india_val), 
        textcoords="offset points", 
        xytext=(0, i_offset), 
        ha='center', 
        fontsize=7, 
        color="#08519c",
        weight="bold" if year in [2000, 2047] else "normal"
    )

# 6. Customize graph aesthetics
plt.title("Cement Consumption Trajectory: China vs. India (2000–2047)", fontsize=16, pad=20, weight="bold")
plt.xlabel("Year", fontsize=12, labelpad=10)
plt.ylabel("Volume (Million Metric Tonnes - MMT)", fontsize=12, labelpad=10)

plt.xticks(df["Year"], rotation=45, fontsize=9)
plt.yticks(range(0, 2800, 200), fontsize=10)
plt.xlim(1999, 2048)
plt.ylim(-50, 2650)

# Add a vertical structural marker dividing history and projection
plt.axvline(x=2025, color="gray", linestyle="-.", alpha=0.7, linewidth=1.5)
plt.text(2024.3, 2550, "Forecast Zone ➔", fontsize=11, color="gray", style="italic", weight="bold")

# Display the legend cleanly
plt.legend(loc="upper left", fontsize=11, frameon=True, shadow=True)
plt.tight_layout()

# Save or show the plot
#plt.savefig("cement_consumption_trends.png", bbox_inches='tight')
plt.show()
