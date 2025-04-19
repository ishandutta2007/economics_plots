# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# # Generate synthetic software engineer data (2003-2022)
# years = list(range(2003, 2023))
# n_years = len(years)

# # Engineering workforce assumptions (synthetic)
# software_engineer_data = {
#     # Google: High growth in early years, stabilizing
#     'Google': np.round(np.exp(np.linspace(np.log(200), np.log(45000), n_years))).astype(int),
    
#     # Meta: Later start with rapid engineering hiring
#     'Meta': np.concatenate([
#         np.zeros(7),  # 2003-2009 (pre-Facebook growth)
#         np.round(np.exp(np.linspace(np.log(100), np.log(25000), n_years-7)))
#     ]).astype(int),
    
#     # Microsoft: Steady growth with enterprise focus
#     'Microsoft': np.linspace(15000, 55000, n_years).astype(int) * np.random.normal(1, 0.05, n_years),
    
#     # Apple: Hardware-focused with growing services engineering
#     'Apple': np.round(np.linspace(2500, 35000, n_years)**1.15).astype(int),
    
#     # Amazon: Two-phase growth (e-commerce then AWS)
#     'Amazon': np.concatenate([
#         np.round(np.exp(np.linspace(np.log(500), np.log(8000), 12))),  # 2003-2014
#         np.round(np.exp(np.linspace(np.log(8000), np.log(45000), n_years-12)))  # 2015-2022
#     ]).astype(int)
# }

# # Create DataFrame
# df = pd.DataFrame(software_engineer_data, index=years)
# df.index.name = 'Year'

# # Plot configuration
# plt.figure(figsize=(14, 8))
# colors = ['#4285F4', '#4267B2', '#F65314', '#A3AAAE', '#FF9900']

# for i, (company, color) in enumerate(zip(df.columns, colors)):
#     plt.plot(df.index, df[company], 
#              marker='o', 
#              linestyle='-', 
#              linewidth=2.5,
#              markersize=8,
#              color=color,
#              label=company)

# plt.title('Software Engineering Workforce Growth (2003-2022)', fontsize=16, pad=20)
# plt.xlabel('Year', fontsize=12)
# plt.ylabel('Number of Software Engineers', fontsize=12)
# plt.legend(title='Companies', title_fontsize='13', fontsize=11)
# plt.grid(True, linestyle='--', alpha=0.7)

# # Formatting axes
# plt.xticks(df.index[::2], rotation=45, ha='right')
# plt.yscale('log')
# plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x):,}'))

# plt.tight_layout()
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Data synthesis (2015-2024) with real Meta data and assumptions for others
years = list(range(2015, 2025))
companies = ['Google', 'Meta', 'Microsoft', 'Apple', 'Amazon']

# Meta's actual employee data (2015-2024) :cite[5]:cite[7]:cite[9]
meta_employees = [12691, 17048, 25105, 35587, 44942, 58604, 71970, 86482, 67317, 74067]
software_engineer_ratio = 0.55  # Assuming 55% are software engineers

data = {
    'Google': np.round(np.linspace(20000, 85000, 10) * np.random.normal(1, 0.05, 10)),
    'Meta': np.array(meta_employees) * software_engineer_ratio,
    'Microsoft': np.round(np.linspace(35000, 110000, 10) * 0.6),
    'Apple': np.round(np.linspace(15000, 65000, 10)**1.1),
    'Amazon': np.round(15000 * (1.4 ** np.arange(10)))
}

# Calculate 10-year growth factors
growth_factors = {}
for company in companies:
    start = data[company][0]
    end = data[company][-1]
    growth_factors[company] = f"{end/start:.1f}x"

# Create DataFrame
df = pd.DataFrame(data, index=years)
df.index.name = 'Year'

# Plot configuration
plt.figure(figsize=(16, 8))
colors = ['#4285F4', '#4267B2', '#F65314', '#A3AAAE', '#FF9900']

for i, (company, color) in enumerate(zip(df.columns, colors)):
    plt.plot(df.index, df[company], 
             marker='o', 
             linestyle='-', 
             linewidth=2.5,
             markersize=8,
             color=color,
             label=f'{company} ({growth_factors[company]})')

# Add growth factor annotations
annotation_text = "\n".join([f"{company}: {growth_factors[company]}" for company in companies])
plt.text(0.95, 0.15, annotation_text,
         transform=plt.gca().transAxes,
         verticalalignment='top',
         horizontalalignment='right',
         bbox=dict(facecolor='white', alpha=0.8))

plt.title('Software Engineer Growth (2015-2024) with 10-Year Growth Factors', fontsize=16, pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Estimated Software Engineers', fontsize=12)
plt.legend(title='Companies', title_fontsize='13', fontsize=11)
plt.grid(True, linestyle='--', alpha=0.7)

# Formatting axes
plt.xticks(df.index, rotation=45)
plt.yscale('log')
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x):,}'))

plt.tight_layout()
plt.show()