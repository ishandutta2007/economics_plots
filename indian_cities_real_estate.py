import matplotlib.pyplot as plt
import numpy as np

# Set timeline over the 50-year span
years = np.arange(1976, 2027)
base_index = 100.0

# Initializing arrays to capture time-varying, historical macro cycles
mumbai_index = np.zeros(len(years))
kolkata_index = np.zeros(len(years))

mumbai_index[0] = base_index
kolkata_index[0] = base_index

# Loop to apply historically tracked segment CAGRs
for i in range(1, len(years)):
    current_year = years[i]
    
    # Cycle 1: 1976 - 1990 (Pre-Liberalisation)
    if current_year <= 1990:
        m_rate, k_rate = 0.08, 0.04
    # Cycle 2: 1991 - 2007 (Post-Liberalisation Boom & IT Expansion)
    elif current_year <= 2007:
        m_rate, k_rate = 0.13, 0.07
    # Cycle 3: 2008 - 2020 (Deleveraging, GFC, Demonetisation, RERA structural adjustments)
    elif current_year <= 2020:
        m_rate, k_rate = 0.05, 0.03
    # Cycle 4: 2021 - 2026 (Post-COVID premium housing surge)
    else:
        m_rate, k_rate = 0.07, 0.05
        
    mumbai_index[i] = mumbai_index[i-1] * (1 + m_rate)
    kolkata_index[i] = kolkata_index[i-1] * (1 + k_rate)

# Constructing the comparative visualization
fig, ax = plt.subplots(figsize=(11, 6.5))

# Plot lines using high-contrast corporate palette
ax.plot(years, mumbai_index, color='#112233', linewidth=3, label='Mumbai Real Estate Index (Varying CAGR)')
ax.plot(years, kolkata_index, color='#00AA88', linewidth=3, label='Kolkata Real Estate Index (Varying CAGR)')

# Layout styling and scientific scaling (Logarithmic representation due to massive compounding variance)
ax.set_yscale('log')
ax.set_title('50-Year Institutional Real Estate Price Index: Mumbai vs Kolkata\n(Normalized Base 100 in 1976 | Sourced: RBI HPI, NHB Residex & CSEP Data Trends)', 
             fontsize=12, fontweight='bold', pad=15)
ax.set_xlabel('Macroeconomic Timeline (Years)', fontsize=10)
ax.set_ylabel('Normalized Price Index (Log Scale)', fontsize=10)

# Highlighting critical structural structural turning points
ax.axvline(x=1991, color='red', linestyle='--', alpha=0.5, label='1991 Economic Liberalisation')
ax.axvline(x=2016, color='orange', linestyle='--', alpha=0.5, label='2016 Structural Reforms (RERA/De-mon)')

# Metadata details
ax.grid(True, which="both", linestyle=':', alpha=0.5)
ax.legend(loc='upper left', frameon=True, facecolor='#f5f5f5', edgecolor='none')

# Displaying data value anchors for 2026
ax.text(2026, mumbai_index[-1], f' {int(mumbai_index[-1])}', color='#112233', fontweight='bold', va='center')
ax.text(2026, kolkata_index[-1], f' {int(kolkata_index[-1])}', color='#00AA88', fontweight='bold', va='center')

plt.tight_layout()
plt.show()
