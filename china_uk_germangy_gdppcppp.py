import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2025, 2051, 5)

# Define the initial GDP per capita (PPP) values for 2025
china_2025 = 29191
germany_2025 = 68743
uk_2025 = 54500

# Define the growth rates
china_growth_rate = 0.0417  # 4.17%
germany_growth_rate = 0.015  # 1.5%
uk_growth_rate = 0.015  # 1.5%

# Calculate the projected GDP per capita (PPP) values
china_gdp_ppp = [china_2025 * ((1 + china_growth_rate) ** ((year - 2025) / 5)) for year in years]
germany_gdp_ppp = [germany_2025 * ((1 + germany_growth_rate) ** ((year - 2025) / 5)) for year in years]
uk_gdp_ppp = [uk_2025 * ((1 + uk_growth_rate) ** ((year - 2025) / 5)) for year in years]

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(years, china_gdp_ppp, label='China', marker='o')
plt.plot(years, germany_gdp_ppp, label='Germany', marker='o')
plt.plot(years, uk_gdp_ppp, label='UK', marker='o')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('GDP per Capita (PPP) in USD')
plt.title('Projected GDP per Capita (PPP) until 2050')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
