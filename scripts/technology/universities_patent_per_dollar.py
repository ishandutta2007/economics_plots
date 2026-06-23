import pandas as pd
import matplotlib.pyplot as plt

# Data from the table
data = {
    "University": [
        "MIT",
        "Stanford",
        "Oxford",
        "Cambridge",
        "Harvard",
        "Caltech",
        "IIT Madras"
    ],
    "Patents_Granted_2024": [362, 199, 34, 294, 155, 164, 435],
    "Research_Grants_USD_M": [2100, 2200, 1039, 735, 1020, 490.7, 61]
}

df = pd.DataFrame(data)

# Patents granted per $1 million of research grants
df["Universities_Patent_Per_Dollar"] = (
    df["Patents_Granted_2024"] / df["Research_Grants_USD_M"]
)

# Sort for better visualization
df = df.sort_values(
    "Universities_Patent_Per_Dollar",
    ascending=False
)

# Plot
plt.figure(figsize=(10, 6))
bars = plt.bar(
    df["University"],
    df["Universities_Patent_Per_Dollar"]
)

plt.title("Patents Granted per $1 Million Research Grant (2024)")
plt.ylabel("Patents per $1M Research Funding")
plt.xlabel("University")

# Value labels
for bar, value in zip(bars, df["Universities_Patent_Per_Dollar"]):
    plt.text(
        bar.get_x() + bar.get_width()/2,
        value,
        f"{value:.2f}",
        ha="center",
        va="bottom"
    )

plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.show()

# Optional: print exact values
print(
    df[["University", "Universities_Patent_Per_Dollar"]]
    .to_string(index=False)
)
