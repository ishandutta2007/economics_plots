import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# --- Data Preparation ---
# Data gathered from the most recent available sources as of late 2024.
# - US data for racial groups is from the US Census Bureau's American Community Survey (2022/2023).
# - India data is an estimation based on the Periodic Labour Force Survey (2022-23), converted to USD.
# - China data is the median per capita disposable income from the National Bureau of Statistics of China (2023), converted to USD.
#   Note: The China data is 'per capita', while others are 'household', which is a significant distinction.

data = {
    "Category": [
        "Indian American",
        "Chinese American",
        "White American",
        "China",
        "India",
    ],
    "Median Income (USD)": [
        152341,  # Source: 2022 ACS
        101728,  # Source: 2022 ACS
        89050,  # Source: 2023 Current Population Survey
        4557,  # Source: NBS of China (2023), converted from 33,036 CNY
        1961,  # Source: Estimated from PLFS (2022-23), converted from ~162,732 INR
    ],
}

df = pd.DataFrame(data)

# Sort the dataframe by income for better visualization
df_sorted = df.sort_values("Median Income (USD)", ascending=True)

# --- Plotting ---
# Create the figure and axes objects
fig, ax = plt.subplots(figsize=(12, 8))

# Create horizontal bars
bars = ax.barh(
    df_sorted["Category"],
    df_sorted["Median Income (USD)"],
    color=["#FF9999", "#66B2FF", "#99FF99", "#FFCC99", "#C2B280"],
)

# --- Formatting and Styling ---
# Set the title and labels
ax.set_title(
    "Median Household Income Comparison (Most Recent Data)", fontsize=16, pad=20
)
ax.set_xlabel("Median Income (USD)", fontsize=12)
ax.set_ylabel("")  # No label for y-axis as categories are clear

# Format the x-axis to show dollar signs and commas
formatter = mticker.FuncFormatter(lambda x, p: f"${x:,.0f}")
ax.xaxis.set_major_formatter(formatter)

# Remove the top and right spines for a cleaner look
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)  # Hide y-axis spine

# Add data labels at the end of each bar
for bar in bars:
    width = bar.get_width()
    label_x_pos = width + (
        ax.get_xlim()[1] * 0.01
    )  # Position label slightly after the bar
    ax.text(
        label_x_pos,
        bar.get_y() + bar.get_height() / 2,
        f"${width:,.0f}",
        va="center",
        ha="left",
        fontsize=10,
        color="black",
    )

# Add a footnote with data source information
footnote_text = (
    "Sources:\n"
    "- US Groups: US Census Bureau (2022 ACS / 2023 CPS).\n"
    "- India: Estimation from Periodic Labour Force Survey (2022-23).\n"
    "- China: National Bureau of Statistics of China (2023).\n\n"
    "*Note: Data for India is an estimate of household income. Data for China is per capita disposable income."
)
# **MODIFIED LINE:** Positioned the footnote inside the figure area.
fig.text(
    0.5, 0.01, footnote_text, ha="center", fontsize=9, style="italic", color="gray"
)


# Adjust layout to make room for labels and title
plt.tight_layout()
plt.subplots_adjust(left=0.15, bottom=0.25)

# Show the plot
plt.show()
