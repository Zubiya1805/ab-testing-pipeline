A/B Testing Pipeline: New Checkout Button Analysis

📌 Project Overview
An end-to-end A/B testing pipeline that analyzes whether a new checkout 
button design increases conversion rate on an e-commerce platform.
This project mirrors real-world experimentation workflows used at 
companies like Google, Amazon, and Deloitte.

Business Problem
The product team designed a new checkout button and needed statistical 
proof before rolling it out to millions of users. As the data analyst, 
I designed and analyzed the experiment to make a data-driven recommendation.

📊 Key Results
| Metric | Value |
|--------|-------|
| Control Conversion Rate | 9.58% |
| Treatment Conversion Rate | 11.34% |
| Relative Uplift | +18.4% |
| P-value | 0.0040 |
| Statistical Significance | ✅ Yes (p < 0.05) |
| Monthly Impact (1M users) | +17,600 purchases |

✅ Recommendation
**Launch the new button.** The result is statistically significant with 
99.6% confidence. At 1 million monthly visitors this generates 17,600 
additional purchases per month.

🗂️ Project Structure
```
AB_testing_project/
├── data/
│   ├── raw/              # Original simulated data
│   └── processed/        # Cleaned data with engineered features
├── notebooks/
│   ├── 01_data_generation.ipynb
│   ├── 02_exploratory_analysis.ipynb
│   ├── 03_statistical_testing.ipynb
│   └── 04_results_business_report.ipynb
├── src/
│   ├── data_generator.py  # Reusable data generation functions
│   ├── stats_tests.py     # Reusable statistical testing functions
│   └── visualizations.py  # Reusable plotting functions
├── reports/
│   └── figures/           # All saved charts
└── README.md
```

🛠️ Technologies Used
- **Python** — core programming language
- **Pandas & Numpy** — data manipulation and simulation
- **Scipy & Statsmodels** — statistical testing
- **Matplotlib & Seaborn** — data visualization
- **Jupyter Notebook** — analysis and reporting

🚀 How To Run
1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run notebooks in order: 01 → 02 → 03 → 04

📦 Requirements
See `requirements.txt` for full list of dependencies.

Author
Zubiya Shaikh — Data Analyst