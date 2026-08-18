import matplotlib.pyplot as plt
import pandas as pd

# 1. Define dataset including Construction Workers
raw_monthly_inflation = [1225, 1776, 2266, 3430, 5022, 6554, 9188]
annual_gdp_pc_inr = [12161, 19863, 31179, 61709, 102351, 142330, 245617]
baseline = raw_monthly_inflation[0] / (annual_gdp_pc_inr[0] / 12)
data = {
    "Year": [1995, 2000, 2005, 2010, 2015, 2020, 2026],
    "House Maid / Cook": [550, 1000, 1850, 3750, 6000, 8000, 15750],
    "Private Driver": [1850, 3000, 4750, 7500, 11500, 15000, 24000],
    "Security Guard": [1500, 2600, 4000, 6250, 9750, 12000, 20750],
    "Janitor / Cleaner": [1000, 1750, 3000, 5250, 8000, 10000, 18000],
    "Construction Worker": [1100, 2000, 3200, 5800, 8500, 11000, 19500],
    "Core Inflation Curve": [round(x / baseline) for x in raw_monthly_inflation],
    "GDP Per Capita": [round(x / 12) for x in annual_gdp_pc_inr],
}
# print(data)
df = pd.DataFrame(data)

# 2. Setup the figure
plt.figure(figsize=(15, 9))

# Define styles for readability
professions = {
    "House Maid / Cook": {"marker": "o", "color": "#1f77b4"},
    "Private Driver": {"marker": "s", "color": "#ff7f0e"},
    "Security Guard": {"marker": "^", "color": "#2ca02c"},
    "Janitor / Cleaner": {"marker": "d", "color": "#9467bd"},
    "Construction Worker": {"marker": "v", "color": "#8c564b"},
}

# 3. Plot and annotate profession lines
for label, style in professions.items():
    plt.plot(
        df["Year"],
        df[label],
        marker=style["marker"],
        color=style["color"],
        linewidth=2,
        label=label,
    )

    # Annotate every single point on the line
    print(label)
    for x, y in zip(df["Year"], df[label]):
        # print(x, y)
        if "Maid" in label and x <= 2005:
            plt.annotate(
                f"₹{y:,}",
                xy=(x, y),
                textcoords="offset points",
                xytext=(0, -14),
                ha="center",
                fontsize=8,
                fontweight="semibold",
                color=style["color"],
            )
        else:
            plt.annotate(
                f"₹{y:,}",
                xy=(x, y),
                textcoords="offset points",
                xytext=(0, 8),
                ha="center",
                fontsize=8,
                fontweight="semibold",
                color=style["color"],
            )

# 4. Plot and annotate the Inflation Line
plt.plot(
    df["Year"],
    df["Core Inflation Curve"],
    color="red",
    linestyle="--",
    linewidth=3,
    label="Core Inflation Curve (Base Indexed)",
)
for x, y in zip(df["Year"], df["Core Inflation Curve"]):
    plt.annotate(
        f"₹{y:,}",
        xy=(x, y),
        textcoords="offset points",
        xytext=(0, -12),
        ha="center",
        fontsize=8,
        color="red",
    )

# 5. Plot and annotate the Inflation Line
plt.plot(
    df["Year"],
    df["GDP Per Capita"],
    color="red",
    linestyle="--",
    linewidth=3,
    label="GDP Per Capita(INR)",
)
for x, y in zip(df["Year"], df["GDP Per Capita"]):
    plt.annotate(
        f"₹{y:,}",
        xy=(x, y),
        textcoords="offset points",
        xytext=(0, -12),
        ha="center",
        fontsize=8,
        color="green",
    )

# 6. Final Chart Formatting
plt.title(
    "30-Year Trend of Mean Indian Labor Wages vs. Inflation (1995 - 2026)",
    fontsize=16,
    fontweight="bold",
    pad=20,
)

# plt.xscale("log")
plt.yscale("log")

plt.xlabel("Year", fontsize=12, fontweight="bold")
plt.ylabel("Average Monthly Salary / Scaled Cost (INR)", fontsize=12, fontweight="bold")
plt.xticks(df["Year"])
plt.grid(True, linestyle=":", alpha=0.5)
plt.legend(fontsize=11, loc="upper left")

# Adjust layout to prevent text clipping
plt.tight_layout()
plt.ylim(0, 27000)

# 6. Render the plot
plt.show()
