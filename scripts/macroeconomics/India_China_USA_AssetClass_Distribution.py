import matplotlib.pyplot as plt
import numpy as np

# 1. Define countries and the finalized wealth buckets
countries = ['India', 'China', 'United States']
buckets = ['Equity', 'Bank Deposit', 'Gold/Silver', 'Real Estate', 'Private Biz Equity', 'Other']

# 2. Perfect 100% normalized datasets with corrected real-world business equity
wealth_data = {
    'India': [5.0, 23.0, 16.0, 38.0, 16.5, 1.5],
    'China': [11.0, 24.0, 2.0, 51.0, 11.0, 1.0],
    'United States': [35.0, 13.0, 0.5, 29.5, 19.5, 2.5]
}

# Convert dictionary values to a structured numpy array for plotting
matrix_data = np.array([wealth_data[c] for c in countries])

# 3. Configure the stacked bar chart layout
fig, ax = plt.subplots(figsize=(11, 7))
bar_width = 0.45
positions = np.arange(len(countries))

# Color palette mapped across the 6 refined categories
colors = ['#4e79a7', '#59a14f', '#f28e2b', '#e15759', '#b07aa1', '#bab0ac']

# 4. Iteratively build the stacked layers
bottom_base = np.zeros(len(countries))

for i, bucket_name in enumerate(buckets):
    layer_values = matrix_data[:, i]
    bars = ax.bar(positions, layer_values, bar_width, bottom=bottom_base, label=bucket_name, color=colors[i])
    bottom_base += layer_values
    
    # Render percentage value labels inside the bar segments
    for bar in bars:
        height = bar.get_height()
        if height > 2.4:  # Suppress small numbers to prevent visual clipping
            y_pos = bar.get_y() + height / 2
            ax.text(bar.get_x() + bar.get_width()/2, y_pos, f'{height:.1f}%', 
                    ha='center', va='center', color='white', fontweight='bold', fontsize=10)

# 5. Stylize chart elements and axes
ax.set_title('Corrected Household Wealth Allocation Profile (Standardized Business Equity)', fontsize=13, fontweight='bold', pad=20)
ax.set_xticks(positions)
ax.set_xticklabels(countries, fontsize=12, fontweight='bold')
ax.set_ylabel('Percentage of Total Net Wealth (%)', fontsize=11)
ax.set_ylim(0, 105)

# Place the legend cleanly below the plot area
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.12), ncol=3, frameon=True, fontsize=10)
ax.grid(axis='y', linestyle='--', alpha=0.3)

plt.tight_layout()
plt.show()
