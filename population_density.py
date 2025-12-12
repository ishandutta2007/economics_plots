def calculate_density(population, area_sq_km):
    """
    Calculates population density (people per sq km) given population and area.
    """
    if area_sq_km == 0:
        return 0
    return population / area_sq_km

# Data for selected countries (Population and Area in sq km) for 2025
# Sources:

sparsest_countries = {
    "Greenland": {"population": 56600, "area": 2166086}, # Area is mostly ice sheet
    "Mongolia": {"population": 3500000, "area": 1564116},
    "Namibia": {"population": 2600000, "area": 824269},
    "Australia": {"population": 27000000, "area": 7692024}
}

dense_countries = {
    "Monaco": {"population": 39684, "area": 2.02}, # Data from 2022/2025 sources
    "Singapore": {"population": 6000000, "area": 728.6},
    "Bangladesh": {"population": 174000000, "area": 147570}, # Most dense large country
    "India": {"population": 1438000000, "area": 3287263}
}

print("--- Population Densities (People per sq km) ---")

print("\n*Sparsest Countries:")
for country, data in sparsest_countries.items():
    density = calculate_density(data["population"], data["area"])
    print(f"- {country}: {density:.2f}")

print("\n*Dense Countries:")
for country, data in dense_countries.items():
    density = calculate_density(data["population"], data["area"])
    print(f"- {country}: {density:.2f}")
