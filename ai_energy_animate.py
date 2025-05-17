import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from scipy.optimize import curve_fit
import matplotlib # <--- Explicitly importing base matplotlib

# --- Data (2015-2024 Historical) ---
years_historical = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024])
years_full_range = np.arange(2015, 2045)

ai_energy_hist_values = np.array([
    1.73, 2.51, 3.63, 5.25, 7.60, 11.0, 15.9, 23.0, 33.3, 48.2
])
total_electricity_hist_values = np.array([
    24002, 24528, 25271, 26159, 26936, 26931, 28454, 28830, 29665, 30700
])

# --- Curve Fitting Function ---
def exponential_func(x, a, b):
    return a * np.exp(b * x)

x_fit_common = years_historical - years_historical[0]
popt_ai, pcov_ai = curve_fit(exponential_func, x_fit_common, ai_energy_hist_values, p0=[ai_energy_hist_values[0], 0.4], maxfev=5000)
a_ai, b_ai = popt_ai
print(f"AI Energy Fitted Parameters (10yr hist): a={a_ai:.2f}, b={b_ai:.4f}, CAGR: {(np.exp(b_ai) - 1)*100:.2f}%")

# Corrected line from previous error: Changed maxfeev to maxfev
popt_total, pcov_total = curve_fit(exponential_func, x_fit_common, total_electricity_hist_values, p0=[total_electricity_hist_values[0], 0.03], maxfev=5000)
a_total, b_total = popt_total
print(f"Total Electricity Fitted Parameters (10yr hist): a={a_total:.2f}, b={b_total:.4f}, CAGR: {(np.exp(b_total) - 1)*100:.2f}%")

ai_energy_full = []
total_electricity_full = []
for year in years_full_range:
    year_index_from_start_hist = year - years_historical[0]
    if year <= years_historical[-1]:
        hist_idx = np.where(years_historical == year)[0]
        ai_val = ai_energy_hist_values[hist_idx[0]] if len(hist_idx) > 0 else np.nan
        total_val = total_electricity_hist_values[hist_idx[0]] if len(hist_idx) > 0 else np.nan
    else:
        ai_val = exponential_func(year_index_from_start_hist, a_ai, b_ai)
        total_val = exponential_func(year_index_from_start_hist, a_total, b_total)
    ai_energy_full.append(ai_val)
    total_electricity_full.append(total_val)

ai_energy_full = np.array(ai_energy_full)
total_electricity_full = np.array(total_electricity_full)
print(f"\nProjected AI Energy in 2050 (10yr hist extrap): {ai_energy_full[-1]:,.0f} TWh")
print(f"Projected Total Electricity in 2050 (10yr hist extrap): {total_electricity_full[-1]:,.0f} TWh")

# --- Plotting ---
fig, ax1 = plt.subplots(figsize=(9, 16)) # Increased figure size for clarity

color_total = 'tab:blue'
color_ai = 'tab:red'

ax1.set_xlabel('Year', fontsize=14)
# ax1.set_ylabel('Energy (TWh)', color='black', fontsize=14) # Single Y-axis label
ax1.set_ylabel('Energy (TWh) [Log Scale]', color='black', fontsize=14) # Single Y-axis label
ax1.tick_params(axis='y', labelcolor='black', labelsize=12)
ax1.tick_params(axis='x', labelsize=12)
ax1.set_yscale('log')
ax1.grid(True, which="both", linestyle='--', alpha=0.6, axis='y')

# Lines for the animation - both plotted on ax1
line_total, = ax1.plot([], [], lw=2.5, color=color_total, label='Total Electricity Generation (Line)')
line_ai, = ax1.plot([], [], lw=2.5, color=color_ai, label='AI Energy Consumption (Line - Extrap.)', linestyle='--')

# Scatter plots for markers every 5 years - both plotted on ax1
# scatter_total_markers = ax1.scatter([], [], s=80, facecolors=color_total, edgecolors='black', alpha=0.7, zorder=5, label='Total Elec. Points (5yr)')
# scatter_ai_markers = ax1.scatter([], [], s=80, facecolors=color_ai, edgecolors='black', alpha=0.7, zorder=5, label='AI Energy Points (5yr)')

year_text = ax1.text(0.5, 1.02, '', transform=ax1.transAxes, fontsize=20, fontweight='bold', ha='center')

# Set Y-axis limits for the single log scale
min_val_overall = np.min(ai_energy_full[~np.isnan(ai_energy_full) & (ai_energy_full > 0)])
max_val_overall = np.max(total_electricity_full[~np.isnan(total_electricity_full)])
if min_val_overall > 0 and max_val_overall > 0 : # Ensure valid min/max for log
    ax1.set_ylim(min_val_overall * 0.5, max_val_overall * 1.5) # Wider margin for text
else: # Fallback
    ax1.set_ylim(0.1, 1e8)


ax1.set_xlim(years_full_range[0], years_full_range[-1])

fig.legend(loc='upper center', bbox_to_anchor=(0.65, 0.17), ncol=1, fontsize=18) # Combined legend
plt.title('Global Energy vs AI Energy', fontsize=22, pad=45, color='darkred', fontweight='bold',)
fig.tight_layout(rect=[0, 0.05, 1, 0.88])

# plt.figtext(0.5, 0.01,
#             "Warning: AI values (2015-19 est.). Projections are direct exponential extrapolations of 2015-2024 trends.\n"
#             "AI energy projection results in extremely high future values. Log scale used for visualization.",
#             ha="center", va="bottom", fontsize=9, color="darkred", style="italic")

# Store marker data and text annotations
marker_total_data = {'x': [], 'y': [], 'texts': []}
marker_ai_data = {'x': [], 'y': [], 'texts': []}

def init():
    line_total.set_data([], [])
    # line_ai.set_data([], [])
    # scatter_total_markers.set_offsets(np.empty((0, 2)))
    # scatter_ai_markers.set_offsets(np.empty((0, 2)))
    year_text.set_text('')
    # Clear previous texts
    for txt_list in [marker_total_data['texts'], marker_ai_data['texts']]:
        for t in txt_list:
            t.set_visible(False) # Hide old texts
        txt_list.clear()
    # return line_total, line_ai, scatter_total_markers, scatter_ai_markers, year_text # Text artists not returned for blit=False
    return line_total, line_ai, year_text # Text artists not returned for blit=False

def animate(i):
    current_year_anim = years_full_range[i]

    x_line_data = years_full_range[:i+1]
    y_total_line_data = total_electricity_full[:i+1]
    y_ai_line_data = ai_energy_full[:i+1]

    valid_total_line = y_total_line_data > 0
    line_total.set_data(x_line_data[valid_total_line], y_total_line_data[valid_total_line])

    valid_ai_line = y_ai_line_data > 0
    line_ai.set_data(x_line_data[valid_ai_line], y_ai_line_data[valid_ai_line])

    # Clear previous texts for this frame to prevent overlap if not using blitting for texts
    # Alternatively, make them invisible and reuse, but clearing is simpler with blit=False
    for txt_list_key in ['texts_total_dynamic', 'texts_ai_dynamic']:
        if hasattr(fig, txt_list_key):
            for t_obj in getattr(fig, txt_list_key):
                t_obj.remove()
            delattr(fig, txt_list_key)
    fig.texts_total_dynamic = []
    fig.texts_ai_dynamic = []


    # Add markers and text if current year is a 5-year interval point
    # Markers are managed by set_offsets, text needs to be added per frame if not blitted
    # Or, manage text artists persistently like scatter points (more complex for blitting)
    # For simplicity with blit=False, let's add text if it's a marker year

    current_marker_points_total_x = []
    current_marker_points_total_y = []
    current_marker_points_ai_x = []
    current_marker_points_ai_y = []

    # Rebuild all visible markers and texts up to current frame
    # This part ensures that texts are only drawn for existing markers in the current frame

    temp_texts_total = []
    temp_texts_ai = []

    for frame_idx in range(i + 1):
        year_at_frame = years_full_range[frame_idx]
        if year_at_frame % 5 == 0:
            val_total_at_frame = total_electricity_full[frame_idx]
            val_ai_at_frame = ai_energy_full[frame_idx]

            if not np.isnan(val_total_at_frame) and val_total_at_frame > 0:
                current_marker_points_total_x.append(year_at_frame)
                current_marker_points_total_y.append(val_total_at_frame)
                # Add text next to the point for total electricity
                txt = ax1.text(year_at_frame, val_total_at_frame, f" {val_total_at_frame:,.0f}",
                               fontsize=18, color=color_total, va='top', ha='left',
                               # path_effects=[matplotlib.patheffects.withStroke(linewidth=0.5, foreground='w')]
                               ) # Uses matplotlib.patheffects
                temp_texts_total.append(txt)


            if not np.isnan(val_ai_at_frame) and val_ai_at_frame > 0:
                current_marker_points_ai_x.append(year_at_frame)
                current_marker_points_ai_y.append(val_ai_at_frame)
                # Add text next to the point for AI
                txt = ax1.text(year_at_frame, val_ai_at_frame, f" {val_ai_at_frame:,.0f}",
                               fontsize=18, color=color_ai, va='top', ha='left',
                               # path_effects=[matplotlib.patheffects.withStroke(linewidth=0.5, foreground='w')]
                               ) # Uses matplotlib.patheffects
                temp_texts_ai.append(txt)

    # Update scatter plot offsets
    # if current_marker_points_total_x:
    #     scatter_total_markers.set_offsets(np.c_[current_marker_points_total_x, current_marker_points_total_y])
    # else:
    #     scatter_total_markers.set_offsets(np.empty((0, 2)))

    # if current_marker_points_ai_x:
    #     scatter_ai_markers.set_offsets(np.c_[current_marker_points_ai_x, current_marker_points_ai_y])
    # else:
    #     scatter_ai_markers.set_offsets(np.empty((0, 2)))

    # Store dynamic texts to remove them in the next frame to avoid clutter
    # This is one way to handle text in animations without blitting them directly
    if hasattr(fig, 'dynamic_texts_artists'):
        for t in fig.dynamic_texts_artists:
            t.remove()
    fig.dynamic_texts_artists = temp_texts_total + temp_texts_ai

    year_text.set_text(f'Year: {current_year_anim}')

    # Return all artists that change or are created in animate if blit=True
    # For blit=False, it's mainly for structure, system redraws everything
    # return line_total, line_ai, scatter_total_markers, scatter_ai_markers, year_text, *fig.dynamic_texts_artists
    return line_total, line_ai, year_text, *fig.dynamic_texts_artists

pause_frames = 0
ani = animation.FuncAnimation(fig, animate, frames=len(years_full_range) + pause_frames,
                              init_func=init, blit=False, interval=200, repeat=False) # blit=False chosen

# ani.save('energy_trends_single_yaxis_log_markers_values.gif', writer='pillow', fps=7)
# ani.save('energy_trends_single_yaxis_log_markers_values.mp4', writer='ffmpeg', fps=7)
# Save to MP4
Writer = animation.writers["ffmpeg"]
writer = Writer(fps=1, metadata=dict(artist="Me"), bitrate=1800)
ani.save("energy_trends_single_yaxis_log_markers_values.mp4", writer=writer)

# plt.show()
