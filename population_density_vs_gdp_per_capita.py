import matplotlib.pyplot as plt
import pandas as pd

# Sample data (Approximate values for representative countries)
data = {
    'Country': ['Monaco', 'Singapore', 'Hong Kong', 'USA', 'Norway', 'Australia', 
                'Canada', 'India', 'Bangladesh', 'Nigeria', 'Japan', 'Germany'],
    'Density': [26000, 8000, 7000, 36, 15, 3.3, 4, 480, 1300, 230, 340, 240],
    'GDP_Per_Capita': [200000, 82000, 50000, 76000, 106000, 65000, 55000, 2500, 2700, 2200, 34000, 48000]
}

df = pd.DataFrame(data)

# Create the plot
plt.figure(figsize=(12, 7))
plt.scatter(df['Density'], df['GDP_Per_Capita'], color='royalblue', s=120, alpha=0.8, edgecolors='black')

# Label each country point
for i, txt in enumerate(df['Country']):
    plt.annotate(txt, (df['Density'][i], df['GDP_Per_Capita'][i]), 
                 xytext=(8, 0), textcoords='offset points', fontsize=9)

# Formatting
plt.xscale('log')  # Essential due to extreme density differences
plt.title('Global Correlation: Population Density vs. GDP per Capita', fontsize=14, pad=20)
plt.xlabel('Population Density (People per sq km) - Log Scale', fontsize=11)
plt.ylabel('GDP per Capita (USD)', fontsize=11)
plt.grid(True, which="both", linestyle='--', alpha=0.5)

# Highlighting the non-linear trend
plt.text(5, 180000, "Low Density / High Wealth\n(Resource Rich)", color='darkgreen', weight='bold')
plt.text(5000, 150000, "High Density / High Wealth\n(City-States)", color='darkred', weight='bold')

plt.tight_layout()
plt.show()
