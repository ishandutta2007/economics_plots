import math
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pandas_datareader import wb

# Get GDP per capita data
countries = ["IND", "CHN", "USA"]
indicator = "NY.GDP.PCAP.CD"

df = wb.download(indicator=indicator, country=countries, start=1973, end=2023)
df = df.reset_index().pivot(index="year", columns="country", values=indicator)
df.index = df.index.astype(int)
df["multiple_usa_india"] = df["United States"] / df["India"]
df["multiple_chn_india"] = df["China"] / df["India"]
df["multiple_usa_chn"] = df["United States"] / df["China"]
persistent_years = [1993, 2001, 2013, 2023]

# Create figure and axes
fig, (ax1, ax2) = plt.subplots(
    2, 1, figsize=(12, 8), gridspec_kw={"height_ratios": [2, 1]}
)

# Plot formatting
ax1.set_yscale("log")
ax1.set_xlim(df.index.min(), df.index.max())
ax1.set_ylim(100, df.max().max() * 1.1)
ax1.grid(True, which="both", ls="--")
ax1.set_title("GDP per capita: India vs USA vs China (1973-2023)")
ax1.set_ylabel("GDP per capita (USD)")

ax2.set_ylim(0, max(df["multiple_usa_india"].max(), df["multiple_usa_chn"].max()) * 1.1)
ax2.set_xlim(df.index.min(), df.index.max())
ax2.grid(True)
ax2.set_ylabel("Multiple")
ax2.set_xlabel("Year")

# Initialize elements
(line1,) = ax1.plot([], [], lw=2, label="India")
(line2,) = ax1.plot([], [], lw=2, label="USA")
(line3,) = ax1.plot([], [], lw=2, label="China")
(ratio_line_usa,) = ax2.plot([], [], lw=2, color="purple", label="USA/India Multiple")
(ratio_line_usa_chn,) = ax2.plot([], [], lw=2, color="blue", label="USA/China Multiple")
year_text = ax1.text(0.9, 0.05, "", transform=ax1.transAxes, fontsize='xx-large', fontweight='extra bold', color="darkred")
multiple_texts = []
cached_annotations = None  # Store 2023 annotation data

def init():
    line1.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])
    ratio_line_usa.set_data([], [])
    ratio_line_usa_chn.set_data([], [])
    year_text.set_text("")
    return line1, line2, line3, ratio_line_usa, ratio_line_usa_chn, year_text

def animate(i):
    global multiple_texts, cached_annotations

    # Clear previous annotations
    for txt in multiple_texts:
        txt.remove()
    multiple_texts = []

    # Determine the frame's year and data
    current_idx = min(i, len(df) - 1)
    current_year = df.index[current_idx]
    years = df.index[: current_idx + 1]

    # Set line data
    line1.set_data(years, df["India"].iloc[: current_idx + 1])
    line2.set_data(years, df["United States"].iloc[: current_idx + 1])
    line3.set_data(years, df["China"].iloc[: current_idx + 1])
    ratio_line_usa.set_data(years, df["multiple_usa_india"].iloc[: current_idx + 1])
    ratio_line_usa_chn.set_data(years, df["multiple_usa_chn"].iloc[: current_idx + 1])

    # Use cached annotations for pause frames
    if i >= len(df) and cached_annotations is not None:
        y_usa, y_chn, y_india, current_multiple_usa_india, current_multiple_chn_india, current_multiple_usa_chn = cached_annotations
    else:
        # Data for annotations
        y_india = df["India"].iloc[current_idx]
        y_usa = df["United States"].iloc[current_idx]
        y_chn = df["China"].iloc[current_idx]
        current_multiple_usa_india = df["multiple_usa_india"].iloc[current_idx]
        current_multiple_chn_india = df["multiple_chn_india"].iloc[current_idx]
        current_multiple_usa_chn = df["multiple_usa_chn"].iloc[current_idx]

        # Cache annotations when reaching 2023
        if current_year == 2023:
            cached_annotations = (y_usa, y_chn, y_india, current_multiple_usa_india, current_multiple_chn_india, current_multiple_usa_chn)

    # Conditional arrow and text for USA based on year
    if current_year <= 1991:
        # Arrow and text for India vs USA
        mid_y_usa = math.exp((math.log(y_india) + math.log(y_usa)) / 2)
        arrow_usa = ax1.annotate(
            "",
            xy=(current_year, y_usa),
            xytext=(current_year, y_india),
            arrowprops=dict(arrowstyle="<->", color="red", lw=1.5),
        )
        multiple_text_usa = ax1.text(
            current_year,
            mid_y_usa,
            f"{current_multiple_usa_india:.1f}x",
            ha="center",
            va="center",
            backgroundcolor="white",
        )
    else:
        # Arrow and text for China vs USA
        mid_y_usa = math.exp((math.log(y_chn) + math.log(y_usa)) / 2)
        arrow_usa = ax1.annotate(
            "",
            xy=(current_year, y_usa),
            xytext=(current_year, y_chn),
            arrowprops=dict(arrowstyle="<->", color="red", lw=1.5),
        )
        multiple_text_usa = ax1.text(
            current_year,
            mid_y_usa,
            f"{current_multiple_usa_chn:.1f}x",
            ha="center",
            va="center",
            backgroundcolor="white",
        )

    # GDP labels for USA and India
    usa_gdp = ax1.text(
        current_year,
        y_usa,
        f"${y_usa:.0f}",
        ha="left",
        va="bottom",
        backgroundcolor="white",
    )
    india_gdp = ax1.text(
        current_year,
        y_india,
        f"${y_india:.0f}",
        ha="left",
        va="top",
        backgroundcolor="white",
    )

    # Arrow and text for China vs India
    mid_y_chn = math.exp((math.log(y_india) + math.log(y_chn)) / 2)
    arrow_chn = ax1.annotate(
        "",
        xy=(current_year, y_chn),
        xytext=(current_year, y_india),
        arrowprops=dict(arrowstyle="<->", color="green", lw=1.5),
    )
    multiple_text_chn = ax1.text(
        current_year + 1,
        mid_y_chn,
        f"{current_multiple_chn_india:.1f}x",
        ha="center",
        va="center",
        backgroundcolor="white",
    )
    chn_gdp = ax1.text(
        current_year,
        y_chn,
        f"${y_chn:.0f}",
        ha="left",
        va="top" if y_chn < y_usa else "bottom",
        backgroundcolor="white",
    )

    multiple_texts.extend([usa_gdp, india_gdp, chn_gdp, arrow_usa, multiple_text_usa, arrow_chn, multiple_text_chn])

    # Add persistent text on ax2 for specific years
    if current_year in persistent_years:
        ax2.text(
            current_year,
            current_multiple_usa_india,
            f"{current_multiple_usa_india:.1f}x",
            ha="center",
            va="bottom",
            fontweight='bold',
            color="darkred",
        )
        ax2.text(
            current_year,
            current_multiple_usa_chn,
            f"{current_multiple_usa_chn:.1f}x",
            ha="center",
            va="bottom",
            fontweight='bold',
            color="darkred",
        )

    # Update year text
    year_text.set_text(f"{current_year}")

    # Debug output for pause frames
    if i >= len(df):
        print(f"Pause frame {i - len(df) + 1}: year={current_year}, annotations={len(multiple_texts)}")

    return line1, line2, line3, ratio_line_usa, ratio_line_usa_chn, year_text

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
ani.save("india_vs_usa_china_gdp_comparison.mp4", writer=writer)

plt.tight_layout()
plt.show()