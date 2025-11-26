import matplotlib.pyplot as plt

# Data for years and HSR length in kilometers
years = [
    2008,
    2009,
    2010,
    2011,
    2012,
    2013,
    2014,
    2015,
    2016,
    2017,
    2018,
    2019,
    2020,
    2021,
    2022,
    2023,
    2024,
]
hsr_length = [
    2740,
    3676,
    5149,
    8358,
    9356,
    11028,
    16726,
    19210,
    22000,
    25000,
    29000,
    35000,
    37900,
    40000,
    42000,
    45000,
    48000,
]

# Create the plot
plt.figure(figsize=(10, 6))  # Set the figure size for better readability
plt.plot(
    years, hsr_length, marker="o", linestyle="-", color="blue"
)  # Plot the data with markers and a line

# Add labels and title
plt.xlabel("Year")  # Label for the x-axis
plt.ylabel("HSR Length (km)")  # Label for the y-axis
plt.title("Growth of China's High-Speed Rail Network")  # Title of the plot

# Add grid for better readability
plt.grid(True)

# Customize x-axis ticks to show all years
plt.xticks(years, rotation=45)  # Rotate x-axis labels for better display

# Display the plot
plt.tight_layout()  # Adjust layout to prevent labels from overlapping
plt.show()
