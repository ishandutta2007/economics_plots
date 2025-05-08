import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import pandas as pd
import calendar # For month names

# Helper function to ensure a scalar value is extracted from DataFrame .loc result
def get_scalar_value(value_from_loc, country_name, year_val):
    """
    Converts a value retrieved by .loc to a scalar.
    If it's a Series with one item, returns that item.
    If it's already a scalar, returns it.
    If it's a Series with multiple items, prints a warning and returns np.nan.
    """
    if isinstance(value_from_loc, pd.Series):
        if len(value_from_loc) == 1:
            return value_from_loc.item()
        else:
            print(f"  Warning: Multiple values found for {country_name}, year {year_val} during scalar extraction. Check data uniqueness.")
            return np.nan  # Indicates an issue
    return value_from_loc # Assumed to be scalar already

# Helper function for annual data interpolation
def interpolate_annual_gdp_data(key_points_dict, start_year=1990, end_year=2024):
    """
    Interpolates GDP data between key points for an annual series.
    """
    series = pd.Series(key_points_dict)
    min_data_year = series.index.min()
    max_data_year = series.index.max()
    dense_series = series.reindex(pd.Index(range(min_data_year, max_data_year + 1))).interpolate(method='linear')
    final_series = dense_series.reindex(pd.Index(range(start_year, end_year + 1)))
    final_series = final_series.fillna(method='ffill').fillna(method='bfill')
    return final_series

# 1. Data Preparation (GDP per capita, PPP, current international $)
data_key_points = {
    'Sri Lanka': {1990: 2320, 2000: 3800, 2010: 8200, 2020: 12800, 2022: 13773, 2023: 13977, 2024: 14679},
    'Bangladesh': {1990: 865, 2000: 1400, 2010: 2800, 2020: 5600, 2022: 7364, 2023: 7965, 2024: 8686},
    'Bhutan': {1990: 1379, 2000: 2800, 2010: 7000, 2020: 12000, 2022: 13011, 2023: 13821, 2024: 14815},
    'India': {1990: 1157, 2000: 1887, 2010: 4680, 2020: 6997, 2022: 8499, 2023: 9294, 2024: 10123},
    'Pakistan': {1990: 2009, 2000: 2800, 2010: 4300, 2020: 5800, 2022: 6479, 2023: 6736, 2024: 6998}
}

countries = ['Sri Lanka', 'Bangladesh', 'Bhutan', 'India', 'Pakistan']
country_flags_unicode = { # Unicode flag emojis
    'Sri Lanka': '🇱🇰', 'Bangladesh': '🇧🇩', 'Bhutan': '🇧🇹',
    'India': '🇮🇳', 'Pakistan': '🇵🇰'
}
# Font to use for emojis. Change if flags don't render correctly.
# Common options: 'Segoe UI Emoji' (Windows), 'Apple Color Emoji' (macOS), 'Noto Color Emoji' (Linux)
EMOJI_FONT = 'Segoe UI Emoji'


# Create annual historical data
historical_gdp_data_annual = {}
for country in countries:
    historical_gdp_data_annual[country] = interpolate_annual_gdp_data(data_key_points[country], 1990, 2024)

df_historical_annual = pd.DataFrame(historical_gdp_data_annual)
df_historical_annual.index.name = 'Year'
df_historical_annual.index = pd.to_datetime(df_historical_annual.index, format='%Y')

# Convert annual data to monthly data by linear interpolation
df_historical_monthly = df_historical_annual.resample('MS').interpolate(method='linear')
df_historical_monthly.index = df_historical_monthly.index.to_period('M')


# 2. Extrapolation
annual_growth_factors = {}
cagr_calc_start_year = 2015
cagr_calc_end_year = 2024
num_years_for_cagr = cagr_calc_end_year - cagr_calc_start_year

print("Calculating annual growth factors for extrapolation (based on 2015-2024 data):")
for country in countries:
    try:
        start_val_raw = df_historical_annual.loc[str(cagr_calc_start_year), country]
        end_val_raw = df_historical_annual.loc[str(cagr_calc_end_year), country]
        start_val = get_scalar_value(start_val_raw, country, cagr_calc_start_year)
        end_val = get_scalar_value(end_val_raw, country, cagr_calc_end_year)
    except KeyError:
        print(f"  Warning: Data for year {cagr_calc_start_year} or {cagr_calc_end_year} not found for {country}.")
        start_val, end_val = np.nan, np.nan

    if pd.isna(start_val) or pd.isna(end_val) or start_val <= 0 or end_val <= 0 or num_years_for_cagr <= 0:
        default_growth = 1.02
        if country == 'India': default_growth = 1.065
        annual_growth_factors[country] = default_growth
        print(f"  Warning: Could not calculate CAGR for {country} (start: {start_val}, end: {end_val}). Using default: {annual_growth_factors[country]:.4f}")
    else:
        cagr = (end_val / start_val)**(1 / num_years_for_cagr) - 1
        annual_growth_factors[country] = 1 + cagr
    print(f"  {country}: {annual_growth_factors[country]:.4f} ({(annual_growth_factors[country]-1)*100:.2f}% annual growth)")

monthly_growth_factors = {country: factor**(1/12) for country, factor in annual_growth_factors.items()}
print("\nMonthly growth factors for projection:")
for country, factor in monthly_growth_factors.items():
    print(f"  {country}: {factor:.6f} ({(factor-1)*100:.4f}% monthly growth)")

df_extrapolated_monthly = df_historical_monthly.copy()
last_historical_period = df_historical_monthly.index.max()
current_projection_period = last_historical_period
extrapolation_stop_period = last_historical_period

max_allowable_projection_year = 2047
max_allowable_projection_period = pd.Period(f'{max_allowable_projection_year}-12', freq='M')

india_overtook_sri_lanka = False
india_overtook_bangladesh = False
india_overtook_bhutan = False

while current_projection_period < max_allowable_projection_period:
    current_projection_period += 1
    next_gdp_row = {}
    for country in countries:
        prev_period_gdp = df_extrapolated_monthly.loc[current_projection_period - 1, country]
        next_gdp_row[country] = prev_period_gdp * monthly_growth_factors[country]
    df_extrapolated_monthly.loc[current_projection_period] = next_gdp_row

    india_gdp_current = df_extrapolated_monthly.loc[current_projection_period, 'India']
    sri_lanka_gdp_current = df_extrapolated_monthly.loc[current_projection_period, 'Sri Lanka']
    bangladesh_gdp_current = df_extrapolated_monthly.loc[current_projection_period, 'Bangladesh']
    bhutan_gdp_current = df_extrapolated_monthly.loc[current_projection_period, 'Bhutan']

    if not india_overtook_sri_lanka and india_gdp_current > sri_lanka_gdp_current:
        print(f"INFO: India (GDP: ${india_gdp_current:,.0f}) surpassed Sri Lanka (GDP: ${sri_lanka_gdp_current:,.0f}) in {current_projection_period}")
        india_overtook_sri_lanka = True
    if not india_overtook_bangladesh and india_gdp_current > bangladesh_gdp_current:
        print(f"INFO: India (GDP: ${india_gdp_current:,.0f}) surpassed Bangladesh (GDP: ${bangladesh_gdp_current:,.0f}) in {current_projection_period}")
        india_overtook_bangladesh = True
    if not india_overtook_bhutan and india_gdp_current > bhutan_gdp_current:
        print(f"INFO: India (GDP: ${india_gdp_current:,.0f}) surpassed Bhutan (GDP: ${bhutan_gdp_current:,.0f}) in {current_projection_period}")
        india_overtook_bhutan = True

    # if india_overtook_sri_lanka and india_overtook_bangladesh and india_overtook_bhutan:
    #     extrapolation_stop_period = current_projection_period
    #     print(f"SUCCESS: India's GDP per capita projected to surpass all Sri Lanka's, Bangladesh's and Bhutan's in {extrapolation_stop_period}.")
    #     break
else:
    extrapolation_stop_period = max_allowable_projection_period
    print(f"WARNING: India did not surpass both Sri Lanka and Bhutan by {max_allowable_projection_period}. Animation runs until then.")

start_animation_period = pd.Period('1990-01', freq='M')
periods_for_animation = df_extrapolated_monthly.loc[start_animation_period:extrapolation_stop_period].index.tolist()

# 3. Animation Setup
fig, ax = plt.subplots(figsize=(16, 10)) # Increased size slightly for clarity
country_color_map = {
    'Sri Lanka': '#1f77b4', 'Bangladesh': '#ff7f0e', 'Bhutan': '#2ca02c',
    'India': '#d62728', 'Pakistan': '#9467bd'
}

projection_start_year_for_annotation = last_historical_period.year + 1
projection_end_year_for_annotation = extrapolation_stop_period.year
projected_data_text = f'Projected Data ({projection_start_year_for_annotation}-{projection_end_year_for_annotation})'


def animate_gdp_chart(period_index_in_animation):
    ax.clear()
    current_period = periods_for_animation[period_index_in_animation]
    # Get data for the current period and sort by GDP value
    gdp_data_for_period = df_extrapolated_monthly.loc[current_period, countries].sort_values(ascending=False)
    
    # Country names for y-axis labels (without flags here)
    y_labels_plain = gdp_data_for_period.index.tolist()
    bar_colors_sorted = [country_color_map[country] for country in y_labels_plain]

    # Create horizontal bars
    bars = ax.barh(y_labels_plain, gdp_data_for_period.values, color=bar_colors_sorted, height=0.8)
    ax.set_yticks(np.arange(len(y_labels_plain)))
    ax.set_yticklabels(y_labels_plain, fontsize=16, fontweight='bold') 
    
    ax.set_title('GDP per Capita (PPP, Current Int\'l $)', fontsize=18, fontweight='bold', pad=20)
    # ax.set_xlabel('GDP per Capita (PPP, Current International $)', fontsize=14)
    ax.invert_yaxis() # Highest GDP at the top

    # Add value labels and flags
    for i, bar in enumerate(bars):
        country_name = y_labels_plain[i] # Get country name from sorted list
        bar_width = bar.get_width()
        
        # Value label (outside the bar, to the right)
        value_label_x_position = bar_width * 1.01 
        ax.text(value_label_x_position, bar.get_y() + bar.get_height() / 2., f'${bar_width:,.0f}', 
                va='center', ha='left', fontsize=18, fontweight='bold', color='black')

        # Flag (inside the bar, towards the right end)
        # Adjust flag_x_offset based on typical flag width and scale
        # This might need tweaking depending on the overall GDP values and plot size
        flag_x_offset_percentage = 0.05 # 5% from the end of the bar
        flag_x_position = bar_width * (1 - flag_x_offset_percentage) 
        
        # Ensure flag position is not too far left for very small bars
        if bar_width > 0 : # Only plot flag if bar exists
             # Heuristic: if bar is very short, place flag closer to start, or make it smaller
            min_bar_width_for_flag_offset = ax.get_xlim()[1] * 0.05 # e.g. 5% of total x-axis width
            if bar_width < min_bar_width_for_flag_offset:
                flag_x_position = bar_width * 0.5 # Center it for very short bars
            
            # ax.text(flag_x_position, bar.get_y() + bar.get_height() / 2., 
            #         country_flags_unicode.get(country_name, ''), # Get flag emoji
            #         va='center', ha='center', fontsize=16, # Adjust fontsize as needed for flags
            #         fontname=EMOJI_FONT, # Attempt to use emoji-supporting font
            #         color='black') # Color of the emoji text (usually not needed as emojis have their own color)


    max_gdp_in_frame = gdp_data_for_period.max()
    ax.set_xlim(0, max_gdp_in_frame * 1.28) # Increased padding for value labels
    ax.tick_params(axis='x', labelsize=11)

    # Date display (Month-Year)
    month_name = calendar.month_abbr[current_period.month]
    date_display_text = f'{month_name}-{current_period.year}'
    ax.text(0.98, 0.03, date_display_text, 
            transform=ax.transAxes, fontsize=20, color='red', 
            ha='right', va='bottom', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', fc='white', alpha=0.7))

    # Projected data annotation
    if current_period > last_historical_period:
        ax.text(0.98, 0.11, projected_data_text, 
                transform=ax.transAxes, fontsize=16, color='darkblue', ha='right', va='bottom', alpha=0.8,
                bbox=dict(boxstyle='round,pad=0.3', fc='lightyellow', alpha=0.6))
    
    ax.grid(axis='x', linestyle='--', alpha=0.7)
    ax.set_facecolor('#f0f0f0') 
    fig.patch.set_facecolor('#e0e0e0') 
    plt.tight_layout(pad=3.0) # Increased padding slightly

pause_frames = 200
animation_frames_count = len(periods_for_animation)
ani = animation.FuncAnimation(fig, animate_gdp_chart, frames=animation_frames_count + pause_frames, 
                              interval=100, repeat=False)

# --- Optional: Code to save the animation ---
print("Attempting to save animation as 'gdp_per_capita_monthly_animation.mp4'...")
try:
    Writer = animation.writers["ffmpeg"]
    writer = Writer(fps=10, metadata=dict(artist="GDP Visualizer"), bitrate=2000) 
    ani.save('gdp_per_capita_monthly_animation.mp4', writer=writer)
    print("Animation successfully saved.")
except RuntimeError as e:
    print(f"Error saving animation: {e}. Ensure ffmpeg is installed and in PATH.")
    print(f"If flags (emojis) are not rendering in the video, it might be an ffmpeg/font issue.")
except Exception as e:
    print(f"An unexpected error occurred during saving: {e}")

# plt.show()
