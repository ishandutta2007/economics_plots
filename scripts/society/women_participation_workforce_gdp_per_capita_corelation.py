import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Data from the research
data = {
    "Country": [
        "Argentina",
        "Australia",
        "Brazil",
        "Canada",
        "China",
        "France",
        "Germany",
        "India",
        "Indonesia",
        "Italy",
        "Japan",
        "Mexico",
        "Russia",
        "Saudi Arabia",
        "South Africa",
        "South Korea",
        "Turkey",
        "United Kingdom",
        "United States",
    ],  # 'European Union'],
    "Female Labor Force Participation Rate (%)": [
        52.9,
        62.4,
        53.0,
        61.0,
        59.6,
        51.7,
        55.6,
        32.8,
        52.6,
        41.3,
        55.3,
        47.4,
        54.5,
        36.2,
        53.0,
        56.0,
        36.3,
        57.3,
        56.1,
    ],  # 70.2],
    "GDP per capita (USD)": [
        14362,
        64547,
        9964,
        53558,
        13687,
        46792,
        55911,
        2880,
        5026,
        41091,
        33956,
        12692,
        14258,
        30099,
        6397,
        34642,
        16709,
        54949,
        89105,
    ],  # , 64545]
}

df = pd.DataFrame(data)

# Create the scatter plot
plt.figure(figsize=(14, 10))
sns.scatterplot(
    data=df,
    x="GDP per capita (USD)",
    y="Female Labor Force Participation Rate (%)",
    s=100,
)

# Add the trend line using regplot, but without the scatter points
sns.regplot(
    data=df,
    x="GDP per capita (USD)",
    y="Female Labor Force Participation Rate (%)",
    scatter=False,
    color="blue",
)

# Add labels for each point with a larger font size
for i in range(df.shape[0]):
    plt.text(
        df["GDP per capita (USD)"][i] + 0.5,
        df["Female Labor Force Participation Rate (%)"][i] + 0.5,
        df["Country"][i],
        fontsize=11,
    )

# Set the title and labels with a larger font size
plt.title(
    "Correlation between Women's Workforce Participation and GDP per Capita in G20 Countries",
    fontsize=16,
)
plt.xlabel("GDP per capita (USD)", fontsize=14)
plt.ylabel("Female Labor Force Participation Rate (%)", fontsize=14)

# Calculate and display the correlation coefficient
correlation = df["GDP per capita (USD)"].corr(
    df["Female Labor Force Participation Rate (%)"]
)
plt.figtext(
    0.5,
    0.01,
    f"Correlation coefficient: {correlation:.2f}",
    ha="center",
    fontsize=14,
    bbox={"facecolor": "orange", "alpha": 0.5, "pad": 5},
)

plt.grid(True)
plt.savefig("g20_correlation_plot_with_trendline.png")
