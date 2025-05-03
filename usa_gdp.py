import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# GDP data
gdp_per_capita_2024 = 80300  # USD
growth_rate = 0.02
start_year = 2024
end_year = 2047
years = np.arange(start_year, end_year + 1)
gdp_per_capita = gdp_per_capita_2024 * (1 + growth_rate) ** (years - start_year)

# Set up plot
fig, ax = plt.subplots()
line, = ax.plot([], [], 'bo-', linewidth=2)
ax.set_xlim(start_year, end_year)
ax.set_ylim(min(gdp_per_capita)*0.95, max(gdp_per_capita)*1.05)
ax.set_title("Projected US GDP Per Capita (2024–2047)")
ax.set_xlabel("Year")
ax.set_ylabel("GDP Per Capita (USD)")

def init():
    line.set_data([], [])
    return line,

def animate(i):
    x = years[:i+1]
    y = gdp_per_capita[:i+1]
    line.set_data(x, y)
    return line,

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=len(years), interval=200, blit=True)

plt.show()
