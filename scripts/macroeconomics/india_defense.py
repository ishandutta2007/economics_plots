import matplotlib.pyplot as plt
import seaborn as sns

# 1. Prepare Dataset
years = [
    "2011-12",
    "2012-13",
    "2013-14",
    "2014-15",
    "2015-16",
    "2016-17",
    "2017-18",
    "2018-19",
    "2019-20",
    "2020-21",
    "2021-22",
    "2022-23",
    "2023-24",
    "2024-25",
    "2025-26",
]
exports_in_crores = [
    500,
    600,
    686,
    1940,
    2059,
    1521,
    4682,
    10745,
    9115,
    8434,
    12814,
    15920,
    21083,
    23622,
    38424,
]

# 2. Configure Aesthetics
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 6))

# 3. Create Plots
plt.plot(
    years,
    exports_in_crores,
    marker="o",
    color="#003366",
    linewidth=2.5,
    label="Export Value Line",
)
# (years, exports_in_crores, color='#4682B4', alpha=0.6, width=0.6, label="Yearly Volume")

# 4. Custom Labels and Details
plt.title(
    "India's Year-on-Year Defense Exports Growth (FY 2012 - FY 2026)",
    fontsize=14,
    fontweight="bold",
    pad=15,
)
plt.xlabel("Financial Year", fontsize=12, labelpad=10)
plt.ylabel("Export Value (₹ in Crores)", fontsize=12, labelpad=10)
plt.xticks(rotation=45)

# 5. Highlight Peak and Benchmarks
for i, val in enumerate(exports_in_crores):
    if i in [2, 7, 14]:  # Label FY14, FY19, and FY26
        plt.text(
            i, val + 1000, f"₹{val:,}", ha="center", fontweight="bold", color="black"
        )

plt.tight_layout()
plt.legend(loc="upper left")
plt.show()
