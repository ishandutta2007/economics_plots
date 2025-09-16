import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create sample data (replace with real data for accurate representation)
# Data represents a simplified trend based on historical economic shifts
years = np.arange(1825, 2025, 5)  # Last 200 years (roughly)

# Simulate component percentages - this is a rough approximation
agriculture = np.interp(years, [1825, 1875, 1925, 1975, 2025], [60, 40, 20, 5, 1])
manufacturing = np.interp(years, [1825, 1875, 1925, 1975, 2025], [10, 30, 40, 20, 15])
services = np.interp(years, [1825, 1875, 1925, 1975, 2025], [20, 20, 30, 60, 75])
mining = np.interp(years, [1825, 1875, 1925, 1975, 2025], [5, 5, 5, 5, 5])

# Create a DataFrame
data = pd.DataFrame({
    'Year': years,
    'Agriculture': agriculture,
    'Manufacturing': manufacturing,
    'Services': services,
    'Mining': mining
})

# Normalize the data to represent proportions (sum to 100%)
data[['Agriculture', 'Manufacturing', 'Services', 'Mining']] = data[['Agriculture', 'Manufacturing', 'Services', 'Mining']].div(data[['Agriculture', 'Manufacturing', 'Services', 'Mining']].sum(axis=1), axis=0) * 100

# Create the plot
plt.figure(figsize=(12, 6))
plt.stackplot(data['Year'], 
              data['Agriculture'], 
              data['Manufacturing'], 
              data['Services'], 
              data['Mining'], 
              labels=['Agriculture', 'Manufacturing', 'Services', 'Mining'])
plt.title('US GDP Components by Sector (Estimated Proportions)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Percentage of GDP', fontsize=12)
plt.legend(loc='upper left', bbox_to_anchor=(1,1))
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

