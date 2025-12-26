import matplotlib.pyplot as plt

# Data for Engineering (Seats in Lakhs)
years_eng = [
    '2014-15', '2015-16', '2016-17', '2017-18', '2018-19', 
    '2019-20', '2020-21', '2021-22', '2022-23', '2023-24', '2024-25'
]
seats_eng = [
    17.05, 16.30, 15.56, 14.75, 14.04, 
    13.28, 12.86, 12.54, 12.74, 13.50, 14.90
]

# Medical data (MBBS + BDS converted to Lakhs) 
medical_years = ['2014-15', '2017-18', '2021-22', '2022-23', '2023-24', '2024-25']
seats_med = [0.765, 0.940, 1.102, 1.194, 1.368, 1.461]

plt.figure(figsize=(12, 7))

# Plotting Engineering
plt.plot(years_eng, seats_eng, marker='o', label='Engineering Intake (Lakhs)', color='#4cabb1', linewidth=2.5)

# Plotting Medical
plt.plot(medical_years, seats_med, marker='s', label='Medical Intake (MBBS+BDS, Lakhs)', color='#d62728', linestyle='--', linewidth=2.5)

# Annotating Engineering points
for i, txt in enumerate(seats_eng):
    plt.annotate(f'{txt}', (years_eng[i], seats_eng[i]), textcoords="offset points", 
                 xytext=(0,10), ha='center', fontsize=9, fontweight='bold', color='#2a5e61')

# Annotating Medical points
for i, txt in enumerate(seats_med):
    plt.annotate(f'{txt}', (medical_years[i], seats_med[i]), textcoords="offset points", 
                 xytext=(0,10), ha='center', fontsize=9, fontweight='bold', color='#b22222')

# Styling the graph
plt.title('Annotated Comparison: Engineering vs Medical Intake (India)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Academic Year', fontsize=12)
plt.ylabel('Seats (in Lakhs)', fontsize=12)
plt.yscale('log')
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.4)
plt.legend(loc='center right')
plt.ylim(0, 19)  # Starting from 0 to highlight the massive gap

plt.tight_layout()
# plt.savefig('annotated_eng_vs_med.png')
plt.show()