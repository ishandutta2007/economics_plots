import matplotlib.pyplot as plt
import pandas as pd

# Expanded dataset with 50+ countries representing all regions and wealth levels
data = {
    "Country": [
        "Monaco",
        "Singapore",
        "Hong Kong",
        "USA",
        "Norway",
        "Australia",
        "Canada",
        "India",
        "Bangladesh",
        "Nigeria",
        "Japan",
        "Germany",
        "Luxembourg",
        "Ireland",
        "Switzerland",
        "Qatar",
        "Iceland",
        "Denmark",
        "Netherlands",
        "Sweden",
        "Finland",
        "Austria",
        "Belgium",
        "Israel",
        "France",
        "UK",
        "New Zealand",
        "Italy",
        "Korea (South)",
        "Spain",
        "China",
        "Brazil",
        "Mexico",
        "Indonesia",
        "Turkey",
        "Saudi Arabia",
        "South Africa",
        "Egypt",
        "Vietnam",
        "Pakistan",
        "Ethiopia",
        "Philippines",
        "Thailand",
        "Russia",
        "Argentina",
        "Chile",
        "Colombia",
        "Malaysia",
        "Kazakhstan",
        "Mongolia",
        "Iceland",
    ],
    "Density": [
        26000,
        8000,
        7100,
        36,
        15,
        3.3,
        4,
        480,
        1300,
        230,
        340,
        240,
        260,
        72,
        215,
        248,
        3.6,
        137,
        508,
        25,
        18,
        109,
        383,
        420,
        119,
        277,
        19,
        205,
        530,
        94,
        153,
        25,
        66,
        151,
        110,
        16,
        49,
        105,
        315,
        310,
        115,
        368,
        135,
        9,
        16,
        26,
        46,
        99,
        7,
        2,
        3.6,
    ],
    "GDP_Per_Capita": [
        234000,
        82000,
        49000,
        76000,
        106000,
        65000,
        52000,
        2400,
        2700,
        2200,
        34000,
        48000,
        126000,
        104000,
        92000,
        88000,
        75000,
        67000,
        56000,
        56000,
        50000,
        52000,
        51000,
        54000,
        41000,
        45000,
        48000,
        34000,
        32000,
        30000,
        12700,
        8900,
        11000,
        4700,
        10600,
        30000,
        6700,
        4300,
        4100,
        1600,
        1000,
        3600,
        7000,
        12000,
        13000,
        15000,
        6600,
        12000,
        11000,
        1900,
        75000,
    ],
}

df = pd.DataFrame(data)

# Create the plot
plt.figure(figsize=(15, 9))
plt.scatter(
    df["Density"],
    df["GDP_Per_Capita"],
    color="darkcyan",
    s=100,
    alpha=0.7,
    edgecolors="white",
)

# Label countries (using a loop to avoid overcrowding for every single point)
# Labels extreme cases or major economies for clarity
for i, txt in enumerate(df["Country"]):
    if (
        df["Density"][i] > 5000
        or df["Density"][i] < 10
        or df["GDP_Per_Capita"][i] > 80000
        or i % 3 == 0
    ):
        plt.annotate(
            txt,
            (df["Density"][i], df["GDP_Per_Capita"][i]),
            xytext=(5, 5),
            textcoords="offset points",
            fontsize=8,
            alpha=0.8,
        )

# Logarithmic scaling remains vital
plt.xscale("log")
plt.yscale("log")

# Layout and labels
plt.title(
    "Global Overview: Population Density vs. GDP per Capita (Log-Log Scale)",
    fontsize=16,
    fontweight="bold",
)
plt.xlabel("Population Density (People per sq km)", fontsize=12)
plt.ylabel("GDP per Capita (USD)", fontsize=12)
plt.grid(True, which="both", linestyle=":", alpha=0.5)

# Visual anchors for interpretation
plt.axvspan(0.1, 10, color="gray", alpha=0.1, label="Sparsely Populated")
plt.axhspan(50000, 250000, color="gold", alpha=0.1, label="High Income")

plt.tight_layout()
plt.show()
