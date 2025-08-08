import pandas as pd
import matplotlib.pyplot as plt

# Creating a DataFrame with historical exchange rate data from 2000 to 2024.
# The 2025 data is a partial average and not included in the plot to maintain annual consistency.
data = {
    'Year': list(range(2000, 2025)),
    'USD to RUB (Average)': [
        28.16, 29.14, 31.34, 30.68, 28.85, 28.27, 26.83, 25.57, 24.87,
        31.74, 30.34, 29.40, 31.09, 31.85, 38.61, 60.96, 67.03, 58.33,
        62.90, 64.67, 72.15, 73.65, 68.47, 76.01, 93.00
    ],
    'USD to CNY (Average)': [
        8.28, 8.28, 8.28, 8.28, 8.28, 8.19, 7.97, 7.60, 6.94, 6.83,
        6.77, 6.46, 6.31, 6.19, 6.16, 6.23, 6.64, 6.75, 6.61,
        6.90, 7.03, 6.45, 6.73, 7.04, 7.20
    ]
}
df_exchange_rates = pd.DataFrame(data)

# Create a figure and a set of subplots
fig, ax1 = plt.subplots(figsize=(12, 8))

# Plot USD to RUB on the primary y-axis (ax1)
color = 'tab:red'
ax1.set_xlabel('Year')
ax1.set_ylabel('USD to RUB (Average)', color=color)
ax1.plot(df_exchange_rates['Year'], df_exchange_rates['USD to RUB (Average)'], color=color, label='USD to RUB')
ax1.tick_params(axis='y', labelcolor=color)

# Create a second y-axis (ax2) for the USD to CNY data, sharing the same x-axis
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('USD to CNY (Average)', color=color)
ax2.plot(df_exchange_rates['Year'], df_exchange_rates['USD to CNY (Average)'], color=color, label='USD to CNY')
ax2.tick_params(axis='y', labelcolor=color)

# Adjust x-axis ticks to show every 5 years for better readability
ax1.set_xticks(range(2000, 2025, 5))
ax1.set_xticklabels(range(2000, 2025, 5), rotation=45, ha='right')

# Add a title and legend
plt.title('Historical Exchange Rates: USD to RUB and USD to CNY (2000-Present)')
fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.9))

# Adjust plot layout
plt.tight_layout()

# Save the plot to a file
plt.show()
plt.savefig('usd_exchange_rates_2000_2025_corrected.png')