import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import pandas as pd

# Helper function for linear interpolation
def interpolate_gdp_data(key_points_dict, start_year=1990, end_year=2024):
    """
    Interpolates GDP data between key points and ensures a full yearly range.
    key_points_dict: A dictionary {year: gdp_value}
    start_year: The first year required in the output Series.
    end_year: The last year required in the output Series.
    Returns a pandas Series with interpolated data from start_year to end_year.
    """
    series = pd.Series(key_points_dict)
    # Create a full index from the minimum key point year to the maximum key point year
    min_data_year = series.index.min()
    max_data_year = series.index.max()
    
    # Interpolate within the span of available key points
    dense_series = series.reindex(pd.Index(range(min_data_year, max_data_year + 1))).interpolate(method='linear')
    
    # Now, reindex to the required full range (start_year to end_year)
    # This might introduce NaNs if start_year/end_year are outside the original key_points span
    final_series = dense_series.reindex(pd.Index(range(start_year, end_year + 1)))
    
    # Fill any NaNs at the beginning or end using forward fill then backward fill
    final_series = final_series.fillna(method='ffill').fillna(method='bfill')
    
    return final_series

# 1. Data Preparation (GDP per capita, PPP, current international $)
# Key data points based on research (IMF WEO April 2024, World Bank, etc.)
# These values represent GDP per capita in PPP (current international dollars)
data_key_points = {
    'Sri Lanka': {1990: 2320, 2000: 3800, 2010: 8200, 2020: 12800, 2022: 13773, 2023: 13977, 2024: 14679},
    'Bangladesh': {1990: 865, 2000: 1400, 2010: 2800, 2020: 5600, 2022: 7364, 2023: 7965, 2024: 8686},
    'Bhutan': {1990: 1379, 2000: 2800, 2010: 7000, 2020: 12000, 2022: 13011, 2023: 13821, 2024: 14815},
    'India': {1990: 1157, 2000: 1887, 2010: 4680, 2020: 6997, 2022: 8499, 2023: 9294, 2024: 10123},
    'Pakistan': {1990: 2009, 2000: 2800, 2010: 4300, 2020: 5800, 2022: 6479, 2023: 6736, 2024: 6998}
}

countries = ['Sri Lanka', 'Bangladesh', 'Bhutan', 'India', 'Pakistan']
historical_gdp_data = {}
# Interpolate data for each country from 1990 to 2024
for country in countries:
    historical_gdp_data[country] = interpolate_gdp_data(data_key_points[country], 1990, 2024)

df_historical = pd.DataFrame(historical_gdp_data)
df_historical.index.name = 'Year'

# 2. Extrapolation
# Calculate Compound Annual Growth Rate (CAGR) for each country using data from 2015-2024 for projection
growth_factors = {}
cagr_calc_start_year = 2015
cagr_calc_end_year = 2024 # Last year of our historical/projected data
num_years_for_cagr = cagr_calc_end_year - cagr_calc_start_year

print("Calculating growth factors for extrapolation (based on 2015-2024 data):")
for country in countries:
    start_val = df_historical.loc[cagr_calc_start_year, country]
    end_val = df_historical.loc[cagr_calc_end_year, country]
    
    # Ensure start_val and end_val are valid for CAGR calculation
    if pd.isna(start_val) or pd.isna(end_val) or start_val <= 0 or end_val <= 0 or num_years_for_cagr <= 0:
        # Fallback to a default growth factor if data is problematic
        default_growth = 1.02 # Default 2% growth
        if country == 'India':
            default_growth = 1.055 # Ensure India has a reasonable default growth for the scenario
        growth_factors[country] = default_growth
        print(f"  Warning: Could not calculate CAGR for {country} between {cagr_calc_start_year}-{cagr_calc_end_year} (start: {start_val}, end: {end_val}). Using default growth factor: {growth_factors[country]:.4f}")
    else:
        cagr = (end_val / start_val)**(1 / num_years_for_cagr) - 1
        growth_factors[country] = 1 + cagr
    print(f"  {country}: {growth_factors[country]:.4f} ({(growth_factors[country]-1)*100:.2f}% annual growth)")

# Initialize DataFrame for extrapolated data, starting with historical data
df_extrapolated = df_historical.copy()
last_historical_year = df_historical.index.max() # Should be 2024
current_projection_year = last_historical_year 
extrapolation_stop_year = last_historical_year # This will be updated when condition is met

max_allowable_projection_year = 2070 # Set a hard limit for extrapolation

india_overtook_sri_lanka = False
india_overtook_bhutan = False

# Perform extrapolation year by year
while current_projection_year < max_allowable_projection_year:
    current_projection_year += 1
    next_gdp_row = {}
    for country in countries:
        # Calculate next year's GDP based on the previous year's GDP and the growth factor
        next_gdp_row[country] = df_extrapolated.loc[current_projection_year - 1, country] * growth_factors[country]
    
    # Add the new row of projected GDPs to the DataFrame
    df_extrapolated.loc[current_projection_year] = next_gdp_row

    # Check the condition for India overtaking Sri Lanka and Bhutan
    india_gdp_current = df_extrapolated.loc[current_projection_year, 'India']
    sri_lanka_gdp_current = df_extrapolated.loc[current_projection_year, 'Sri Lanka']
    bhutan_gdp_current = df_extrapolated.loc[current_projection_year, 'Bhutan']

    if not india_overtook_sri_lanka and india_gdp_current > sri_lanka_gdp_current:
        print(f"INFO: India (GDP: ${india_gdp_current:,.0f}) surpassed Sri Lanka (GDP: ${sri_lanka_gdp_current:,.0f}) in {current_projection_year}")
        india_overtook_sri_lanka = True
    
    if not india_overtook_bhutan and india_gdp_current > bhutan_gdp_current:
        print(f"INFO: India (GDP: ${india_gdp_current:,.0f}) surpassed Bhutan (GDP: ${bhutan_gdp_current:,.0f}) in {current_projection_year}")
        india_overtook_bhutan = True

    if india_overtook_sri_lanka and india_overtook_bhutan:
        extrapolation_stop_year = current_projection_year
        print(f"SUCCESS: India's GDP per capita is projected to surpass both Sri Lanka's and Bhutan's in the year {extrapolation_stop_year}.")
        break 
else: # This 'else' corresponds to the 'while' loop
    # Executed if the loop terminated because max_allowable_projection_year was reached
    extrapolation_stop_year = max_allowable_projection_year
    print(f"WARNING: India did not surpass both Sri Lanka and Bhutan by {max_allowable_projection_year}. Animation will run until {max_allowable_projection_year}.")
    if not india_overtook_sri_lanka:
        print(f"  India's GDP (${df_extrapolated.loc[max_allowable_projection_year, 'India']:,.0f}) vs Sri Lanka's GDP (${df_extrapolated.loc[max_allowable_projection_year, 'Sri Lanka']:,.0f}) in {max_allowable_projection_year}")
    if not india_overtook_bhutan:
        print(f"  India's GDP (${df_extrapolated.loc[max_allowable_projection_year, 'India']:,.0f}) vs Bhutan's GDP (${df_extrapolated.loc[max_allowable_projection_year, 'Bhutan']:,.0f}) in {max_allowable_projection_year}")


# 3. Animation Setup
fig, ax = plt.subplots(figsize=(14, 8)) # Set figure size for better readability
# Years to plot: from 1990 up to the year the extrapolation condition was met or max year
years_for_animation = df_extrapolated.loc[1990:extrapolation_stop_year].index.tolist()

# Define consistent colors for each country
country_color_map = {
    'Sri Lanka': '#1f77b4',  # Muted Blue
    'Bangladesh': '#ff7f0e', # Safety Orange
    'Bhutan': '#2ca02c',     # Cooked Asparagus Green
    'India': '#d62728',      # Brick Red
    'Pakistan': '#9467bd'    # Muted Purple
}

def animate_gdp_chart(year_index_in_animation):
    """Function to update the chart for each frame of the animation."""
    ax.clear() # Clear previous frame's drawing
    
    current_year_to_plot = years_for_animation[year_index_in_animation]
    
    # Get GDP data for the current year and sort countries by GDP in descending order
    gdp_data_for_year = df_extrapolated.loc[current_year_to_plot, countries].sort_values(ascending=False)
    
    # Get colors in the new sorted order for consistent coloring
    bar_colors_sorted = [country_color_map[country] for country in gdp_data_for_year.index]

    # Create horizontal bars
    bars = ax.barh(gdp_data_for_year.index, gdp_data_for_year.values, color=bar_colors_sorted)
    
    # Set title and labels
    ax.set_title(f'GDP per Capita (PPP, Current Int\'l $) - Year: {current_year_to_plot}', fontsize=16, fontweight='bold')
    ax.set_xlabel('GDP per Capita (PPP, Current International $)', fontsize=12)
    ax.set_ylabel('Country', fontsize=12)
    
    # Ensure the country with the highest GDP is at the top of the y-axis
    ax.invert_yaxis() 

    # Add value labels to the end of each bar for clarity
    for bar in bars:
        bar_width = bar.get_width()
        # Position label slightly to the right of the bar
        label_x_position = bar_width * 1.01 
        ax.text(label_x_position, bar.get_y() + bar.get_height() / 2., f'${bar_width:,.0f}', 
                va='center', ha='left', fontsize=9, color='black')

    # Dynamically adjust x-axis limits with some padding for labels
    max_gdp_in_frame = gdp_data_for_year.max()
    ax.set_xlim(0, max_gdp_in_frame * 1.22) # ~22% padding for labels

    # Customize tick parameters
    ax.tick_params(axis='x', labelsize=10)
    ax.tick_params(axis='y', labelsize=10)
    
    # Add a text annotation for projected data years
    if current_year_to_plot > last_historical_year: # last_historical_year is 2024
        ax.text(0.98, 0.02, 'Projected Data', 
                transform=ax.transAxes, # Position relative to axes
                fontsize=10, color='darkred', ha='right', va='bottom', alpha=0.8,
                bbox=dict(boxstyle='round,pad=0.3', fc='wheat', alpha=0.5)) # Add a background box

    plt.tight_layout(pad=2.0) # Adjust layout to prevent labels from being cut off

# Create the animation
# Interval is the delay between frames in milliseconds (e.g., 500ms = 0.5s per frame)
# repeat=False ensures the animation plays once
animation_frames_count = len(years_for_animation)
ani = animation.FuncAnimation(fig, animate_gdp_chart, frames=animation_frames_count, 
                              interval=500, repeat=False)

# Display the animation
plt.show()

# --- Optional: Code to save the animation ---
# You need ffmpeg installed and configured in your system's PATH for this to work.
# print("Attempting to save animation as 'gdp_per_capita_animation.mp4'...")
# print("(This process can take some time depending on the animation length and system performance.)")
# try:
#     # fps (frames per second) can be adjusted. interval=500ms means 2 fps.
#     ani.save('gdp_per_capita_animation.mp4', writer='ffmpeg', fps=2, dpi=150)
#     print("Animation successfully saved as gdp_per_capita_animation.mp4")
# except RuntimeError as e:
#     print(f"Error saving animation: {e}")
#     print("Please ensure ffmpeg is installed and accessible in your system's PATH.")
# except Exception as e:
#     print(f"An unexpected error occurred during saving: {e}")

