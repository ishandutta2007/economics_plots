import matplotlib.pyplot as plt
import numpy as np

def generate_gdp_plot():
    """
    Generates data for a Matplotlib plot visualizing India/UK GDP convergence.
    """
    # --- Realistic Data & Projections (as discussed) ---
    current_gdp_india_ppp = 12100.0
    current_gdp_uk_ppp = 63760.0
    india_growth_rate = 0.048  # 4.8% annually
    uk_growth_rate = 0.008     # 0.8% annually
    start_year = 2025
    convergence_year = 2068
    total_years = convergence_year - start_year + 5 # Extend plot a bit past convergence

    years = np.arange(start_year, start_year + total_years)
    gdp_india_data = []
    gdp_uk_data = []

    gdp_i = current_gdp_india_ppp
    gdp_u = current_gdp_uk_ppp

    for year in years:
        gdp_india_data.append(gdp_i)
        gdp_uk_data.append(gdp_u)
        gdp_i *= (1 + india_growth_rate)
        gdp_u *= (1 + uk_growth_rate)

    # --- Plotting using Matplotlib ---
    plt.figure(figsize=(10, 6))
    plt.plot(years, gdp_india_data, label=f'India GDP/Capita (Growth: {india_growth_rate*100:.1f}%)', color='orange', linewidth=2)
    plt.plot(years, gdp_uk_data, label=f'UK GDP/Capita (Growth: {uk_growth_rate*100:.1f}%)', color='blue', linewidth=2)

    # Add a marker and annotation for convergence
    convergence_gdp = gdp_uk_data[convergence_year - start_year]
    plt.scatter(convergence_year, convergence_gdp, color='red', zorder=5)
    plt.annotate(
        f'Convergence: {convergence_year}\n(${convergence_gdp:,.0f})',
        xy=(convergence_year, convergence_gdp),
        xytext=(convergence_year - 15, convergence_gdp + 10000),
        arrowprops=dict(facecolor='black', arrowstyle='->', connectionstyle="arc3,rad=.2"),
        fontsize=10
    )

    # Customize the plot
    plt.title('Projection of India vs. UK GDP per Capita (PPP)')
    plt.xlabel('Year')
    plt.ylabel('GDP Per Capita (Intl. USD, PPP)')
    plt.legend()
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.yscale('linear') # Use 'log' if the numbers get too large for linear scale
    plt.xlim(start_year, start_year + total_years)
    plt.tight_layout()
    
    # Display the plot
    plt.show()

# Run the function to generate the plot when the script is executed
if __name__ == "__main__":
    generate_gdp_plot()
