import matplotlib.pyplot as plt
import pandas as pd

# Hardcoded 5-year data (Annual Averages / Year-End Milestones)
years = [2021, 2022, 2023, 2024, 2025]
gold_prices = [1798.00, 1800.00, 1940.00, 2624.60, 4887.07]
silver_prices = [25.14, 21.79, 23.41, 28.46, 84.63]
copper_prices = [4.24, 4.00, 3.85, 4.40, 5.92]

# Create DataFrame
df = pd.DataFrame({
    'Year': years,
    'Gold': gold_prices,
    'Silver': silver_prices,
    'Copper': copper_prices
})

fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot Gold and Silver on Primary Axis (Left)
ax1.set_xlabel('Year')
ax1.set_ylabel('Price (Gold/Silver) - USD/oz', color='black')
line1 = ax1.plot(df['Year'], df['Gold'], marker='o', color='gold', label='Gold (oz)')
line2 = ax1.plot(df['Year'], df['Silver'], marker='s', color='silver', label='Silver (oz)')
ax1.tick_params(axis='y')

# Plot Copper on Secondary Axis (Right)
ax2 = ax1.twinx()
ax2.set_ylabel('Price (Copper) - USD/lb', color='brown')
line3 = ax2.plot(df['Year'], df['Copper'], marker='^', color='brown', linestyle='--', label='Copper (lb)')
ax2.tick_params(axis='y', labelcolor='brown')

# Adding Titles and Legend
plt.title('5-Year Metal Price Trends (2021-2025)')
plt.xticks(years)
lines = line1 + line2 + line3
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left')

plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
