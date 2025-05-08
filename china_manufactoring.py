import matplotlib.pyplot as plt

# Hypothetical data for China's manufacturing growth by year
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
manufacturing_growth = [12.1, 10.0, 9.3, 7.8, 7.3, 6.8, 6.5, 6.6, 6.2, 5.7, 2.3, 4.5]  # in percentage

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(years, manufacturing_growth, marker='o', linestyle='-', color='b', label="Manufacturing Growth (%)")

# Add title and labels
plt.title("China's Manufacturing Growth by Year", fontsize=16)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Growth Rate (%)", fontsize=12)

# Add grid and legend
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.axhline(0, color='black', linewidth=0.8, linestyle='-')
plt.legend(fontsize=12)

# Show the plot
plt.tight_layout()
plt.show()