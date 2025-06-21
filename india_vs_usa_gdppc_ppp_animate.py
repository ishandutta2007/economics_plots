import math
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pandas_datareader import wb

# Get GDP per capita data
countries = ["CHN", "USA"]
indicator = "NY.GDP.PCAP.PP.CD"

df = wb.download(indicator=indicator, country=countries, start=1990, end=2024)
df = df.reset_index().pivot(index="year", columns="country", values=indicator)
df.index = df.index.astype(int)
df["multiple"] = df["United States"] / df["China"]
persistent_years = [1993, 2001, 2013, 2023]

# Create figure and axes
fig, (ax1, ax2) = plt.subplots(
    2, 1, figsize=(12, 8), gridspec_kw={"height_ratios": [2, 1]}
)

# Plot formatting
ax1.set_yscale("log")
ax1.set_xlim(df.index.min(), df.index.max())
ax1.set_ylim(df.min().min() * 0.9, df.max().max() * 1.1)
ax1.grid(True, which="both", ls="--")
ax1.set_title("GDP per capit(PPP)a: China vs USA (1990-2023)")
ax1.set_ylabel("GDP per capita(PPP) (USD)")

ax2.set_ylim(0, df["multiple"].max() * 1.1)
ax2.set_xlim(df.index.min(), df.index.max())
ax2.grid(True)
ax2.set_ylabel("Multiple (USA/China)")
ax2.set_xlabel("Year")

# Initialize elements
(line1,) = ax1.plot([], [], lw=2, label="China")
(line2,) = ax1.plot([], [], lw=2, label="USA")
(ratio_line,) = ax2.plot([], [], lw=2, color="purple", label="USA/China Multiple")
year_text = ax1.text(
    0.9,
    0.05,
    "",
    transform=ax1.transAxes,
    fontsize="xx-large",
    fontweight="extra bold",
    color="darkred",
)
multiple_texts = []


def init():
    return line1, line2, ratio_line, year_text


def animate(i):
    global multiple_texts

    # Clear previous elements
    for txt in multiple_texts:
        txt.remove()
    multiple_texts = []

    if i < len(df):
        years = df.index[: i + 1]
        current_year = years[i]
        line1.set_data(years, df["China"].iloc[: i + 1])
        line2.set_data(years, df["United States"].iloc[: i + 1])
        ratio_line.set_data(years, df["multiple"].iloc[: i + 1])
        y_China = df["China"].iloc[i]
        y_usa = df["United States"].iloc[i]
        current_multiple = df["multiple"].iloc[i]
    else:
        years = df.index[: len(df) - 1 + 1]
        current_year = years[len(df) - 1]
        line1.set_data(years, df["China"].iloc[: len(df) - 1 + 1])
        line2.set_data(years, df["United States"].iloc[: len(df) - 1 + 1])
        ratio_line.set_data(years, df["multiple"].iloc[: len(df) - 1 + 1])
        y_China = df["China"].iloc[len(df) - 1]
        y_usa = df["United States"].iloc[len(df) - 1]
        current_multiple = df["multiple"].iloc[len(df) - 1]

    mid_y = math.exp((math.log(y_China) + math.log(y_usa)) / 2)

    # Create arrow with text on ax1
    arrow = ax1.annotate(
        "",
        xy=(current_year, y_usa),
        xytext=(current_year, y_China),
        arrowprops=dict(arrowstyle="<->", color="red", lw=1.5),
    )
    multiple_text = ax1.text(
        current_year,
        mid_y,
        f"{current_multiple:.1f}x",
        ha="center",
        va="center",
        backgroundcolor="white",
    )
    usa_gdp = ax1.text(
        current_year,
        y_usa,
        f"${y_usa:.0f}",
        ha="left",
        va="bottom",
        backgroundcolor="white",
    )
    China_gdp = ax1.text(
        current_year,
        y_China,
        f"${y_China:.0f}",
        ha="left",
        va="top",
        backgroundcolor="white",
    )

    multiple_texts.extend([usa_gdp, China_gdp, arrow, multiple_text])

    # Add persistent text on ax2 for specific years
    if current_year in persistent_years:
        ax2.text(
            current_year,
            current_multiple,
            f"{current_multiple:.1f}x",
            ha="center",
            va="bottom",
            fontweight="bold",
            color="darkred",
        )
        # Do not append to multiple_texts

    # Update year text
    year_text.set_text(f"{current_year}")

    return line1, line2, ratio_line, year_text


pause_frames = 20
ani = animation.FuncAnimation(
    fig,
    animate,
    frames=len(df) + pause_frames,
    init_func=init,
    blit=False,
    interval=800,
)

# Add legends
ax1.legend()
ax2.legend()

# Save to MP4
Writer = animation.writers["ffmpeg"]
writer = Writer(fps=1, metadata=dict(artist="Me"), bitrate=1800)
ani.save("China_vs_usa_gdp_comparison.mp4", writer=writer)

plt.tight_layout()
plt.show()
