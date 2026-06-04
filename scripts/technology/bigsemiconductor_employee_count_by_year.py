import matplotlib.pyplot as plt
import pandas as pd

# Semi-conductor headcount data (2020-2025)
data = {
    "Year": [2020, 2021, 2022, 2023, 2024, 2025],
    "Nvidia": [13775, 18975, 22473, 26196, 29600, 36000],
    # 'Qualcomm': [41000, 45000, 51000, 50000, 49000, 52000],
    "Broadcom": [21000, 20000, 20000, 20000, 37000, 33000],
    "AMD": [12600, 15500, 25000, 26000, 28000, 28000],
    "ASML": [28000, 32016, 39086, 42416, 42790, 45000],
}
company_list = list(data.keys())[1:]
df = pd.DataFrame(data)

# Styling the plot
plt.figure(figsize=(12, 8))
plt.style.use("seaborn-v0_8-muted")

for company in company_list:
    plt.plot(df["Year"], df[company], marker="s", label=company, linewidth=2.5)

plt.title("Semiconductor Global Headcount Trends (2020–2025)", fontsize=16)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Total Full-Time Employees", fontsize=12)
plt.legend(title="Company", loc="upper left")
plt.grid(True, linestyle=":", alpha=0.6)

# Display raw numbers on markers for clarity
for col in df.columns[1:]:
    for x, y in zip(df["Year"], df[col]):
        plt.text(x, y + 500, f"{int(y / 1000)}k", ha="center", fontsize=9)

plt.tight_layout()
plt.show()
