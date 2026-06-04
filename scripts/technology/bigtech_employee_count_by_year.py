import matplotlib.pyplot as plt
import pandas as pd

# Data based on official reported figures and 2025 projections
data = {
    "Year": [2020, 2021, 2022, 2023, 2024, 2025],
    # 'Amazon': [1298000, 1608000, 1541000, 1525000, 1556000, 1578000],
    "AmazonTech": [129800, 160800, 154100, 152500, 155600, 157800],
    "Microsoft": [163000, 181000, 221000, 221000, 228000, 228000],
    "Alphabet": [135301, 156500, 190234, 182502, 183323, 190167],
    "Apple": [147000, 154000, 164000, 161000, 164000, 166100],
    "Meta": [58604, 71970, 86482, 67317, 70799, 72000],
}
company_list = list(data.keys())[1:]

df = pd.DataFrame(data)

# Set the style
plt.style.use("ggplot")
fig, ax1 = plt.subplots(figsize=(12, 7))

# Amazon has a significantly larger scale, so we use a twin axis or separate logic
# For a clean 5-line comparison, we plot all on one but note the scale
for company in company_list:
    ax1.plot(df["Year"], df[company], marker="o", linewidth=2, label=company)

# Formatting the chart
ax1.set_title("Big Tech Global Headcount Trends (2020–2025)", fontsize=16, pad=20)
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Total Employees (Millions)", fontsize=12)
ax1.legend(loc="upper left", frameon=True)
ax1.grid(True, linestyle="--", alpha=0.7)

# Adjusting Y-axis to show millions for readability
ax1.get_yaxis().set_major_formatter(
    plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x)))
)

plt.tight_layout()
plt.show()
