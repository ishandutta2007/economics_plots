import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# 1. Baseline Parameters (IMF 2026 Estimates)
# ---------------------------------------------------------
start_year = 2026

data = {
    'United States': (94430, 0.0232),
    'European Union': (67957, 0.0130),
    'China': (31596, 0.0441),
    'India': (12801, 0.0648)
}

# ---------------------------------------------------------
# 2. Dynamic Trajectory Generation
# ---------------------------------------------------------
current_year = start_year
years_log = [start_year]
trajectories = {region: [val[0]] for region, val in data.items()}

while True:
    current_year += 1
    years_log.append(current_year)
    
    current_values = {}
    for region, (initial, rate) in data.items():
        t = current_year - start_year
        val = initial * ((1 + rate) ** t)
        trajectories[region].append(val)
        current_values[region] = val
        
    # Stop execution when the trailing country (India) intercepts the leader (US)
    if current_values['India'] >= current_values['United States']:
        convergence_year = current_year
        break

# Convert log tracking to arrays for structural indexing
years_arr = np.array(years_log)
traj_arr = {k: np.array(v) for k, v in trajectories.items()}

# ---------------------------------------------------------
# 3. Intersection Mapping Matrix
# ---------------------------------------------------------
intersections = [
    {"year": 2051, "y_val": traj_arr['China'][years_arr == 2051][0], "label": "China crosses EU", "align": "center"},
    {"year": 2059, "y_val": traj_arr['India'][years_arr == 2059][0], "label": "India crosses EU", "align": "left"},
    {"year": 2072, "y_val": traj_arr['India'][years_arr == 2072][0], "label": "India crosses China", "align": "left"},
    {"year": 2076, "y_val": traj_arr['India'][years_arr == 2076][0], "label": "Full Convergence\n(India crosses US)", "align": "center"}
]

# ---------------------------------------------------------
# 4. Custom Visualization Canvas Pipeline
# ---------------------------------------------------------
plt.figure(figsize=(14, 8.5), dpi=100)
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

colors = {
    'United States': '#1A365D',   # Deep Slate Blue
    'European Union': '#D69E2E',  # Ochre Gold
    'China': '#E53E3E',           # Crimson
    'India': '#319795'            # Deep Teal
}

# Plot Base Trajectories
for region, path in traj_arr.items():
    plt.plot(years_arr, path, label=f"{region} ({data[region][1]*100:.2f}%)", 
             color=colors[region], linewidth=2.5, alpha=0.85)

# A. Annotate 2026 Baseline Starts
for region, (initial, _) in data.items():
    plt.scatter(start_year, initial, color=colors[region], s=50, zorder=4)
    plt.text(start_year - 0.8, initial, f"${initial:,.0f}", 
             ha='right', va='center', fontsize=9, fontweight='semibold', color='#2D3748')

# B. Plot and Highlight Structural Intersection Vectors
for pt in intersections:
    # Anchor point
    plt.scatter(pt["year"], pt["y_val"], color='#2D3748', s=80, zorder=5, edgecolors='white', linewidth=1.5)
    
    # Text Placement logic based on intersection layout density
    x_offset = -2 if pt["align"] == "right" else (2 if pt["align"] == "left" else 0)
    y_offset = pt["y_val"] * 1.08 if pt["align"] == "center" else pt["y_val"] * 0.92
    va_dir = 'bottom' if pt["align"] == "center" else 'top'
    ha_dir = pt["align"] if pt["align"] != "center" else "center"
    
    plt.annotate(
        f'{pt["label"]}\nYear: {pt["year"]}\n${pt["y_val"]:,.0f}',
        xy=(pt["year"], pt["y_val"]),
        xytext=(pt["year"] + x_offset, y_offset),
        arrowprops=dict(arrowstyle="->", color='#4A5568', lw=1, connectionstyle="arc3,rad=0.1"),
        bbox=dict(boxstyle='round,pad=0.4', fc='#F7FAFC', alpha=0.95, ec='#CBD5E0', lw=1),
        fontsize=9,
        fontweight='bold',
        color='#2D3748',
        ha=ha_dir,
        va=va_dir
    )

# Formatting polish
plt.title('Macro Convergence Matrix: Per Capita GDP (PPP) Long-Run Intersection Points', 
          fontsize=16, fontweight='bold', pad=20, color='#1A202C')
plt.xlabel('Projection Horizon Year', fontsize=11, labelpad=10, fontweight='semibold', color='#4A5568')
plt.ylabel('GDP per Capita, PPP (Current International USD)', fontsize=11, labelpad=10, fontweight='semibold', color='#4A5568')
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"${x:,.0f}"))

plt.legend(title='Country & Baseline Compound Rate', loc='upper left', frameon=True, facecolor='white', shadow=True)
plt.xlim(start_year - 4, convergence_year + 4)
plt.ylim(0, max(traj_arr['United States']) * 1.15)
plt.tight_layout()

# Render Pipeline
plt.show()