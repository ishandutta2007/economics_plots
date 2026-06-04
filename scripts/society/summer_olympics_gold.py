import matplotlib.pyplot as plt
import numpy as np

# Data provided in the table
games = ["Beijing 2008", "London 2012", "Rio 2016", "Tokyo 2020*", "Paris 2024"]
china_golds = [48, 38, 26, 38, 40]
usa_golds = [36, 46, 46, 39, 40]

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Set position and width for the bars
bar_width = 0.35
index = np.arange(len(games))

# Plotting the bars for China and USA
bar1 = ax.bar(index - bar_width / 2, china_golds, bar_width, label="China", color="red")
bar2 = ax.bar(index + bar_width / 2, usa_golds, bar_width, label="USA", color="blue")

# Adding labels, title, and legend
ax.set_xlabel("Olympic Games")
ax.set_ylabel("Number of Gold Medals")
ax.set_title("Gold Medals Comparison: China vs. USA (Last 5 Summer Olympics)")
ax.set_xticks(index)
ax.set_xticklabels(games, rotation=45, ha="right")
ax.legend()


# Function to add the value labels on top of the bars
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(
            f"{height}",
            xy=(bar.get_x() + bar.get_width() / 2, height),
            xytext=(0, 3),  # 3 points vertical offset
            textcoords="offset points",
            ha="center",
            va="bottom",
        )


add_labels(bar1)
add_labels(bar2)

# Adjust layout to prevent labels from being cut off
plt.tight_layout()

# Display the plot
plt.show()
