import pandas as pd
import matplotlib.pyplot as plt
import os

# Define the paths
script_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(os.path.dirname(__file__), "..", "..", "assets")
# Navigate up to the project root and into the data directory
source = "Thapar"
data_path = os.path.join(script_dir, '..', '..', 'data', source+'_Europe_India_China_PPP.csv')

# Output plot path
output_path = os.path.join(assets_dir, 'gdp_curve.png')

def plot_gdp():
    print(f"Reading data from: {data_path}")
    
    # Load the CSV data
    df = pd.read_csv(data_path)
    
    # Convert 'Year' column from string (e.g., '1 AD') to integer
    df['Year'] = df['Year'].str.replace(' AD', '').astype(int)
    
    # Plotting
    plt.figure(figsize=(12, 7))
    
    plt.plot(df['Year'], df['Europe GDP ($B)'], label='Europe GDP ($B)', marker='o', linewidth=2)
    plt.plot(df['Year'], df['India GDP ($B)'], label='India GDP ($B)', marker='s', linewidth=2)
    plt.plot(df['Year'], df['China GDP ($B)'], label='China GDP ($B)', marker='^', linewidth=2)
    
    # Annotate points
    for i in range(len(df)):
        plt.annotate(str(df['Europe GDP ($B)'].iloc[i]), (df['Year'].iloc[i], df['Europe GDP ($B)'].iloc[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8, alpha=0.8)
        plt.annotate(str(df['India GDP ($B)'].iloc[i]), (df['Year'].iloc[i], df['India GDP ($B)'].iloc[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8, alpha=0.8)
        plt.annotate(str(df['China GDP ($B)'].iloc[i]), (df['Year'].iloc[i], df['China GDP ($B)'].iloc[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8, alpha=0.8)
    
    # Adding titles and labels
    plt.title(f'Historical GDP: Europe vs India vs China (source:{source})', fontsize=16)
    plt.xlabel('Year (AD)', fontsize=12)
    plt.ylabel('GDP in Billions ($)', fontsize=12)
    
    # Grid and Legend
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(fontsize=12)
    
    # Use logarithmic scale if the exponential growth at the end makes earlier data hard to see
    plt.yscale('log') 
    
    # Save the plot
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    print(f"Plot saved successfully to: {output_path}")
    
    # Uncomment to show the plot if running interactively
    plt.show()

if __name__ == '__main__':
    plot_gdp()
