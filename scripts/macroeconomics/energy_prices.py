import matplotlib.pyplot as plt
import pandas as pd

# 1. Structure the historical energy dataset
data = {
    'Year': list(range(2015, 2027)),
    'US': [0.127, 0.126, 0.129, 0.129, 0.130, 0.132, 0.137, 0.150, 0.160, 0.165, 0.173, 0.188],
    'China': [0.085, 0.082, 0.081, 0.080, 0.077, 0.074, 0.080, 0.082, 0.084, 0.086, 0.087, 0.088],
    'India': [0.071, 0.072, 0.073, 0.074, 0.072, 0.065, 0.068, 0.070, 0.072, 0.075, 0.078, 0.080],
    'US_China_Ratio': [1.49, 1.54, 1.59, 1.61, 1.69, 1.78, 1.71, 1.83, 1.90, 1.92, 1.99, 2.14],
    'US_India_Ratio': [1.79, 1.75, 1.77, 1.74, 1.81, 2.03, 2.01, 2.14, 2.22, 2.20, 2.22, 2.35]
}
df = pd.DataFrame(data)

# 2. Initialize the plot layout
fig, ax1 = plt.subplots(figsize=(11, 6))
ax2 = ax1.twinx()  # Create shared-X right axis for ratios

# 3. Plot Absolute Electricity Prices (Left Axis)
line1 = ax1.plot(df['Year'], df['US'], color='#d95f02', marker='o', linewidth=2.5, label='US Price ($/kWh)')
line2 = ax1.plot(df['Year'], df['China'], color='#1b9e77', marker='s', linewidth=2, label='China Price ($/kWh)')
line3 = ax1.plot(df['Year'], df['India'], color='#7570b3', marker='^', linewidth=2, label='India Price ($/kWh)')

# 4. Plot Premium Price Ratios (Right Axis)
line4 = ax2.plot(df['Year'], df['US_China_Ratio'], color='#e7298a', linestyle='--', alpha=0.7, label='US/China Ratio (x)')
line5 = ax2.plot(df['Year'], df['US_India_Ratio'], color='#66a61e', linestyle='--', alpha=0.7, label='US/India Ratio (x)')

# 5. Fine-tune axis labels and constraints
ax1.set_xlabel('Year', fontsize=11, fontweight='bold', labelpad=10)
ax1.set_ylabel('Electricity Price (USD per kWh)', color='black', fontsize=11, labelpad=10)
ax2.set_ylabel('US Cost Premium Multiplier (x)', color='black', fontsize=11, labelpad=10)

# Format ticker marks for readability
ax1.set_xticks(df['Year'])
ax1.set_ylim(0.04, 0.21)
ax2.set_ylim(1.0, 2.6)

# 6. Build a unified grid and legend
ax1.grid(True, linestyle=':', alpha=0.6)
lines = line1 + line2 + line3 + line4 + line5
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left', frameon=True, facecolor='white', edgecolor='none')

plt.title('Global Electricity Price Divergence & US Premium Ratios (2015–2026)', fontsize=13, fontweight='bold', pad=15)
plt.tight_layout()

# 7. Display the final visualization
plt.show()
