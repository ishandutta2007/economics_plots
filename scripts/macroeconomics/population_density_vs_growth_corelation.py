import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import linregress

###############################################################################
# SETTINGS
###############################################################################

START_YEAR = "1990"
END_YEAR = "2024"

POP_FILE = "API_SP.POP.TOTL_DS2_en_csv_v2.csv"
GDP_FILE = "API_NY.GDP.PCAP.KD_DS2_en_csv_v2.csv"
LAND_FILE = "API_AG.LND.TOTL.K2_DS2_en_csv_v2.csv"

###############################################################################
# LOAD WORLD BANK FILES
###############################################################################

def load_indicator(filename):

    df = pd.read_csv(filename, skiprows=4)

    keep = [
        "Country Name",
        "Country Code",
        START_YEAR,
        END_YEAR
    ]

    if filename == LAND_FILE:
        keep = [
            "Country Name",
            "Country Code",
            END_YEAR
        ]

    return df[keep]

pop = load_indicator(POP_FILE)
gdp = load_indicator(GDP_FILE)
land = load_indicator(LAND_FILE)

###############################################################################
# MERGE
###############################################################################

df = pop.merge(
    gdp,
    on=["Country Name", "Country Code"],
    suffixes=("_POP", "_GDP")
)

df = df.merge(
    land,
    on=["Country Name", "Country Code"]
)

df.rename(columns={
    END_YEAR: "LandArea"
}, inplace=True)

###############################################################################
# CLEAN
###############################################################################

df = df.rename(columns={
    START_YEAR + "_POP":"Pop1990",
    END_YEAR + "_POP":"Pop2024",
    START_YEAR + "_GDP":"GDP1990",
    END_YEAR + "_GDP":"GDP2024"
})

df = df[
    [
        "Country Name",
        "Country Code",
        "Pop1990",
        "Pop2024",
        "GDP1990",
        "GDP2024",
        "LandArea"
    ]
]

df = df.dropna()

###############################################################################
# COMPUTE VARIABLES
###############################################################################

df["Density"] = df["Pop2024"] / df["LandArea"]

df["Growth"] = (
    (df["GDP2024"] - df["GDP1990"])
    / df["GDP1990"]
    * 100
)

###############################################################################
# REMOVE MICROSTATES
###############################################################################

df = df[df["LandArea"] > 1000]
df = df[df["Pop2024"] > 1000000]

###############################################################################
# POPULATION BANDS
###############################################################################

bands = [

    ("5-15M",5e6,15e6),

    ("15-30M",15e6,30e6),

    ("30-60M",30e6,60e6),

    ("60-120M",60e6,120e6),

    ("120-250M",120e6,250e6)

]

###############################################################################
# PLOTTING
###############################################################################

fig, axes = plt.subplots(
    3,
    2,
    figsize=(14,15)
)

axes = axes.flatten()

summary = []

for ax,(label,low,high) in zip(axes,bands):

    sub = df[
        (df.Pop2024>=low)
        &
        (df.Pop2024<high)
    ]

    if len(sub)<5:
        continue

    x = np.log10(sub["Density"])
    y = sub["Growth"]

    result = linregress(x,y)

    summary.append({

        "Band":label,

        "Countries":len(sub),

        "r":result.rvalue,

        "R2":result.rvalue**2,

        "p":result.pvalue

    })

    ax.scatter(
        x,
        y,
        s=50
    )

    xs = np.linspace(
        x.min(),
        x.max(),
        100
    )

    ys = result.intercept + result.slope*xs

    ax.plot(xs,ys)

    ax.set_title(
        f"{label}\n"
        f"r={result.rvalue:.2f}, "
        f"R²={result.rvalue**2:.2f}"
    )

    ax.set_xlabel("log10(Population Density)")
    ax.set_ylabel("GDP per capita Growth (%)")

    for _,row in sub.iterrows():

        ax.text(
            np.log10(row["Density"]),
            row["Growth"],
            row["Country Code"],
            fontsize=7
        )

plt.tight_layout()

plt.savefig(
    "population_density_vs_growth.png",
    dpi=300
)

plt.show()

###############################################################################
# SUMMARY TABLE
###############################################################################

summary = pd.DataFrame(summary)

print("\nRegression Results\n")
print(summary)

summary.to_csv(
    "density_regression_summary.csv",
    index=False
)

###############################################################################
# SAVE PROCESSED DATA
###############################################################################

df.to_csv(
    "processed_country_data.csv",
    index=False
)