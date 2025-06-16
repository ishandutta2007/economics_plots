import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# --- Data Preparation ---
# Data gathered from the most recent available sources.
# - US ethnic group data is from the US Census Bureau's American Community Survey (ACS).
# - National data is from respective national statistics offices or OECD, converted to USD.

data = {
    'Category': [
        'Indian American',
        'Taiwanese American',
        'Chinese American',
        'Japanese American',
        'White American',
        'Korean American',
        'Japan',
        'Taiwan',
        'South Korea',
        'China',
        'India'
    ],
    'Median Income (USD)': [
        152341,  # Source: 2022 ACS
        110000,  # Source: 2022 ACS
        101728,  # Source: 2022 ACS
        95000,   # Source: 2022 ACS
        89050,   # Source: 2023 Current Population Survey
        85000,   # Source: 2022 ACS
        32300,   # Source: Est. from JP Statistics Bureau / OECD data (2022)
        31500,   # Source: Est. from Taiwan DGBAS data (2022)
        30900,   # Source: Est. from Statistics Korea / OECD data (2022)
        12242,   # Source: Estimated from NBS 2023 per capita data
        1961     # Source: Estimated from PLFS (2022-23)
    ], 
    'Colors': [
        'blue',   #India
        'cyan',   #'Taiwan',
        'yellow', #china,
        'pink',   #Japan
        'grey',   #whites
        'green',  #'korea',
        'pink',   #Japan
        'cyan',   #'Taiwan',
        'green',  #'korea',
        'yellow', #china
        'blue'    #India
    ]
}

df = pd.DataFrame(data)

# Sort the dataframe by income for better visualization
df_sorted = df.sort_values('Median Income (USD)', ascending=True).reset_index(drop=True)

# --- Plotting ---
# Create the figure and axes objects, adjusted figure size for more bars
fig, ax = plt.subplots(figsize=(14, 11))

# Create horizontal bars
bars = ax.barh(
    df_sorted.index,
    df_sorted['Median Income (USD)'],
    tick_label=df_sorted['Category'],
    color=df_sorted['Colors'],
    # color=plt.cm.plasma(df_sorted['Median Income (USD)'] / max(df_sorted['Median Income (USD)'])) # Color gradient
    # color=['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#C2B280', '#FF9999', '#FFCC99', '#66B2FF', '#99FF99', '#99FF99', '#C2B280']
)

# --- Formatting and Styling ---
ax.set_title('Median Household Income Comparison (Most Recent Data)', fontsize=16, pad=20)
ax.set_xlabel('Median Income (USD)', fontsize=12)
ax.set_ylabel('')
formatter = mticker.FuncFormatter(lambda x, p: f'${x:,.0f}')
ax.xaxis.set_major_formatter(formatter)
ax.spines[['top', 'right', 'left']].set_visible(False)
ax.tick_params(axis='y', length=0) # Hide y-axis ticks

# Add data labels at the end of each bar
for i, bar in enumerate(bars):
    width = bar.get_width()
    ax.text(width + 2000, i, f'${width:,.0f}', va='center', ha='left', fontsize=10)

# --- Add Relationship Annotations ---
# Define the pairs for comparison (lower income entity first)
pairs = [
    ('India', 'Indian American'),
    ('Taiwan', 'Taiwanese American'),
    ('China (Household Est.)', 'Chinese American'),
    ('Japan', 'Japanese American'),
    ('South Korea', 'Korean American')
]

# Define a consistent X-position for the annotation arrows
anno_x_pos = 16000#175000

for low_cat, high_cat in pairs:
    # Get data for the pair
    low_data = df_sorted[df_sorted['Category'] == low_cat]
    high_data = df_sorted[df_sorted['Category'] == high_cat]

    if low_data.empty or high_data.empty:
        continue

    # Get y-positions (which are the new indices) and income values
    y_low = low_data.index[0]
    val_low = low_data['Median Income (USD)'].iloc[0]
    y_high = high_data.index[0]
    val_high = high_data['Median Income (USD)'].iloc[0]

    # Calculate the multiple
    multiple = val_high / val_low

    # Draw the arrow
    ax.annotate(
        '',
        xy=(anno_x_pos*multiple + 2000, y_high),
        xytext=(anno_x_pos*multiple + 2000, y_low),
        arrowprops=dict(arrowstyle='<->', color='purple', shrinkA=5, shrinkB=5)
    )

    # Add the text label for the multiple
    ax.text(
        anno_x_pos*multiple + 2000,
        (y_low + y_high) / 2,
        f'{multiple:.1f}x',
        ha='left',
        va='center',
        fontweight='bold',
        color='purple',
        fontsize=11
    )


# --- Final Layout Adjustments ---
# Expand X-axis limit to make space for all labels and annotations
ax.set_xlim(right=ax.get_xlim()[1] * 1.35)

footnote_text = (
    "Sources:\n"
    "- US Groups: US Census Bureau (ACS/CPS).\n"
    "- Nations: Respective national statistics offices (e.g., NBS, DGBAS), OECD, or estimations from official data.\n\n"
    "*Note: National incomes are converted to USD and may be estimates."
)
fig.text(0.5, 0.01, footnote_text, ha='center', fontsize=9, style='italic', color='gray')
plt.tight_layout()
plt.subplots_adjust(left=0.25, bottom=0.15)
plt.show()

