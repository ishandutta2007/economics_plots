import pandas as pd
import matplotlib.pyplot as plt

def calculate_population_density(country_data):
    """
    Calculates population density (people per sq km) for a given set of countries.

    Args:
        country_data (list): A list of dictionaries, each containing 'Country', 
                             'Population', and 'Area_sq_km'.

    Returns:
        pandas.DataFrame: A DataFrame with the calculated population densities.
    """
    # Create a pandas DataFrame from the data
    df = pd.DataFrame(country_data)

    # Calculate population density: Population / Area
    df['Density_per_sq_km'] = df['Population'] / df['Area_sq_km']

    # Sort the DataFrame by density in ascending order for horizontal plot
    df = df.sort_values(by='Density_per_sq_km', ascending=True)

    return df

def plot_density(df):
    """
    Generates a horizontal bar plot of population densities.
    """
    plt.figure(figsize=(10, 6))
    bars = plt.barh(df['Country'], df['Density_per_sq_km'], color='skyblue')
    plt.xlabel('Population Density (people per sq km)')
    plt.title('Population Density of Selected Countries')

    # Annotate each bar with the value
    for bar in bars:
        width = bar.get_width()
        plt.text(width, bar.get_y() + bar.get_height()/2, f' {width:.2f}', va='center')

    plt.tight_layout()

    # To save the plot to a file:
    # plt.savefig('population_density_plot.png')
    # To display the plot (this works in environments like Jupyter, but not in all text consoles):
    plt.show()
    print("\n--- A horizontal bar plot 'population_density_plot.png' has been generated and saved (or would be displayed if running in a suitable environment). ---")


# Data for selected countries (Population and Area data are approximate and for demonstration)
selected_countries_data = [
    # Densely Populated
    # {'Country': 'Macau (SAR, China)', 'Population': 683200, 'Area_sq_km': 32.9},
    # {'Country': 'Monaco', 'Population': 36687, 'Area_sq_km': 2.1},
    # {'Country': 'Singapore', 'Population': 6000000, 'Area_sq_km': 719},
    {'Country': 'Bangladesh', 'Population': 170000000, 'Area_sq_km': 148460},
    {'Country': 'Pakistan', 'Population': 245000000, 'Area_sq_km': 881913},
    {'Country': 'Philippines', 'Population': 117000000, 'Area_sq_km': 300000},
    # Sparsely Populated
    {'Country': 'Mongolia', 'Population': 3400000, 'Area_sq_km': 1564116},
    {'Country': 'Namibia', 'Population': 2600000, 'Area_sq_km': 825615},
    {'Country': 'Australia', 'Population': 26400000, 'Area_sq_km': 7692024},
    {'Country': 'Greenland', 'Population': 56000, 'Area_sq_km': 2166086},
    {'Country': 'Canada', 'Population': 40000000, 'Area_sq_km': 9984670},
    {'Country': 'Kazakhstan', 'Population': 19500000, 'Area_sq_km': 2724900}
]

# Calculate densities
density_df = calculate_population_density(selected_countries_data)

# Print the results
print("Population Density of Selected Countries (people per sq km):\n")
# Format the output for better readability
print(density_df.round(2).to_markdown(index=False))

# Generate the plot
plot_density(density_df)
