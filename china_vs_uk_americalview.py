import matplotlib.pyplot as plt
import numpy as np


def generate_china_uk_gdp_plot():
    """
    Generates data for a Matplotlib plot visualizing China/UK GDP convergence.
    """
    # --- Realistic Data & Projections ---
    # Data Sources: IMF WEO October 2025 estimates
    # Long-term growth projections based on various economic analyses

    current_gdp_china_ppp = 29191.0  # approx USD PPP
    current_gdp_uk_ppp = 63760.0  # approx USD PPP
    china_growth_rate = (
        0.040  # 4.0% average annual growth in real GDP per capita (long-term estimate)
    )
    uk_growth_rate = (
        0.009  # 0.9% average annual growth in real GDP per capita (long-term estimate)
    )
    start_year = 2025

    # Calculate convergence year (around 2051 based on these rates)
    # The script logic calculates the exact convergence point
    years_to_converge = round(
        np.log(current_gdp_uk_ppp / current_gdp_china_ppp)
        / np.log((1 + china_growth_rate) / (1 + uk_growth_rate))
    )
    convergence_year = start_year + years_to_converge

    total_years = years_to_converge + 10  # Extend plot a bit past convergence
    years = np.arange(start_year, start_year + total_years)
    gdp_china_data = []
    gdp_uk_data = []

    gdp_c = current_gdp_china_ppp
    gdp_u = current_gdp_uk_ppp

    for year in years:
        gdp_china_data.append(gdp_c)
        gdp_uk_data.append(gdp_u)
        gdp_c *= 1 + china_growth_rate
        gdp_u *= 1 + uk_growth_rate

    # --- Plotting using Matplotlib ---
    plt.figure(figsize=(10, 6))
    plt.plot(
        years,
        gdp_china_data,
        label=f"China GDP/Capita (Growth: {china_growth_rate * 100:.1f}%)",
        color="red",
        linewidth=2,
    )
    plt.plot(
        years,
        gdp_uk_data,
        label=f"UK GDP/Capita (Growth: {uk_growth_rate * 100:.1f}%)",
        color="blue",
        linewidth=2,
    )

    # Add a marker and annotation for convergence
    # Find the value at the convergence year
    convergence_gdp = gdp_uk_data[years_to_converge]
    plt.scatter(convergence_year, convergence_gdp, color="green", zorder=5, s=100)
    plt.annotate(
        f"Convergence: {convergence_year}\n(${convergence_gdp:,.0f})",
        xy=(convergence_year, convergence_gdp),
        xytext=(convergence_year - 10, convergence_gdp + 20000),
        arrowprops=dict(
            facecolor="black", arrowstyle="->", connectionstyle="arc3,rad=.2"
        ),
        fontsize=10,
        ha="center",
    )

    # Customize the plot
    plt.title("Projection of China vs. UK GDP per Capita (PPP)")
    plt.xlabel("Year")
    plt.ylabel("GDP Per Capita (Intl. USD, PPP)")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.yscale("linear")
    plt.xlim(start_year, start_year + total_years - 1)
    plt.tight_layout()

    # Display the plot
    plt.show()


# Run the function to generate the plot when the script is executed
if __name__ == "__main__":
    generate_china_uk_gdp_plot()
