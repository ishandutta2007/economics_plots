import matplotlib.pyplot as plt

# Define the data points for the two job roles.
# The numbers are in thousands for better readability on the plot.
years = [2023, 2035]

# Data for Software Engineers
se_jobs_2023 = 760_000
se_jobs_2035 = 1_500_000
software_engineer_jobs = [se_jobs_2023, se_jobs_2035]

# Data for ML Engineers
ml_jobs_2023 = 40_000
ml_jobs_2035 = 1_500_000
ml_engineer_jobs = [ml_jobs_2023, ml_jobs_2035]

# Calculate the growth factors
se_growth_factor = se_jobs_2035 / se_jobs_2023
ml_growth_factor = ml_jobs_2035 / ml_jobs_2023

# Create the plot
plt.style.use('seaborn-v0_8-whitegrid') # A clean style with a grid
plt.figure(figsize=(10, 6)) # Set the figure size for better viewing

# Plot the Software Engineer job growth line
plt.plot(years, software_engineer_jobs, marker='o', linestyle='-', color='b', label='Traditional Software Engineers at FAANG')

# Plot the ML Engineer job growth line
plt.plot(years, ml_engineer_jobs, marker='o', linestyle='-', color='r', label='ML/AI Engineers/Scientists/Researchers at FAANG')

# Add labels and a title to the plot
plt.title('Projected Job Growth: 2023 to 2035', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Jobs', fontsize=12)

# Customize the y-axis to be in millions
# This makes the large numbers easier to read
# We'll also set a consistent limit for better comparison
plt.ticklabel_format(style='plain')
plt.yticks(
    [0, 500_000, 1_000_000, 1_500_000],
    ['0', '0.5M', '1.0M', '1.5M']
)
# plt.xlim(0, 2040)
plt.ylim(0, 1_600_000)

# Add vertical arrows and text annotations for Software Engineers
plt.annotate(
    f'{se_growth_factor:.0f}x',
    xy=(years[1]-0.5, se_jobs_2023),
    xytext=(years[1]-0.5, se_jobs_2035),
    arrowprops=dict(arrowstyle="<|-", color='blue', lw=2, mutation_scale=20),
    fontsize=10,
    ha='center'
)

# Add vertical arrows and text annotations for ML Engineers
plt.annotate(
    f'{ml_growth_factor:.0f}x',
    xy=(years[1]+0.5, ml_jobs_2023),
    xytext=(years[1]+0.5, ml_jobs_2035),
    arrowprops=dict(arrowstyle="<|-", color='red', lw=2, mutation_scale=20),
    fontsize=10,
    ha='center'
)


# Add a legend to differentiate the lines
plt.legend(fontsize=10)

# Ensure the x-axis ticks are only at the data points
plt.xticks(years)

# Display the plot
plt.show()

