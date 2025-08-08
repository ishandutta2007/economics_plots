import matplotlib.pyplot as plt
import numpy as np

# Data Center Electricity Consumption (TWh) and Global Total (TWh) - based on search results
# (Detailed data population and alignment logic would go here,
# incorporating the specific years and values/ranges from the sources)
# Example placeholders:
years = np.array([2010, 2018, 2022, 2024, 2026, 2030, 2035]) # Example years
# datacenter_twh = np.array([193, 205, 290, 415, 850, 945, 1200]) # Example data center TWh (using averages where ranges exist)
datacenter_twh = np.array([193, 205, 290, 415, 850, 1945, 3200]) # Example data center TWh (using averages where ranges exist)
total_electricity_twh = np.array([19300, 20500, 24398, 26000, 29000, 32586, 36364]) # Example total TWh (derived from percentages and reported totals)

# Calculate percentages
datacenter_percentage = (datacenter_twh / total_electricity_twh) * 100

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(years, datacenter_percentage, marker='o', linestyle='-')
plt.title('Datacenter Electricity Consumption as Percentage of Global Total (Historical and Projected)')
plt.xlabel('Year')
plt.ylabel('Percentage of Total Global Electricity Consumption')
plt.grid(True)
plt.xlim([2004, 2045]) # Adjust x-axis limits to cover 20 years past and future
plt.ylim([0, max(datacenter_percentage) * 1.2]) # Adjust y-axis limits
plt.show()

