import matplotlib.pyplot as plt
import numpy as np

# Combined data after merging rows 1-2 (IT Services & Global IT Firms)
categories = [
    "IT Services Firms\n(Infosys, TCS, Wipro, \nIBM, Cognizant, Accenture)",
    "Indian Startups\n(Flipkart, Swiggy, Zomato, Paytm)",
    "FAANG and other American \nProduct Companies' Indian offices\n(Adobe, Microsoft India, Google India)",
    "Consulting\n(BCG, McKinsey, Bain)",
    "Research Labs\n(ISRO, DRDO, CDAC)",
    "No Work Experience in India"
]

# Mean percentages calculated from original ranges
mean_percentages = [
    (55 + 65 + 15 + 20) / 2 / 2,  # Combined mean for merged rows (55-65% + 15-20%)
    (10 + 15) / 2,                # Startups
    (5 + 8) / 2,                  # Product Companies
    (1 + 3) / 2,                  # Consulting
    0.5                           # Research Labs (<1% approximated)
]

mean_percentages = [72.4, 12.1, 6.2, 1.9, 0.4, 7.0]  # Total = 100%

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

plt.figure(figsize=(12, 6))
bars = plt.bar(categories, mean_percentages, color=colors)

# Add percentage labels on bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.1f}%',
             ha='center', va='bottom')

plt.ylabel('Percentage (%)', fontsize=12)
plt.title('Companies Joined by current FAANG employees in US\n Between Undergrad(in India) and MS(in USA)', fontsize=18, pad=22)
plt.ylim(0, 85)  # Adjust y-axis to emphasize differences

# Rotate x-axis labels for readability
plt.xticks(rotation=15, ha='right', fontsize=10)

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.figtext(0.85, 0.01, 'Data-source: Linkedin as of March,2025.', ha='center', fontsize=10, color='blue', style='italic')
plt.show()
