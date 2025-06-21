import pandas as pd
import matplotlib.pyplot as plt

# Sample data for demonstration purposes
years = list(range(1995, 2025))
west_europe_gdp = [25000 + i * 500 for i in range(30)]  # Simulated data
east_europe_gdp = [8000 + i * 600 for i in range(30)]  # Simulated data

# Create a DataFrame
df = pd.DataFrame(
    {
        "Year": years,
        "Western Europe": west_europe_gdp,
        "Eastern Europe": east_europe_gdp,
    }
)

# Calculate growth ratios
west_growth_ratio = df["Western Europe"].iloc[-1] / df["Western Europe"].iloc[0]
east_growth_ratio = df["Eastern Europe"].iloc[-1] / df["Eastern Europe"].iloc[0]

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(df["Year"], df["Western Europe"], label="Western Europe", color="blue")
plt.plot(df["Year"], df["Eastern Europe"], label="Eastern Europe", color="green")

# Annotate oldest values
plt.text(
    df["Year"].iloc[0],
    df["Western Europe"].iloc[0],
    f"Western Europe ({df['Western Europe'].iloc[0]:,.0f})",
    fontsize=9,
    va="top",
    ha="left",
)
plt.text(
    df["Year"].iloc[0],
    df["Eastern Europe"].iloc[0],
    f"Eastern Europe ({df['Eastern Europe'].iloc[0]:,.0f})",
    fontsize=9,
    va="top",
    ha="left",
)

# Annotate latest values
plt.text(
    df["Year"].iloc[-1],
    df["Western Europe"].iloc[-1],
    f"Western Europe ({df['Western Europe'].iloc[-1]:,.0f})",
    fontsize=9,
    va="bottom",
    ha="right",
)
plt.text(
    df["Year"].iloc[-1],
    df["Eastern Europe"].iloc[-1],
    f"Eastern Europe ({df['Eastern Europe'].iloc[-1]:,.0f})",
    fontsize=9,
    va="bottom",
    ha="right",
)

# Annotate growth ratios
mid_index = len(df) // 2
plt.text(
    df["Year"].iloc[mid_index],
    df["Western Europe"].iloc[mid_index] * 1.05,
    f"{west_growth_ratio:.2f}x",
    color="blue",
    fontsize=9,
)
plt.text(
    df["Year"].iloc[mid_index],
    df["Eastern Europe"].iloc[mid_index] * 0.95,
    f"{east_growth_ratio:.2f}x",
    color="green",
    fontsize=9,
)

# Formatting
plt.title("GDP per Capita Comparison: Western vs Eastern Europe (1995–2024)")
plt.xlabel("Year")
plt.ylabel("GDP per capita (current US$)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
