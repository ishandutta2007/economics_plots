import matplotlib.pyplot as plt
import pandas as pd
import io

# Data from the image
data = """Country,Tonnes per million people
Greenland,26422406.20
Vietnam,224103.72
Australia,219230.77
Brazil,96774.19
Russia,68493.15
China,31148.24
Canada,21282.05
Tanzania,14062.03
South Africa,13166.67
United States,5389.22
India,4859.15
Thailand,64.29
"""

# Read the data into a pandas DataFrame
df = pd.read_csv(io.StringIO(data))

# Sort the data to have the largest value on top
df = df.sort_values(by='Tonnes per million people', ascending=True)

# Create the plot
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(12, 8))

# Create horizontal bars
bars = ax.barh(df['Country'], df['Tonnes per million people'], color='skyblue')

# Add labels and title
ax.set_xlabel('Tonnes per Million People (Logarithmic Scale)', fontsize=12)
ax.set_ylabel('Country', fontsize=12)
ax.set_title('Rare Earth Metal Oxides per Capita', fontsize=16, fontweight='bold')

# Use a logarithmic scale due to the outlier (Greenland)
ax.set_xscale('log')

# Add data labels to the bars
for bar in bars:
    width = bar.get_width()
    label_x_pos = width * 1.1
    ax.text(label_x_pos, bar.get_y() + bar.get_height()/2, f'{width:,.2f}',
            va='center', ha='left', fontsize=10)

# Adjust layout and display the plot
plt.tight_layout()
plt.show()
