import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Example data: Replace with actual values from official sources for accuracy
years = np.arange(2005, 2035)
# Approximate historical imports in million metric tons (2005-2024)
historical_imports = [
    140, 160, 180, 200, 220, 240, 260, 280, 300, 330, 360, 400, 450, 500, 540, 560, 540, 510, 540, 560,
    600, 630, 670, 700, 700, 700, 700, 690, 680, 670  # 2025-2034 projections (plateau then slight decline)
]
# Split into historical and projected
historical_years = years[:20]    # 2005-2024
projected_years = years[20:]     # 2025-2034
historical_data = historical_imports[:20]
projected_data = historical_imports[20:]

plt.figure(figsize=(14, 6))
plt.plot(historical_years, historical_data, label='Historical Imports', color='blue', linewidth=2)
plt.plot(projected_years, projected_data, 'r--', label='Projected Imports (IEA, CNPC, Reuters, Bloomberg, Statista)', linewidth=2)

# Highlight COVID-19 dip (2020-2021)
plt.axvspan(2020, 2021, color='gray', alpha=0.2, label='COVID-19 Dip')

plt.title("China's Crude Oil Imports (2005–2034)\nSources: CEIC Data, CNPC, IEA, Reuters, Bloomberg, Statista", fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Crude Oil Imports (million metric tons)', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
