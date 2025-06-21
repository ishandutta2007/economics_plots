import requests
import pandas as pd
import matplotlib.pyplot as plt

# Country ISO codes and labels
countries = {
    "IN": "India",
    "PK": "Pakistan",
    "BD": "Bangladesh",
    "LK": "Sri Lanka",
    "BT": "Bhutan",
}

indicator = "NY.GDP.PCAP.CD"  # GDP per capita (current US$)
end_year = 2023
start_year = end_year - 9


def fetch_gdp_per_capita(country_code):
    url = f"https://api.worldbank.org/v2/country/{country_code}/indicator/{indicator}?format=json&date={start_year}:{end_year}&per_page=100"
    response = requests.get(url)
    data = response.json()[1]
    return {
        int(item["date"]): item["value"] for item in data if item["value"] is not None
    }


# Create DataFrame with GDP per capita data
gdp_data = {}

for code, name in countries.items():
    gdp_per_year = fetch_gdp_per_capita(code)
    gdp_data[name] = gdp_per_year

df = pd.DataFrame(gdp_data)
df = df.sort_index()

# Plotting
plt.figure(figsize=(12, 6))
for country in df.columns:
    plt.plot(df.index, df[country], marker="o", label=country)

    # Add label near the last point
    latest_year = df[country].last_valid_index()
    latest_value = df[country].loc[latest_year]
    if pd.notnull(latest_value):
        label = f"{country} ({latest_value:,.0f})"
        plt.text(latest_year + 0.1, latest_value, label, fontsize=9, va="center")

plt.title("GDP per Capita (USD) - Last 10 Years")
plt.xlabel("Year")
plt.ylabel("GDP per Capita (USD)")
plt.grid(True)
plt.tight_layout()
plt.show()
