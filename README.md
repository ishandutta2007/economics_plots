# 📈 Economics & Geopolitical Data Visualizations

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](http://makeapullrequest.com)
[![Discord](https://img.shields.io/badge/Discord-Join%20Us-7289DA?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com/invite/jc4xtF58Ve)

Transforming complex global datasets into insightful, animated, and interactive visual stories. This repository contains a curated collection of Python scripts leveraging **Matplotlib**, **Pandas**, and **World Bank data** to explore macroeconomics, tech trends, and geopolitical shifts.

---

## 🌟 Core Capabilities

This repository provides a versatile toolkit for data storytellers and economists:

- **Static Plotting:** Generate high-resolution `.png` charts for reports and social media.
- **Dynamic Animations:** Create `.mp4` video animations that visualize economic trends over time (e.g., the closing GDP gap between major powers).
- **Live Data Fetching:** Many scripts integrate with the **World Bank API** to fetch the most recent global indicators automatically.
- **Interactive Visuals:** Some scripts include interactive features like hover tooltips and dynamic annotations using Matplotlib's event handling.

---

## 📊 Gallery

| China vs India: FDI vs GDP | Renewable Growth Comparison | SaaS vs World GDP |
|:---:|:---:|:---:|
| ![FDI vs GDP](assets/china_india_fdi_vs_gdp_hardcoded_plot.png) | ![Renewable Growth](assets/renewable_growth_comparison.png) | ![SaaS Growth](assets/saas_vs_world_gdp_projection.png) |

> *Note: More animations and plots are generated dynamically by running the scripts.*

---

## 📂 Project Structure

```text
economics_plots/
├── assets/                  # Gallery images and static plots
├── data/                    # Datasets (CSV files)
├── scripts/                 # Core visualization scripts
│   ├── macroeconomics/      # GDP, Trade, Energy, and Geopolitics
│   ├── technology/          # AI, Big Tech, and Industry trends
│   └── society/             # Population, Labor, and Environment
├── README.md
├── LICENSE
└── requirements.txt
```

---

## 📂 Topic Index

Explore the scripts based on your area of interest:

### 🌍 Macroeconomics & Geopolitics
| Topic | Scripts |
| :--- | :--- |
| **GDP & Convergence** | `scripts/macroeconomics/brics_vs_g7_gdp.py`, `scripts/macroeconomics/china_vs_usa_gdppc_ppp_animate.py`, `scripts/macroeconomics/EU_China_convergence.py`, `scripts/macroeconomics/india_vs_china_vs_usa_gdppc_animate.py`, `scripts/macroeconomics/southasiagdppc.py` |
| **Trade & FDI** | `scripts/macroeconomics/chinas_crude_imports.py`, `scripts/macroeconomics/fdi.py`, `scripts/macroeconomics/fdi_vs_immigrants.py`, `scripts/macroeconomics/india_crude_import.py` |
| **Energy & Resources** | `scripts/macroeconomics/china_vs_usa_energy_price.py`, `scripts/macroeconomics/cheapest_renewable_energy.py`, `scripts/macroeconomics/natural_resopurce_per_capita.py`, `scripts/macroeconomics/us_china_renewable.py`, `scripts/macroeconomics/rare_earth_metals_per_capita.py` |
| **Infrastructure** | `scripts/macroeconomics/China_high_speed_rail.py`, `scripts/macroeconomics/indian_highway_construction_rate.py` |

### 💻 Technology & Industry
| Topic | Scripts |
| :--- | :--- |
| **Artificial Intelligence** | `scripts/technology/ai_company_valuations.py`, `scripts/technology/ai_startups_revenue.py`, `scripts/technology/swe_vs_ai_jobs.py`, `scripts/technology/ai_energy_animate.py` |
| **Big Tech** | `scripts/technology/FAANG_headcount.py`, `scripts/technology/bigtech_employee_count_by_year.py`, `scripts/technology/bigsemiconductor_employee_count_by_year.py` |
| **Digital Platforms** | `scripts/technology/You_vs_Tik.py`, `scripts/technology/youtube_cpm.py` |
| **SaaS** | `scripts/technology/saas_vs_gdp.py` |

### 👥 Society & Environment
| Topic | Scripts |
| :--- | :--- |
| **Population** | `scripts/society/population_density.py`, `scripts/society/population_india_similar_sized.py`, `scripts/society/population_density_major_economies.py` |
| **Incomes & Labor** | `scripts/society/US_vs_India_median_wage.py`, `scripts/society/houshold_incomes_indians_vs_chinese.py`, `scripts/society/women_participation_workforce_gdp_per_capita_corelation.py` |
| **Environment** | `scripts/society/southasiaAQI.py`, `scripts/society/datacenter_power_share.py` |
| **Education** | `scripts/society/india_engg_vs_med_seats.py` |

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.7+**
- **FFmpeg (Optional but Recommended):** Required specifically for scripts ending in `_animate.py` to export animations as `.mp4` videos. If you only intend to generate static plots, this is not needed.
  - *Why FFmpeg?* It serves as the video encoding backend for `matplotlib.animation`.
  - *Windows:* `choco install ffmpeg` or download from [ffmpeg.org](https://ffmpeg.org/download.html).
  - *macOS:* `brew install ffmpeg`
  - *Linux:* `sudo apt install ffmpeg`

### Installation

1. **Clone the repo:**
   ```bash
   git clone https://github.com/Mr-Innovation/economics_plots.git
   cd economics_plots
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running a Visualization

Simply run any script to generate its corresponding plot or animation:

```bash
# Generate a static plot
python scripts/technology/ai_company_valuations.py

# Generate an animated MP4 (Requires FFmpeg)
python scripts/macroeconomics/china_vs_usa_gdppc_ppp_animate.py
```

---

## 📈 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=ishandutta2007/economics_plots&type=date&legend=top-left)](https://www.star-history.com/#ishandutta2007/economics_plots&type=date&legend=top-left)

---

## 🤝 Contributing

Contributions are welcome! Whether it's adding a new script, improving existing ones, or fixing a bug.

1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingVisualization`).
3. Commit your Changes (`git commit -m 'Add some AmazingVisualization'`).
4. Push to the Branch (`git push origin feature/AmazingVisualization`).
5. Open a Pull Request.

---

## 💬 Connect & Support

- **Discord:** [Join our community](https://discord.com/invite/jc4xtF58Ve)
- **Twitter:** [@ishandutta2007](https://twitter.com/ishandutta2007)
- **Sponsor:** [Support the development on GitHub](https://github.com/sponsors/ishandutta2007)

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
