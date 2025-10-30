import traceback
import pandas as pd
import matplotlib.pyplot as plt
import re
import requests  # <-- Import requests library

# List of major economies by nominal GDP (2025 estimate)
major_economies = [
    "Argentina",
    "Australia",
    "Brazil",
    "Canada",
    "China",
    "France",
    "Germany",
    "India",
    "Indonesia",
    "Italy",
    "Japan",
    "Mexico",
    "Russia",
    "Saudi Arabia",
    "South Africa",
    "South Korea",
    "Turkey",
    "United Kingdom",
    "United States",
]

tax_heaven_economies = [
    "Netherlands",
    "Ireland",
    "Switzerland",
    "Luxembourg",
    "Liechtenstein",
    "Monaco",
    "Singapore",
    "Hong Kong",
    "Macao",
    "UAE",
]

print("Major Economies:", major_economies)

# --- Helper Functions (unchanged) ---


def clean_country_name(name):
    """Cleans country names for merging."""
    name = str(name).strip()
    name = re.sub(r"\[.*?\]", "", name)
    name = name.split("[")[0]
    if name == "United States":
        name = "United States"
    if name == "Russian Federation":
        name = "Russia"
    if name in ["Curaçao", "Curaçao[b]"]:
        name = "Curaçao"
    return name


def clean_numeric_col(series):
    """Cleans a string column to be numeric, handling '−' and other chars."""
    return pd.to_numeric(
        series.astype(str)
        .str.replace("−", "-", regex=False)
        .str.replace("[^0-9.-]", "", regex=True),
        errors="coerce",
    )


def find_fdi_table(tables_list):
    """Finds the correct FDI table by checking for characteristic columns."""
    for table in tables_list:
        cols = table.columns
        if isinstance(cols, pd.MultiIndex):
            if ("Country/Territory", "Country/Territory") in cols and (
                "% of GDP",
                "2023",
            ) in cols:
                print("Found FDI table.")
                df_fdi = table.copy()
                df_fdi.columns = [
                    "_".join(col).strip() for col in df_fdi.columns.values
                ]
                df_fdi = df_fdi[
                    ["Country/Territory_Country/Territory", "% of GDP_2023"]
                ]
                df_fdi.columns = ["Country", "FDI_pct_GDP"]
                df_fdi["Country"] = df_fdi["Country"].apply(clean_country_name)
                df_fdi["FDI_pct_GDP"] = clean_numeric_col(df_fdi["FDI_pct_GDP"])
                return df_fdi
    return None


def find_immigrant_table(tables_list):
    """Finds the immigrant table. It has a simple header."""
    for table in tables_list:
        cols = table.columns
        if (
            not isinstance(cols, pd.MultiIndex)
            and "Name" in cols
            and "% of population" in cols
        ):
            if "immigrant" in str(table.iloc[0, 0]).lower():
                continue

            print("Found Immigrant table.")
            df_imm = table.copy()
            df_imm = df_imm[["Name", "% of population"]]
            df_imm.columns = ["Country", "Immigrant_pct_Pop"]
            df_imm["Country"] = df_imm["Country"].apply(clean_country_name)
            df_imm["Immigrant_pct_Pop"] = clean_numeric_col(df_imm["Immigrant_pct_Pop"])
            return df_imm
    return None


def find_emigrant_table(tables_list):
    """Finds the emigrant table. It has a MultiIndex header."""
    for table in tables_list:
        cols = table.columns
        if isinstance(cols, pd.MultiIndex):
            if ("Name", "Name") in cols and ("Emigrants", "% of population") in cols:
                print("Found Emigrant table.")
                df_em = table.copy()
                df_em.columns = ["_".join(col).strip() for col in df_em.columns.values]
                df_em = df_em[["Name_Name", "Emigrants_% of population"]]
                df_em.columns = ["Country", "Emigrant_pct_Pop"]
                df_em["Country"] = df_em["Country"].apply(clean_country_name)
                df_em["Emigrant_pct_Pop"] = clean_numeric_col(df_em["Emigrant_pct_Pop"])
                return df_em
    return None


# --- Main script ---
try:
    # 1. Define URLs and Headers
    url_fdi = "https://en.wikipedia.org/wiki/List_of_countries_by_foreign_direct_investment_inflows"
    url_pop = "https://en.wikipedia.org/wiki/List_of_sovereign_states_by_immigrant_and_emigrant_population"

    # This header makes us look like a browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    # 2. Load Data using 'requests'
    print("Fetching FDI data...")
    html_fdi = requests.get(url_fdi, headers=headers).text
    all_tables_fdi = pd.read_html(html_fdi)
    print(f"Loaded {len(all_tables_fdi)} tables from FDI URL.")

    print("Fetching Population data...")
    html_pop = requests.get(url_pop, headers=headers).text
    all_tables_pop = pd.read_html(html_pop)
    print(f"Loaded {len(all_tables_pop)} tables from Population URL.")

    # 3. Find and Process Each Table
    df_fdi = all_tables_fdi[0]  # find_fdi_table([all_tables_fdi[0]])
    df_imm = all_tables_pop[1]  # find_immigrant_table(all_tables_pop)
    # df_em = find_emigrant_table(all_tables_pop)

    if df_fdi is None:
        raise ValueError("Could not find the required FDI table.")
    if df_imm is None:
        raise ValueError("Could not find the required Immigrant table.")
    # if df_em is None:
    #     raise ValueError("Could not find the required Emigrant table.")

    # 4. --- Plot 1: FDI vs. Immigrant Population ---

    df_imm.columns = [
        "Country",
        "Immigrants",
        "Immigrant_pct_Pop",
        "Female_Immigrant_pct_Pop",
    ]
    df_fdi.columns = [
        "Country",
        "FDI_mil",
        "FDI_yr",
        "FDI_pct_GDP",
        "FDI_pct_GDP_yr",
        "Inward_FDI_mil",
        "Inward_FDI_yr",
    ]
    merged_imm = pd.merge(df_fdi, df_imm, on="Country", how="inner")
    merged_imm.dropna(subset=["FDI_pct_GDP", "Immigrant_pct_Pop"], inplace=True)

    print(f"\nMerged {len(merged_imm)} countries for Immigrant plot.")

    merged_imm = merged_imm[merged_imm["Country"].isin(major_economies + tax_heaven_economies)]
    print("Immigrant Data Head:\n", merged_imm.head(30))

    if not merged_imm.empty:
        plt.figure(figsize=(10, 6))
        plt.scatter(
            merged_imm["Immigrant_pct_Pop"], merged_imm["FDI_pct_GDP"], alpha=0.7
        )
        # Annotate each point with its country name
        for i, row in merged_imm.iterrows():
            plt.annotate(
                row["Country"],
                (row["Immigrant_pct_Pop"], row["FDI_pct_GDP"]),
                fontsize=8,
                xytext=(3, 3),
                textcoords="offset points",
            )
        plt.xlabel("Immigrant % of Population")
        plt.ylabel("FDI % of GDP (2023)")
        plt.xscale("log")
        plt.title("FDI (% of GDP) vs. Immigrant Population (%) by Country")
        plt.grid(True)
        plt.tight_layout()
        plt.show()
        plt.savefig("fdi_vs_immigrant_plot.png")
        print("Plot saved as 'fdi_vs_immigrant_plot.png'")
    else:
        print("No data to plot for Immigrants.")

    # 5. --- Plot 2: FDI vs. Emigrant Population ---

    # merged_em = pd.merge(df_fdi, df_em, on='Country', how='inner')
    # merged_em.dropna(subset=['FDI_pct_GDP', 'Emigrant_pct_Pop'], inplace=True)

    # print(f"\nMerged {len(merged_em)} countries for Emigrant plot.")
    # print("Emigrant Data Head:\n", merged_em.head())

    # if not merged_em.empty:
    #     plt.figure(figsize=(10, 6))
    #     plt.scatter(merged_em['Emigrant_pct_Pop'], merged_em['FDI_pct_GDP'], alpha=0.7, color='green')
    #     plt.xlabel('Emigrant % of Population')
    #     plt.ylabel('FDI % of GDP (2023)')
    #     plt.title('FDI (% of GDP) vs. Emigrant Population (%) by Country')
    #     plt.grid(True)
    #     plt.tight_layout()
    #     plt.savefig('fdi_vs_emigrant_plot.png')
    #     print("Plot saved as 'fdi_vs_emigrant_plot.png'")
    # else:
    #     print("No data to plot for Emigrants.")

except Exception as e:
    print(f"An error occurred: {e}")
    print(
        "Failed to generate plots. Check URLs and page structures, which may have changed."
    )
    traceback.print_exc()
