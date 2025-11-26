import matplotlib.pyplot as plt

# Data (source: World Bank 2023 estimates)
countries = ["Kazakhstan", "Argentina", "India"]
population = [19.62, 45.81, 1428]

# Create horizontal bar chart
plt.figure(figsize=(10, 5))
bars = plt.barh(countries, population, color=["#FF9933", "#75AADB", "#00AFCA"])

# Add value labels
for bar in bars:
    width = bar.get_width()
    plt.text(
        width * 1.01,
        bar.get_y() + bar.get_height() / 2,
        f"{width:.2f}M",
        va="center",
        ha="left",
        fontsize=11,
    )

# Adjust x-axis to show population difference clearly
plt.xlim(0, 1500)  # India's population is much larger

# Add labels and title
plt.xlabel("Population (Millions)", fontsize=12)
plt.title(
    "Similar Sized Country Population Comparison (2023 Estimates)", fontsize=14, pad=20
)
plt.grid(axis="x", linestyle="--", alpha=0.7)

# Add footnote
plt.figtext(
    0.5,
    0.01,
    "Source: World Bank 2023 estimates",
    ha="center",
    fontsize=9,
    style="italic",
)

plt.tight_layout()
plt.show()
