import matplotlib.pyplot as plt
import numpy as np

# Actual data points (in millions) based on provided information
years_historical = [2023, 2024, 2025]  # Example years with available data/estimates
gcc_jobs_historical = [1.6, 1.9, 2.1]  # GCC jobs (using estimates from various reports)
it_services_jobs_historical = [5.4, 5.4, 5.5]  # IT services jobs (reflecting slow growth/stagnation)

# Future projection years
extrapolation_years = np.arange(2026, 2035)  # Extending projection to potentially see the crossover

# Growth rate assumptions (based on reports and projections suggesting a crossover)
# GCCs are showing strong growth, while IT services hiring has slowed.
# For illustration purposes, the assumptions are:
# - GCCs continue with robust growth (e.g., 15-20% growth per year in net additions).
# - IT services growth significantly slows down, potentially even with minor attrition or very low net additions.
#   Some reports highlight a "silent collapse" of entry-level jobs due to automation and changing models.
#   A credit rating agency predicts a significant recovery only in the latter half of FY2025-26 for IT firms.

# For a potential crossover to occur, the IT services line needs to flatten or decline,
# while the GCC line maintains a steep upward trend.
# The growth rates are adjusted to reflect this.
gcc_annual_addition = 0.25 # Million jobs per year (estimate for robust growth)
it_services_annual_addition = 0.05 # Million jobs per year (estimate for slow growth/stagnation)

# Extrapolate GCC jobs
extrapolated_gcc_jobs = [gcc_jobs_historical[-1]]
for year in extrapolation_years:
    extrapolated_gcc_jobs.append(extrapolated_gcc_jobs[-1] + gcc_annual_addition)

# Extrapolate IT services jobs
extrapolated_it_services_jobs = [it_services_jobs_historical[-1]]
for year in extrapolation_years:
    extrapolated_it_services_jobs.append(extrapolated_it_services_jobs[-1] + it_services_annual_addition)

# Combine historical and extrapolated data
all_years = years_historical + list(extrapolation_years)
all_gcc_jobs = gcc_jobs_historical + extrapolated_gcc_jobs[1:] # Exclude first element of extrapolated
all_it_services_jobs = it_services_jobs_historical + extrapolated_it_services_jobs[1:]

plt.figure(figsize=(12, 7))

# Plot historical data
plt.plot(years_historical, gcc_jobs_historical, label='GCC Jobs (Historical)', marker='o', linestyle='-', color='blue')
plt.plot(years_historical, it_services_jobs_historical, label='IT Services Jobs (Historical)', marker='x', linestyle='-', color='green')

# Plot extrapolated data
plt.plot(extrapolation_years, extrapolated_gcc_jobs[1:], label='GCC Jobs (Extrapolated)', marker='o', linestyle='--', color='blue', alpha=0.7)
plt.plot(extrapolation_years, extrapolated_it_services_jobs[1:], label='IT Services Jobs (Extrapolated)', marker='x', linestyle='--', color='green', alpha=0.7)

# Label all data points (historical and extrapolated)
for i in range(len(all_years)):
    plt.text(all_years[i], all_gcc_jobs[i] + 0.1, f'{all_gcc_jobs[i]:.2f}', ha='center', va='bottom', fontsize=8, color='blue')
    plt.text(all_years[i], all_it_services_jobs[i] - 0.2, f'{all_it_services_jobs[i]:.2f}', ha='center', va='top', fontsize=8, color='green')

# Find and highlight crossover point (if any)
crossover_year = None
crossover_index = -1
for i in range(len(all_years) - 1):
    if (all_gcc_jobs[i] < all_it_services_jobs[i]) and (all_gcc_jobs[i+1] >= all_it_services_jobs[i+1]):
        crossover_year = all_years[i+1]
        crossover_index = i+1
        break

if crossover_year:
    plt.axvline(crossover_year, color='red', linestyle=':', label=f'Potential Crossover Point: Approx. {crossover_year}')
    print(f"GCC jobs are projected to potentially overtake IT services jobs around the year: {crossover_year}")
else:
    print("Based on these growth rates, a crossover point was not found within the projection period.")

plt.title('Trend of GCC and IT Services Jobs in India (Historical and Projected)')
plt.xlabel('Year')
plt.ylabel('Number of Jobs (in millions)')
plt.grid(True)
plt.legend()
plt.xticks(all_years)
plt.ylim(bottom=1, top=7) # Adjust y-axis limits for better visualization
plt.tight_layout()
plt.show()
