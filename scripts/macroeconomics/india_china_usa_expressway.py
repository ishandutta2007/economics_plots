import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Historical/milestone network length data (in kilometers)
# Sources: NHAI/MoRTH (India), FHWA (USA Interstate System), Ministry of Transport (China)
data_india = {
    2002: 95,      # Mumbai-Pune Expressway early opening
    2014: 1021,    # Early baseline prior to Bharatmala acceleration
    2018: 1583,
    2020: 2065,
    2022: 4100,
    2024: 6059,
    2026: 7332     # Current operational capacity
}

data_usa = {
    1956: 1600,    # Federal-Aid Highway Act passed (incorporating early turnpikes)
    1960: 16700,   # Rapid Interstate buildout decade
    1970: 49000,
    1980: 65000,
    1992: 75000,   # Interstate system largely declared complete
    2010: 76500,
    2026: 78680    # Sustained maintenance & minor expansion
}

data_china = {
    1988: 147,     # First corridor: Shanghai-Jiading Expressway
    1995: 2141,
    1999: 10000,   # China at India's current ~7k–10k km stage
    2005: 41000,
    2011: 74000,   # Year China matched & surpassed the USA
    2015: 123500,
    2020: 161000,
    2026: 199400   # World's largest network
}

# Setup figure and aesthetic styling
plt.figure(figsize=(14, 8), dpi=120)
plt.yscale('log')

# Plot curves
plt.plot(list(data_india.keys()), list(data_india.values()), marker='o', color='#FF9933', linewidth=2.5, label='India (Access-Controlled Expressways)')
plt.plot(list(data_usa.keys()), list(data_usa.values()), marker='s', color='#002868', linewidth=2.5, label='USA (Interstate Highway System)')
plt.plot(list(data_china.keys()), list(data_china.values()), marker='^', color='#DE2910', linewidth=2.5, label='China (National Expressway System)')

# Helper function to annotate every single data point
def annotate_points(data, offset=(0, 10), color='black'):
    for year, km in data.items():
        label = f"{km:,} km"
        plt.annotate(
            label, 
            xy=(year, km), 
            xytext=offset,
            textcoords='offset points', 
            fontsize=8, 
            fontweight='semibold',
            color=color,
            ha='center',
            va='bottom',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.7, edgecolor='none')
        )

# Annotate points with offsets to prevent collisions
annotate_points(data_india, offset=(0, 8), color='#B35900')
annotate_points(data_usa, offset=(0, 8), color='#001A44')
annotate_points(data_china, offset=(0, 8), color='#990000')

# Key milestone reference annotations
plt.axhline(y=78680, color='gray', linestyle='--', alpha=0.5)
plt.text(1955, 82000, 'US Interstate Benchmark (~78k km)', fontsize=9, fontstyle='italic', color='gray')

# Formatting axes
plt.title("Expressway Network Expansion: India vs. USA vs. China\n", fontsize=14, pad=15, fontweight='bold')
plt.xlabel("Year", fontsize=11, labelpad=10)
plt.ylabel("Operational Length in Kilometers", fontsize=11, labelpad=10)
plt.xlim(1950, 2030)
plt.ylim(50, 210000)

# Format y-axis ticks as regular numbers rather than scientific notation
ax = plt.gca()
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, _: f'{int(y):,}'))

plt.grid(True, which="both", ls="--", lw=0.5, alpha=0.6)
plt.legend(loc='upper left', frameon=True, fontsize=8)
plt.tight_layout()

# Display plot
plt.show()
