import matplotlib.pyplot as plt
import pandas as pd

# Revenue values in Millions of USD (Estimates based on industry reports/ARR)
data = {
    "Year": [2021, 2022, 2023, 2024, 2025],
    "OpenAI": [28, 200, 1600, 3700, 13000],  # Scaling post-GPT-3 and ChatGPT launch
    "Anthropic": [None, 10, 100, 1000, 9000],  # Rapid enterprise growth with Claude
    "Perplexity": [None, None, 10, 80, 148],  # Growth in AI-native search
    "xAI (Grok)": [None, None, None, 100, 500],  # Standalone estimated revenue
    "DeepSeek": [None, None, None, 50, 460],  # Rise in 2025 via API efficiency
    "MoonshotAI": [None, None, None, 20, 240],  # Rise in 2025 via API efficiency
}

df = pd.DataFrame(data)

# Define brand colors for better visual distinction
colors = {
    "OpenAI": "#00A67E",
    "Anthropic": "#D97757",
    "Perplexity": "#20B2AA",
    "xAI (Grok)": "#333333",
    "DeepSeek": "#4169E1",
    "MoonshotAI": "#2969AA",
}

print(colors.keys())

plt.figure(figsize=(14, 8))

for company in colors.keys():
    # Drop None values for plotting each individual curve
    subset = df[["Year", company]].dropna()
    plt.plot(
        subset["Year"],
        subset[company],
        marker="o",
        label=company,
        linewidth=2.5,
        color=colors[company],
    )

    # Annotate points
    for x, y in zip(subset["Year"], subset[company]):
        # Format label: $B for Billions, $M for Millions
        label = f"${y / 1000:.1g}B" if y >= 1000 else f"${int(y)}M"
        plt.annotate(
            label,
            (x, y),
            textcoords="offset points",
            xytext=(0, 12),
            ha="center",
            fontsize=10,
            fontweight="bold",
            color=colors[company],
        )

# Set Y-axis to Log Scale to make different orders of magnitude readable
plt.yscale("log")

# Customizing the Chart
plt.title(
    "Estimated Revenue Growth of Major AI Companies (2021 - 2025)",
    fontsize=18,
    pad=20,
    fontweight="bold",
)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Annual Revenue (Millions USD - Log Scale)", fontsize=14)
plt.xticks([2021, 2022, 2023, 2024, 2025], fontsize=12)

# Custom Y-ticks for log scale readability
plt.yticks([10, 100, 1000, 10000], ["$10M", "$100M", "$1B", "$10B"], fontsize=12)

plt.grid(True, which="both", linestyle="--", alpha=0.5)
plt.legend(fontsize=12, loc="upper left", frameon=True, shadow=True)

# Contextual Note
plt.figtext(
    0.5,
    0.01,
    "Note: Values for 2024/2025 are estimates/run-rate projections. Logarithmic scale used for visual clarity.",
    ha="center",
    fontsize=10,
    bbox={"facecolor": "orange", "alpha": 0.1, "pad": 5},
)

plt.tight_layout()
plt.savefig("ai_revenue_comparison.png")
plt.show()
