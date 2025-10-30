import pandas as pd
import matplotlib.pyplot as plt

def create_fdi_dataframe():
    """
    Creates a DataFrame with hardcoded FDI (% of GDP) data 
    for China and India (1990-2023).
    Source: World Bank World Development Indicators (BX.KLT.DINV.CD.WD.GD.ZS)
    """
    
    # FDI Net Inflows (% of GDP) data from 1990 to 2023
    data = {
        'Year': range(1990, 2024),
        'China': [
            0.56, 1.25, 2.76, 5.09, 5.25, 4.41, 4.29, 3.49, 3.25, 3.28, 3.28, 
            3.23, 3.39, 2.74, 2.65, 2.73, 2.50, 2.27, 3.03, 3.19, 2.45, 2.05, 
            2.38, 2.70, 2.05, 2.08, 1.77, 1.48, 1.57, 1.59, 1.63, 1.83, 1.78, 1.62
        ],
        'India': [
            0.04, 0.10, 0.20, 0.35, 0.44, 0.58, 0.69, 0.91, 0.77, 0.67, 0.66, 
            0.94, 0.82, 0.97, 1.34, 1.42, 1.63, 3.51, 3.13, 2.87, 2.23, 2.26, 
            2.01, 1.74, 1.81, 2.45, 1.89, 2.28, 2.16, 1.86, 1.76, 2.69, 2.40, 1.51
        ]
    }
    
    df = pd.DataFrame(data).set_index('Year')
    return df

def plot_fdi_trends(df):
    """Plots the FDI trends for China and India on the same grid."""
    
    plt.figure(figsize=(12, 6))
    
    # Plotting China's FDI
    plt.plot(df.index, df['China'], label='China', marker='o', linestyle='-', color='red', linewidth=2)
    
    # Plotting India's FDI
    plt.plot(df.index, df['India'], label='India', marker='s', linestyle='--', color='blue', linewidth=2)
    
    # --- Plot Customization ---
    start_year = df.index.min()
    end_year = df.index.max()
    plt.title(f'Foreign Direct Investment (FDI) Net Inflows as % of GDP: China vs. India ({start_year}-{end_year})', fontsize=14)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('FDI Net Inflows (% of GDP)', fontsize=12)
    plt.legend(title='Country', fontsize=10)
    plt.grid(True, linestyle=':', alpha=0.6)
    
    # Customize X-axis ticks (show every 5 years)
    years = df.index.tolist()
    tick_years = [years[i] for i in range(0, len(years), 5)]
    if years[-1] not in tick_years:
        tick_years.append(years[-1])
    
    plt.xticks(tick_years, rotation=45) 
    plt.yticks(range(0, 7)) # Set y-axis ticks for better readability
    
    plt.tight_layout()
    plt.savefig('china_india_fdi_vs_gdp_hardcoded_plot.png')
    plt.show()

# --- Execution ---
try:
    fdi_df = create_fdi_dataframe()
    print("--- Hardcoded FDI Data (Tail) ---")
    print(fdi_df.tail())
    plot_fdi_trends(fdi_df)
    print("\nSuccessfully generated plot: 'china_india_fdi_vs_gdp_hardcoded_plot.png' 📊")
    
except Exception as e:
    print(f"\nAn error occurred: {e}")
