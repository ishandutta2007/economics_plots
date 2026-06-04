import matplotlib.pyplot as plt

# --- Data ---
# Data for the USA is from the U.S. Social Security Administration's
# "National Average Wage Index" (AWI). This is an AVERAGE wage, not median.
# Source: https://www.ssa.gov/oact/cola/awiseries.html
#
# A consistent 35-year *median wage* series for India is not readily available.
# We are substituting India's "GDP per Capita (Current US$)" as a proxy
# to show economic growth over the same period.
# Source: Macrotrends, citing World Bank & IMF.
#
# *** NOTE THE DIFFERENT METRICS: US (Average Wage) vs. India (GDP per Capita) ***
years = [
    1990,
    1995,
    2000,
    2005,
    2010,
    2015,
    2020,
    # 2024 data for India GDP per capita is not yet finalized in this dataset
]

# US Average Wage Index (USD)
us_wages = [
    21027.98,  # 1990
    24705.66,  # 1995
    32154.82,  # 2000
    36952.94,  # 2005
    41673.83,  # 2010
    48098.63,  # 2015
    55628.60,  # 2020
    # 69846.57   # 2024 (Removed to match India data availability)
]

# India GDP per Capita (Current US$) - PROXY FOR WAGE
# Source: https://www.macrotrends.net/global-metrics/countries/IND/india/gdp-per-capita
india_gdp_per_capita = [
    371.09,  # 1990
    375.18,  # 1995
    442.75,  # 2000
    710.49,  # 2005
    1347.52,  # 2010
    1584.00,  # 2015
    1907.04,  # 2020
    # Data for 2024 not included to keep lists equal
]


# --- Plotting ---
def plot_comparison():
    """
    Plots the US Average Wage vs. India's GDP per Capita.
    """
    plt.figure(figsize=(12, 7))

    # --- Create two Y-axes ---
    # This is necessary because the scales are vastly different

    # Axis 1 (Left) for US Wages
    ax1 = plt.gca()  # get current axis
    ax1.plot(
        years,
        us_wages,
        label="USA (Average Wage Index)",
        marker="o",
        linestyle="-",
        color="blue",
    )
    ax1.set_xlabel("Year", fontsize=12)
    ax1.set_ylabel("USA Average Annual Wage (USD)", fontsize=12, color="blue")
    ax1.tick_params(axis="y", labelcolor="blue")
    ax1.set_ylim(bottom=0)

    # Axis 2 (Right) for India GDP per Capita
    ax2 = ax1.twinx()  # Create a second y-axis that shares the same x-axis
    ax2.plot(
        years,
        india_gdp_per_capita,
        label="India (GDP per Capita)",
        marker="s",
        linestyle="--",
        color="green",
    )
    ax2.set_ylabel("India GDP per Capita (USD)", fontsize=12, color="green")
    ax2.tick_params(axis="y", labelcolor="green")
    ax2.set_ylim(bottom=0)

    # --- Customize the Plot ---
    plt.title("US Average Wage vs. India GDP per Capita (1990-2020)", fontsize=16)

    # Add legends for both lines
    # We need to get the "handles" and "labels" from both axes and combine them
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(lines1 + lines2, labels1 + labels2, loc="upper left")

    ax1.grid(True, linestyle="--", alpha=0.6)  # Add grid (optional, can look busy)

    # Add a note about the data
    plt.figtext(
        0.5,
        0.01,
        "NOTE: Data for 'median wage' for India is not available. "
        "This chart uses 'GDP per Capita' as a proxy.",
        wrap=True,
        horizontalalignment="center",
        fontsize=8,
        color="gray",
    )

    # Display the plot
    plt.tight_layout(rect=[0, 0.05, 1, 1])  # Adjust layout to make room for note
    plt.show()


# --- Main execution ---
if __name__ == "__main__":
    # Check if matplotlib is installed
    try:
        import matplotlib
    except ImportError:
        print("Error: 'matplotlib' library not found.")
        print("Please install it by running: pip install matplotlib")
    else:
        plot_comparison()
