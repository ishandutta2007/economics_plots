import matplotlib.pyplot as plt

# Data from Statistics Canada Census reviews
years = [2001, 2006, 2011, 2016, 2021]
chinese_share = [17.6, 18.2, 18.7, 19.6, 19.6]
south_asian_share = [8.4, 9.9, 11.1, 12.0, 14.2]

# Create the figure and plot lines
plt.figure(figsize=(9, 5.5))
plt.plot(
    years,
    chinese_share,
    marker="o",
    color="#d62728",
    linewidth=2.5,
    label="Chinese Population Share",
)
plt.plot(
    years,
    south_asian_share,
    marker="s",
    color="#ff7f0e",
    linewidth=2.5,
    label="South Asian / Indian Subcontinent",
)

# Customizing plot visuals
plt.title(
    "Demographic Growth Trends in Metro Vancouver (2001–2021)",
    fontsize=14,
    fontweight="bold",
    pad=15,
)
plt.xlabel("Census Year", fontsize=12, labelpad=10)
plt.ylabel("Percentage of Total Metro Population (%)", fontsize=12, labelpad=10)
plt.xticks(years)
plt.ylim(0, 25)
plt.grid(True, linestyle="--", alpha=0.5)

# Adding data labels to points
for x, y in zip(years, chinese_share):
    plt.text(x, y + 0.6, f"{y}%", ha="center", fontweight="semibold", color="#d62728")
for x, y in zip(years, south_asian_share):
    plt.text(x, y - 1.2, f"{y}%", ha="center", fontweight="semibold", color="#ff7f0e")

plt.legend(loc="upper left", frameon=True, shadow=True, facecolor="white")
plt.tight_layout()

# Show plot
plt.show()
