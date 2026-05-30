import matplotlib.pyplot as plt
import pandas as pd

# Data representing valuations in Billions USD
data = {
    "Timeline": [
        "Jan 2023",
        "Oct 2023",
        "Feb 2024",
        "Oct 2024",
        "Mar 2025",
        "Sep 2025",
        "May 2026",
    ],
    "OpenAI_Valuation": [29, 86, 80, 157, 310, 550, 850],
    "Anthropic_Valuation": [4, 18, 18, 40, 150, 480, 1200],
}

df = pd.DataFrame(data)

plt.figure(figsize=(12, 7))
plt.plot(
    df["Timeline"],
    df["OpenAI_Valuation"],
    marker="o",
    label="OpenAI",
    color="#74aa9c",
    linewidth=2.5,
)
plt.plot(
    df["Timeline"],
    df["Anthropic_Valuation"],
    marker="s",
    label="Anthropic",
    color="#da7756",
    linewidth=2.5,
)

# Annotating OpenAI points
for i, txt in enumerate(df["OpenAI_Valuation"]):
    plt.annotate(
        f"${txt}B",
        (df["Timeline"][i], df["OpenAI_Valuation"][i]),
        textcoords="offset points",
        xytext=(0, 10),
        ha="center",
        fontsize=9,
    )

# Annotating Anthropic points
for i, txt in enumerate(df["Anthropic_Valuation"]):
    val_label = f"${txt}B" if txt < 1000 else f"${txt / 1000}T"
    plt.annotate(
        val_label,
        (df["Timeline"][i], df["Anthropic_Valuation"][i]),
        textcoords="offset points",
        xytext=(0, -15),
        ha="center",
        fontsize=9,
    )

plt.title(
    "Valuation Trajectory: OpenAI vs. Anthropic (2023-2026)",
    fontsize=14,
    fontweight="bold",
    pad=20,
)
plt.ylabel("Valuation ($ Billions USD)", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()
