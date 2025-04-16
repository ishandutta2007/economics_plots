import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# --- Load pre-downloaded data (replace with your actual file paths) ---
try:
    us_data_df = pd.read_csv('us_electricity_price.csv')
    if 'Commercial Price (cents/kWh)' in us_data_df.columns:
        us_data_df = us_data_df.rename(columns={'Commercial Price (cents/kWh)': 'USA Commercial Price (cents/kWh)'})
    elif 'value' in us_data_df.columns:
        us_data_df = us_data_df.rename(columns={'value': 'USA Commercial Price (cents/kWh)'})
    elif 'USA Commercial Price (cents/kWh)' not in us_data_df.columns:
        raise ValueError("Column 'USA Commercial Price (cents/kWh)' not found in us_electricity_price.csv")
except FileNotFoundError:
    print("Error: us_electricity_price.csv not found. Please download and save the US data.")
    us_data_df = None
except ValueError as e:
    print(f"Error loading US data: {e}")
    us_data_df = None

try:
    china_data_df = pd.read_csv('china_electricity_price.csv')
    if 'China Commercial Price (cents/kWh)' not in china_data_df.columns and 'value' in china_data_df.columns:
        china_data_df = china_data_df.rename(columns={'value': 'China Commercial Price (cents/kWh)'})
    elif 'China Commercial Price (cents/kWh)' not in china_data_df.columns:
        raise ValueError("Column 'China Commercial Price (cents/kWh)' not found in china_electricity_price.csv")
except FileNotFoundError:
    print("Error: china_electricity_price.csv not found. Please download and save the China data.")
    china_data_df = None
except ValueError as e:
    print(f"Error loading China data: {e}")
    china_data_df = None

# --- Merge the dataframes ---
if us_data_df is not None and china_data_df is not None:
    merged_df = pd.merge(us_data_df, china_data_df, on='Year', how='inner')
    merged_df = merged_df[(merged_df['Year'] >= 2014) & (merged_df['Year'] <= 2023)].sort_values(by='Year')

    # --- Plotting ---
    fig, ax = plt.subplots(figsize=(12, 7))

    line_china, = ax.plot(merged_df['Year'], merged_df['China Commercial Price (cents/kWh)'], marker='o', label='China')
    line_usa, = ax.plot(merged_df['Year'], merged_df['USA Commercial Price (cents/kWh)'], marker='s', label='USA')

    ax.set_title('Average Commercial Electricity Prices (2014-2023)')
    ax.set_xlabel('Year')
    ax.set_ylabel('Average Price (cents/kWh)')
    ax.set_xticks(merged_df['Year'])
    ax.legend()
    ax.grid(True)

    # --- Add latest value annotations ---
    last_china_year = merged_df['Year'].iloc[-1]
    last_china_price = merged_df['China Commercial Price (cents/kWh)'].iloc[-1]
    ax.annotate(f'{last_china_price:.2f}',
                xy=(last_china_year, last_china_price),
                xytext=(5, 5),  # Offset from the data point
                textcoords='offset points',
                fontsize=9,
                color=line_china.get_color())

    last_usa_year = merged_df['Year'].iloc[-1]
    last_usa_price = merged_df['USA Commercial Price (cents/kWh)'].iloc[-1]
    ax.annotate(f'{last_usa_price:.2f}',
                xy=(last_usa_year, last_usa_price),
                xytext=(5, 5),  # Offset from the data point
                textcoords='offset points',
                fontsize=9,
                color=line_usa.get_color())

    # --- Tooltip functionality ---
    annot = ax.annotate("", xy=(0, 0), xytext=(20, 20), textcoords="offset points",
                        bbox=dict(boxstyle="round,pad=0.3", fc="yellow", alpha=0.5),
                        arrowprops=dict(arrowstyle="->"))
    annot.set_visible(False)

    def update_annot(event):
        vis = annot.get_visible()
        if event.inaxes == ax:
            for line, label_col in zip([line_china, line_usa], ['China Commercial Price (cents/kWh)', 'USA Commercial Price (cents/kWh)']):
                cont, ind = line.contains(event)
                if cont:
                    x, y = line.get_data()
                    snap_idx = ind['ind'][0]
                    annot.xy = (x[snap_idx], y[snap_idx])
                    text = f"{int(x[snap_idx])}, {merged_df[label_col].iloc[snap_idx]:.2f} cents/kWh ({line.get_label()})"
                    annot.set_text(text)
                    annot.get_bbox_patch().set_alpha(0.4)
                    annot.set_visible(True)
                    fig.canvas.draw_idle()
                    return
        if vis:
            annot.set_visible(False)
            fig.canvas.draw_idle()

    fig.canvas.mpl_connect("motion_notify_event", update_annot)
    plt.tight_layout()
    plt.show()

else:
    print("Could not load data for one or both countries. Please ensure the CSV files are correctly formatted and in the same directory.")