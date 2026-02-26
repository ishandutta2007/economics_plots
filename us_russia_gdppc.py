import pandas as pd
import matplotlib.pyplot as plt

# ---- Load Data ----
df = pd.read_csv("us_russia_gdppc.csv")

# Convert to numeric (empty cells -> NaN)
df["Russia"] = pd.to_numeric(df["Russia"], errors="coerce")
df["United States"] = pd.to_numeric(df["United States"], errors="coerce")

# ---- Drop rows where Russia data is missing (before 1992) ----
df_clean = df.dropna(subset=["Russia"]).copy()

# ---- Calculate USA : Russia Ratio ----
df_clean["USA_Russia_Ratio"] = (
    df_clean["United States"] / df_clean["Russia"]
)

# # ==========================
# # Plot GDP per Capita
# # ==========================
# plt.figure()

# plt.plot(df_clean["Year"], df_clean["United States"],
#          label="USA GDP per capita")

# plt.plot(df_clean["Year"], df_clean["Russia"],
#          label="Russia GDP per capita")

# plt.xlabel("Year")
# plt.ylabel("GDP per Capita (Current US$)")
# plt.title("GDP per Capita Comparison")

# plt.legend()
# plt.grid(True)

# plt.show()


# ==========================
# Plot Ratio Curve
# ==========================
plt.figure()

plt.plot(df_clean["Year"],
         df_clean["USA_Russia_Ratio"],
         label="USA : Russia Ratio")

plt.xlabel("Year")
plt.ylabel("Ratio")
plt.title("USA to Russia GDP per Capita Ratio")

plt.legend()
plt.grid(True)

plt.show()