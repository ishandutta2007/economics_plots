import matplotlib.pyplot as plt
import numpy as np

# --- Existing Data ---
# Data for Engineering (Seats in Lakhs)
years_eng_str = [
    '2014-15', '2015-16', '2016-17', '2017-18', '2018-19', 
    '2019-20', '2020-21', '2021-22', '2022-23', '2023-24', '2024-25'
]
seats_eng = [
    17.05, 16.30, 15.56, 14.75, 14.04, 
    13.28, 12.86, 12.54, 12.74, 13.50, 14.90
]
years_eng_numeric = [int(y.split('-')[0]) for y in years_eng_str]

# Medical data (MBBS + BDS converted to Lakhs) 
medical_years_str = ['2014-15', '2017-18', '2021-22', '2022-23', '2023-24', '2024-25']
seats_med = [0.765, 0.940, 1.102, 1.194, 1.368, 1.461]
medical_years_numeric = [int(y.split('-')[0]) for y in medical_years_str]

# --- Projection ---
last_known_year_numeric = 2024
projection_end_year = 2047

# --- Engineering Projection ---
# Use trend from last 10 years (2015-2024)
eng_recent_years = years_eng_numeric[-10:]
eng_recent_seats = seats_eng[-10:]
eng_fit_coeffs = np.polyfit(eng_recent_years, eng_recent_seats, 1)
eng_growth_rate = eng_fit_coeffs[0]

projected_years_numeric = np.arange(last_known_year_numeric, projection_end_year + 1)
projected_seats_eng = [seats_eng[-1]]
for i in range(1, len(projected_years_numeric)):
    projected_seats_eng.append(projected_seats_eng[-1] + eng_growth_rate)

# --- Medical Projection ---
# Use linear regression on all available points
med_fit_coeffs = np.polyfit(medical_years_numeric, seats_med, 1)
med_growth_rate = med_fit_coeffs[0]

projected_seats_med = [seats_med[-1]]
for i in range(1, len(projected_years_numeric)):
    projected_seats_med.append(projected_seats_med[-1] + med_growth_rate)

# --- Prepare for Plotting ---
projected_years_str = [f"{y}-{y+1-2000}" for y in projected_years_numeric]

# --- Plotting ---
plt.figure(figsize=(14, 8))

# Plotting Actual Data (Solid Line)
plt.plot(years_eng_str, seats_eng, marker='o', label='Engineering Intake (Actual)', color='#4cabb1', linewidth=2.5, solid_capstyle='round')
plt.plot(medical_years_str, seats_med, marker='s', label='Medical Intake (Actual)', color='#d62728', linewidth=2.5, solid_capstyle='round')

# Plotting Projected Data (Dotted Line)
plt.plot(projected_years_str, projected_seats_eng, linestyle='--', label='Engineering Intake (Projected)', color='#4cabb1', linewidth=2.5)
plt.plot(projected_years_str, projected_seats_med, linestyle='--', label='Medical Intake (Projected)', color='#d62728', linewidth=2.5)

# Annotating original data points
for i, txt in enumerate(seats_eng):
    plt.annotate(f'{txt:.2f}', (years_eng_str[i], seats_eng[i]), textcoords="offset points", 
                 xytext=(0,10), ha='center', fontsize=9, fontweight='bold', color='#2a5e61')

for i, txt in enumerate(seats_med):
    plt.annotate(f'{txt:.3f}', (medical_years_str[i], seats_med[i]), textcoords="offset points", 
                 xytext=(0,10), ha='center', fontsize=9, fontweight='bold', color='#b22222')

# Annotate final projected values for 2047
plt.annotate(f'{projected_seats_eng[-1]:.2f}L', (projected_years_str[-1], projected_seats_eng[-1]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=10, fontweight='bold', color='#2a5e61')
plt.annotate(f'{projected_seats_med[-1]:.2f}L', (projected_years_str[-1], projected_seats_med[-1]), textcoords="offset points", xytext=(0,-20), ha='center', fontsize=10, fontweight='bold', color='#b22222')

# --- Styling ---
plt.title('Engineering vs Medical Seats in India (with Projections to 2047)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Academic Year', fontsize=12)
plt.ylabel('Seats (in Lakhs)', fontsize=12)
# plt.yscale('log')

# Create a combined list of x-axis labels for proper ticking
all_years_str = sorted(list(set(years_eng_str + projected_years_str)))
# Select a subset of ticks to prevent overcrowding
tick_years = all_years_str[::4] # Every 4th year
if all_years_str[-1] not in tick_years:
    tick_years.append(all_years_str[-1]) # Ensure the last year is a tick

plt.xticks(ticks=tick_years, rotation=45)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='best')
plt.ylim(bottom=0.5) # Set bottom for log scale, let top be auto

plt.tight_layout()
# plt.savefig('india_engg_vs_med_seats_2047.png')
plt.show()
