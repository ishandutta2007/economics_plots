import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Historical data
years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]).reshape(-1, 1)
imports = np.array([112, 88, 92, 114, 111, 82, 121, 158, 141])

# Train a simple Linear Regression model
model = LinearRegression()
model.fit(years, imports)

# Predict future till 2030
future_years = np.arange(2015, 2031).reshape(-1, 1)
future_imports = model.predict(future_years)

# Plot
plt.figure(figsize=(10,6))
plt.plot(years.flatten(), imports, 'bo-', label='Actual Imports')
plt.plot(future_years.flatten(), future_imports, 'r--', label='Projected Imports')
plt.title("India's Crude Oil Imports (USD Billion) with Projections till 2030")
plt.xlabel('Year')
plt.ylabel('Imports (USD Billion)')
plt.grid(True)
plt.legend()
plt.show()
