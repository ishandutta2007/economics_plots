import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
gdp_per_capita_2024 = 80300  # USD
growth_rate = 0.02
start_year = 2024
end_year = 2047
years = np.arange(start_year, end_year + 1)
gdp_per_capita = gdp_per_capita_2024 * (1 + growth_rate) ** (years - start_year)

# Set up plot
fig, ax = plt.subplots()
line, = ax.plot([], [], 'bo-', linewidth=2)
text = ax.text(0, 0, '', fontsize=12, ha='left', va='bottom')
ax.set_xlim(start_year, end_year)
ax.set_ylim(min(gdp_per_capita)*0.95, max(gdp_per_capita)*1.05)
ax.set_title("Projected US GDP Per Capita (2024–2047)")
ax.set_xlabel("Year")
ax.set_ylabel("GDP Per Capita (USD)")

def init():
    line.set_data([], [])
    text.set_position((0, 0))
    text.set_text('')
    return line, text

def animate(i):
    x = years[:i+1]
    y = gdp_per_capita[:i+1]
    line.set_data(x, y)
    if i > 0:
        text.set_position((x[-1], y[-1]))
        text.set_text(f"${y[-1]:,.0f}")
    return line, text

pause_frames=10
ani = animation.FuncAnimation(fig, animate, 
    init_func=init, frames=len(years) + pause_frames, interval=200, blit=True)
# Save to MP4
Writer = animation.writers["ffmpeg"]
writer = Writer(fps=1, metadata=dict(artist="Me"), bitrate=1800)
ani.save("usa_gdp.mp4", writer=writer)

plt.show()
