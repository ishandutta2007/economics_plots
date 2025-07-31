import matplotlib.pyplot as plt

# Replace with your actual data
years = [2018, 2019, 2020, 2021, 2022, 2023]
gcc_jobs = [1.2, 1.4, 1.5, 1.7, 1.9, 1.975]  # Hypothetical GCC job numbers in millions
it_services_jobs = [4.2, 4.5, 4.8, 5.0, 5.2, 5.4]  # Hypothetical IT Services job numbers in millions

plt.figure(figsize=(10, 6))

plt.plot(years, gcc_jobs, label='GCC Jobs', marker='o', linestyle='-', color='blue')
plt.plot(years, it_services_jobs, label='IT Services Jobs', marker='x', linestyle='--', color='green')

# Label GCC data points
for year, job_count in zip(years, gcc_jobs):
    plt.text(year, job_count + 0.05, f'{job_count:.2f}', ha='center', va='bottom', fontsize=8, color='blue') # .2f for 2 decimal places

# Label IT Services data points
for year, job_count in zip(years, it_services_jobs):
    plt.text(year, job_count + 0.05, f'{job_count:.2f}', ha='center', va='bottom', fontsize=8, color='green') # Adjust vertical alignment to avoid overlap

plt.title('Trend of GCC and IT Services Jobs in India (by Year)')
plt.xlabel('Year')
plt.ylabel('Number of Jobs (in millions)')
plt.grid(True)
plt.legend()

plt.xticks(years)
plt.tight_layout()
plt.show()
