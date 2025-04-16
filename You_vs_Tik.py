import matplotlib.pyplot as plt
import pandas as pd

# Sample data (hypothetical - replace with real sources)
years = ['2018', '2019', '2020', '2021', '2022', '2023']
tiktok_revenue = [0, 0, 1.5, 5.0, 12.0, 25.0]  # TikTok started monetizing in 2019
youtube_revenue = [13.6, 15.4, 19.7, 24.1, 28.8, 30.5, 36.1]  # All figures in USD billion

# Create DataFrame
data = pd.DataFrame({
    'Year': years,
    'TikTok': tiktok_revenue,
    'YouTube': youtube_revenue
})

# Convert Year to datetime for proper x-axis formatting
data['Year'] = pd.to_datetime(data['Year'], format='%Y')

plt.figure(figsize=(12, 6))

# Plot both platforms
plt.plot(data['Year'], data['TikTok'], marker='o', label='TikTok', color='#FF4754', linewidth=2)
plt.plot(data['Year'], data['YouTube'], marker='s', label='YouTube', color='#00B8D4', linewidth=2)

# Add labels and title
plt.title('Monthly Active Users Growth Comparison (Hypothetical Data)', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Revenue (USD Billion)', fontsize=12)

# Format y-axis to show dollar signs
plt.gca().get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, _: f'${x}B'))

# Add grid and legend
plt.grid(True, alpha=0.3)
plt.legend(fontsize=12)

# Rotate x-axis labels
plt.xticks(rotation=45)

# Show plot
plt.tight_layout()
plt.show()