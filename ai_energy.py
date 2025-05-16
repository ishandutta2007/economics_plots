import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from scipy.optimize import curve_fit

# --- Data ---
years_historical = np.array([2020, 2021, 2022, 2023, 2024])
years_full_range = np.arange(2020, 2051)

# Historical AI Energy Consumption (TWh)
ai_energy_hist_values = np.array([11.0, 15.9, 23.0, 33.3, 48.2])

# Historical Total Electricity Generation (TWh)
total_electricity_hist_values = np.array([26931, 28454, 28830, 29665, 30700])

# --- Curve Fitting Function ---
def exponential_func(x, a, b):
    return a * np.exp(b * x)

# --- Fit AI Energy Consumption Data ---
# Normalize x for fitting (years since 2020)
x_fit_ai = years_historical - 2020
popt_ai, pcov_ai = curve_fit(exponential_func, x_fit_ai, ai_energy_hist_values, p0=[10, 0.4])
a_ai, b_ai = popt_ai
print(f"AI Energy Fitted Parameters: a={a_ai:.2f}, b={b_ai:.4f}")
print(f"Implied AI CAGR from fit: {(np.exp(b_ai) - 1)*100:.2f}%")


# --- Fit Total Electricity Generation Data ---
x_fit_total = years_historical - 2020
popt_total, pcov_total = curve_fit(exponential_func, x_fit_total, total_electricity_hist_values, p0=[25000, 0.03])
a_total, b_total = popt_total
print(f"Total Electricity Fitted Parameters: a={a_total:.2f}, b={b_total:.4f}")
print(f"Implied Total Electricity CAGR from fit: {(np.exp(b_total) - 1)*100:.2f}%")

# --- Generate Full Data Series (Historical + Projected) ---
ai_energy_full = []
total_electricity_full = []

for year in years_full_range:
    year_index = year - 2020
    if year <= 2024:
        # Find the index in historical years
        hist_idx = np.where(years_historical == year)[0]
        ai_energy_full.append(ai_energy_hist_values[hist_idx[0]] if len(hist_idx) > 0 else np.nan)
        total_electricity_full.append(total_electricity_hist_values[hist_idx[0]] if len(hist_idx) > 0 else np.nan)
    else:
        ai_energy_full.append(exponential_func(year_index, a_ai, b_ai))
        total_electricity_full.append(exponential_func(year_index, a_total, b_total))

# Convert to numpy arrays
ai_energy_full = np.array(ai_energy_full)
total_electricity_full = np.array(total_electricity_full)

# Print projected 2050 values to illustrate the extrapolation
print(f"\nProjected AI Energy Consumption in 2050 (by pure extrapolation): {ai_energy_full[-1]:,.2f} TWh")
print(f"Projected Total Electricity Generation in 2050 (by pure extrapolation): {total_electricity_full[-1]:,.2f} TWh")


# --- Plotting ---
fig, ax1 = plt.subplots(figsize=(14, 8))

# Setup primary y-axis (Total Electricity)
color_total = 'tab:blue'
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Global Total Electricity Generation (TWh)', color=color_total, fontsize=12)
ax1.tick_params(axis='y', labelcolor=color_total, labelsize=10)
ax1.tick_params(axis='x', labelsize=10)
ax1.grid(True, linestyle='--', alpha=0.7, axis='y') # Grid for primary axis

# Setup secondary y-axis (AI Consumption)
ax2 = ax1.twinx()
color_ai = 'tab:red'
ax2.set_ylabel('Global AI Energy Consumption (TWh)', color=color_ai, fontsize=12)
ax2.tick_params(axis='y', labelcolor=color_ai, labelsize=10)
# No separate grid for ax2 to avoid clutter, or style differently if needed

# Lines for the animation
line_total, = ax1.plot([], [], lw=2.5, color=color_total, label='Total Electricity Generation')
line_ai, = ax2.plot([], [], lw=2.5, color=color_ai, label='AI Energy Consumption (Extrapolated)', linestyle='--')

# Year text annotation
year_text = ax1.text(0.5, 1.05, '', transform=ax1.transAxes, fontsize=14, fontweight='bold', ha='center')

# Set y-limits: Use dynamic scaling for animation or pre-calculate max
# For animation, it's often better to fix limits if the final scale is known and very large
# Otherwise, the axes will rescale dramatically during animation.
# Let's fix them to the projected 2050 values from this extrapolation.
ax1.set_ylim(0, total_electricity_full[-1] * 1.1 if not np.isnan(total_electricity_full[-1]) else 60000)
ax2.set_ylim(0, ai_energy_full[-1] * 1.1 if not np.isnan(ai_energy_full[-1]) else 1000) # This will be very large!
ax1.set_xlim(years_full_range[0], years_full_range[-1])


# Add legend
handles, labels = [], []
for ax in [ax1, ax2]:
    for handle, label in zip(*ax.get_legend_handles_labels()):
        handles.append(handle)
        labels.append(label)
fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 0.95), ncol=2, fontsize=10)


plt.title('Global Energy Projection via Extrapolation of 2020-2024 Trends', fontsize=16, pad=40)
fig.tight_layout(rect=[0, 0, 1, 0.9]) # Adjust layout to make room for title and legend

# Display a warning about the AI projection methodology on the plot
plt.figtext(0.5, 0.01,
            "Warning: AI energy projection is a direct exponential extrapolation of 5-year data (2020-2024)\n"
            "and likely results in unrealistically high values for later years.",
            ha="center", va="bottom", fontsize=8, color="red", style="italic")


# Animation function
def init():
    line_total.set_data([], [])
    line_ai.set_data([], [])
    year_text.set_text('')
    return line_total, line_ai, year_text

def animate(i):
    current_year_index = i
    
    x_data = years_full_range[:current_year_index+1]
    y_total_data = total_electricity_full[:current_year_index+1]
    y_ai_data = ai_energy_full[:current_year_index+1]
    
    line_total.set_data(x_data, y_total_data)
    line_ai.set_data(x_data, y_ai_data)
    
    # Update Y-axis limits dynamically if not pre-set, or manage fixed limits carefully
    # With fixed limits for the full range, this part is not needed for limits,
    # but could be used if you wanted dynamic Y scaling (can be jarring).

    year_text.set_text(f'Year: {years_full_range[current_year_index]}')
    
    return line_total, line_ai, year_text

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=len(years_full_range),
                              init_func=init, blit=True, interval=150, repeat=False)

# To save the animation, you might need ffmpeg or another writer installed:
# ani.save('energy_trends_extrapolation.gif', writer='pillow', fps=10)
# ani.save('energy_trends_extrapolation.mp4', writer='ffmpeg', fps=10)

plt.show()
