import matplotlib.pyplot as plt

# Data
countries = ["Canada", "Australia", "Russia", "United States", "India"]
reserves = [853, 753, 516, 131, 3]  # in thousands of dollars

# Create horizontal bar chart
plt.figure(figsize=(10, 6))
bars = plt.barh(
    countries, reserves, color=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]
)

# Add value labels
for bar in bars:
    width = bar.get_width()
    plt.text(
        width * 1.05,
        bar.get_y() + bar.get_height() / 2,
        f"${int(width)}K",
        va="center",
        ha="left",
        fontsize=10,
    )

# Use logarithmic scale for better visualization
# plt.xscale('log')
plt.xlim(1, 1000)  # Set limits for log scale

# Add labels and title
plt.xlabel("Value (Thousands of USD)", fontsize=12)
plt.title("Natural Resource Reserves Per Capita Comparison", fontsize=14, pad=20)
plt.grid(axis="x", linestyle="--", alpha=0.7)

# Add footnote
plt.figtext(
    0.5,
    0.01,
    "Note: Values represent total estimated reserve per capita value in thousands of USD",
    ha="center",
    fontsize=9,
    style="italic",
)

plt.tight_layout()
plt.show()
