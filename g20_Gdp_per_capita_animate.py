import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from sklearn.linear_model import LinearRegression
import warnings

# Suppress potential future warnings from pandas
warnings.simplefilter(action='ignore', category=FutureWarning)

def get_hardcoded_g20_data():
    """Provides a DataFrame with hardcoded historical GDP per capita data for G20 countries."""
    data = {
        'Argentina':    [11795, 8579, 13622, 15502],
        'Australia':    [59907, 53696, 64491, 74886],
        'Brazil':       [9257, 7011, 8918, 12530],
        'Canada':       [46831, 43278, 52722, 65516],
        'China':        [9977, 10409, 12720, 18634],
        'France':       [43493, 40581, 42330, 53814],
        'Germany':      [48011, 47101, 51384, 65516],
        'India':        [2008, 1933, 2411, 4475],
        'Indonesia':    [3894, 3912, 4798, 6972],
        'Italy':        [35058, 32172, 37146, 47470],
        'Japan':        [40049, 40033, 33854, 41669],
        'Mexico':       [9931, 8561, 11497, 15517],
        'Russia':       [11453, 10255, 15444, 16601],
        'Saudi Arabia': [23625, 20349, 30448, 34705],
        'South Africa': [6442, 5236, 6766, 7066],
        'South Korea':  [33543, 31762, 32423, 41857],
        'Türkiye':      [9883, 8645, 10616, 20149],
        'United Kingdom':[43632, 41059, 45850, 68659],
        'United States':[63184, 64483, 77412, 105692]
    }
    years = [2018, 2020, 2022, 2030]
    df = pd.DataFrame(data, index=years)
    df.index.name = 'Year'
    return df

def extrapolate_gdp_data(df_historic):
    """Extrapolates GDP data to 2070 using a log-linear regression model."""
    last_historical_year = df_historic.index.max()
    future_years = np.array(range(last_historical_year + 1, 2071))
    all_country_series = []
    
    for country in df_historic.columns:
        series = df_historic[country].dropna()
        X_train = series.index.values.reshape(-1, 1)
        y_train_log = np.log(series.values)
        model = LinearRegression()
        model.fit(X_train, y_train_log)
        
        future_years_reshaped = future_years.reshape(-1, 1)
        log_predictions = model.predict(future_years_reshaped)
        predictions = np.exp(log_predictions)
        
        future_series = pd.Series(predictions, index=future_years)
        full_series = pd.concat([series, future_series])
        full_series.name = country
        all_country_series.append(full_series)
        
    df_extrapolated = pd.concat(all_country_series, axis=1)
    df_extrapolated.index.name = 'Year'
    return df_extrapolated

def create_gdp_animation(df_animated):
    """Creates and saves an animated bar chart of GDP per capita."""
    animation_years = list(range(df_animated.index.min(), 2071))
    fig, ax = plt.subplots(figsize=(16, 9))
    
    # Define colors for specific countries
    country_colors = {
        'India': 'blue',
        'China': 'red',
        'Russia': 'brown',
        'United States': 'orange'
    }
    
    def animate(year):
        ax.clear()
        data_for_year = df_animated.loc[year].dropna().sort_values()
        
        # Create colors array for all countries
        colors = []
        for country in data_for_year.index:
            if country in country_colors:
                colors.append(country_colors[country])
            else:
                colors.append('steelblue')
                
        # Create bar plot
        bars = ax.bar(data_for_year.index, data_for_year.values, color=colors)
        
        # Add value labels on top of each bar
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval + 500,  # Add 500 to position text above bar
                    f'{yval/1000:,.1f}K',  # Format as float with one decimal place
                    ha='center', va='bottom', fontsize=10, rotation=0)
        
        ax.set_title(f'G20 Nominal GDP Per Capita in {year}', fontsize=20, pad=20)
        ax.set_ylabel('Nominal GDP Per Capita (Current US$)', fontsize=14)
        ax.set_ylim(0, df_animated.values.max() * 1.05)
        ax.tick_params(axis='x', labelrotation=60, labelsize=11)
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        ax.text(0.97, 0.95, str(year), transform=ax.transAxes, fontsize=24,
                fontweight='bold', ha='right', va='top', color='gray')
        
        fig.tight_layout(pad=2.0)

    ani = FuncAnimation(fig, animate, frames=animation_years, interval=200, repeat=False)
    
    try:
        output_filename = 'g20_gdp_per_capita_animation.mp4'
        ani.save(output_filename, writer='ffmpeg', fps=1, dpi=150)
        print(f"✅ Animation successfully saved as '{output_filename}'")
    except FileNotFoundError:
        print("❌ Error: 'ffmpeg' not found.")
        print("Please install FFmpeg on your system to save the animation as an MP4 video.")

# --- Main execution block ---
if __name__ == "__main__":
    print("Loading hardcoded G20 historical GDP data...")
    g20_historical_data = get_hardcoded_g20_data()
    
    print("Extrapolating data to 2070...")
    g20_extrapolated_data = extrapolate_gdp_data(g20_historical_data)
    
    # **FIX**: Reindex the DataFrame to include all years and interpolate missing values.
    # This creates a complete index from 2018 to 2070, preventing the KeyError.
    print("Interpolating missing years for a smooth animation...")
    start_year = g20_extrapolated_data.index.min()
    full_index = range(start_year, 2071)
    g20_final_data = g20_extrapolated_data.reindex(full_index)
    g20_final_data.interpolate(method='linear', inplace=True)
    
    print("\nCreating animated bar chart...")
    create_gdp_animation(g20_final_data)