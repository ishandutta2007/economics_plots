import math
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pandas_datareader import wb

# Get GDP data
countries = ["IND", "JP"]
indicator = "NY.GDP.MKTP.CD"

df = wb.download(indicator=indicator, country=countries, start=1992, end=2023)
df = df.reset_index().pivot(index="year", columns="country", values=indicator)
df.loc[2024] = {'India': 3.567552e+12, 'Japan': 4.104495e+12}
df.loc[2025] = {'India': 4.192345e+12, 'Japan': 4.191365e+12}
df.loc[2026] = {'India': 4.593552e+12, 'Japan': 4.373495e+12}

print(df.tail())
df.index = df.index.astype(int)
df["multiple_japan_india"] = df["Japan"] / df["India"]
persistent_years = [1993, 2000, 2008, 2014, 2019, 2025]

# Create figure and axes
fig, (ax1, ax2) = plt.subplots(
    2, 1, figsize=(12, 8), gridspec_kw={"height_ratios": [2, 1]}
)

# Plot formatting
# ax1.set_yscale("log")
ax1.set_xlim(df.index.min(), df.index.max())
ax1.set_ylim(10**11, df.max().max() * 1.1)
ax1.grid(True, which="both", ls="--")
ax1.set_title("GDP: India vs Japan (1990-2025)", fontdict={'fontsize':20, 'fontweight':'bold'})
ax1.set_ylabel("GDP (USD)")

# ax2.set_ylim(0, max(df["multiple_japan_india"].max(), df["multiple_japan_chn"].max()) * 1.1)
ax2.set_ylim(0, df["multiple_japan_india"].max() * 1.1)
ax2.set_xlim(df.index.min(), df.index.max())
ax2.grid(True)
ax2.set_ylabel("Multiple")
ax2.set_xlabel("Year")

# Initialize elements
(line1,) = ax1.plot([], [], lw=2, label="India")
(line2,) = ax1.plot([], [], lw=2, label="Japan")
(ratio_line_japan,) = ax2.plot([], [], lw=2, color="purple", label="Japan/India Multiple")
year_text = ax1.text(0.9, 0.05, "", transform=ax1.transAxes, fontsize='xx-large', fontweight='extra bold', color="darkred")
multiple_texts = []
cached_annotations = None  # Store 2025 annotation data

def init():
    line1.set_data([], [])
    line2.set_data([], [])
    ratio_line_japan.set_data([], [])
    year_text.set_text("")
    return line1, line2, ratio_line_japan, year_text

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
    line2.set_data(years, df["Japan"].iloc[: current_idx + 1])
    ratio_line_japan.set_data(years, df["multiple_japan_india"].iloc[: current_idx + 1])

    # Use cached annotations for pause frames
    if i >= len(df) and cached_annotations is not None:
        y_japan, y_india, current_multiple_japan_india = cached_annotations
    else:
        # Data for annotations
        y_india = df["India"].iloc[current_idx]
        y_japan = df["Japan"].iloc[current_idx]
        current_multiple_japan_india = df["multiple_japan_india"].iloc[current_idx]

        # Cache annotations when reaching 2025
        if current_year == 2025:
            cached_annotations = (y_japan, y_india, current_multiple_japan_india)

    # Arrow and text for India vs Japan
    mid_y_japan = math.exp((math.log(y_india) + math.log(y_japan)) / 2)
    arrow_japan = ax1.annotate(
        "",
        xy=(current_year, y_japan),
        xytext=(current_year, y_india),
        arrowprops=dict(arrowstyle="<->", color="red", lw=1.5),
    )
    multiple_text_japan = ax1.text(
        current_year,
        mid_y_japan,
        f"{current_multiple_japan_india:.1f}x",
        ha="center",
        va="center",
        backgroundcolor="white",
    )

    # GDP labels for Japan and India
    japan_gdp = ax1.text(
        current_year,
        y_japan,
        f"Japan: ${(y_japan/10**12):.3f}T",
        ha="left",
        va="bottom",
        fontweight='bold',
        backgroundcolor="white",
    )
    india_gdp = ax1.text(
        current_year,
        y_india,
        f"India: ${(y_india/10**12):.3f}T",
        ha="left",
        va="top",
        fontweight='bold',
        backgroundcolor="white",
    )

    multiple_texts.extend([japan_gdp, india_gdp, arrow_japan, multiple_text_japan])

    # Add persistent text on ax2 for specific years
    if current_year in persistent_years:
        ax2.text(
            current_year,
            current_multiple_japan_india,
            f"{current_multiple_japan_india:.1f}x",
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

    return line1, line2, ratio_line_japan, year_text

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
ani.save("india_vs_japan_gdp_comparison.mp4", writer=writer)

plt.tight_layout()
plt.show()