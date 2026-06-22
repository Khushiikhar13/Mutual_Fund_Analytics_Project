# 📊 Bluestock Fintech - Mutual Fund Analytics Project

This project is a complete end-to-end financial data analytics system built to analyze mutual fund datasets using Python. It simulates a real-world data engineering workflow including data ingestion, transformation, validation, and financial analysis.

The objective of this project is to process mutual fund data and generate meaningful insights related to NAV trends, fund performance, risk metrics, SIP inflows, and investor behavior.

---

## 🎯 Project Objectives

- Build an end-to-end ETL pipeline for financial data processing
- Analyze mutual fund NAV trends and performance
- Validate datasets using AMFI scheme codes
- Perform risk-return analysis using financial metrics
- Study SIP inflows and investor behavior patterns
- Generate structured insights for analysis and reporting

---

## 📁 Project Structure

bluestock_mf_capstone/
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
├── scripts/
│   ├── data_ingestion.py
│   ├── live_nav_fetch.py
│   ├── data_validation.py
│   └── fund_analysis.py
├── notebooks/
├── reports/
├── requirements.txt
└── README.md

---

## 📊 Datasets Used

- fund_master.csv → Mutual fund scheme details (AMC, category, risk, expense ratio)
- nav_history.csv → Historical NAV values of mutual funds
- sip_inflows.csv → SIP investment flow data
- investor_transactions.csv → Transaction records (SIP, lumpsum, redemption)
- scheme_performance.csv → Financial metrics (returns, CAGR, Sharpe ratio, Alpha, Beta)

---

## 🔄 ETL Pipeline

### Extract
- Data loaded from CSV files
- Live NAV data fetched using external API (mfapi.in)

### Transform
- Handling missing values and duplicates
- Data cleaning and formatting
- Standardization of AMFI scheme codes

### Load
- Processed data stored in structured folders
- Optional SQLite database integration for querying

---

## ✔ Data Validation

- Matching records between fund_master and nav_history using AMFI codes
- Ensuring data consistency across datasets
- Removing invalid or mismatched entries
- Maintaining data integrity for financial accuracy

---

## 📈 Analysis Performed

- NAV trend analysis over time
- Fund category-wise comparison
- Risk vs return analysis (Sharpe ratio, Alpha, Beta)
- SIP inflow trend analysis
- Investor behavior analysis
- Fund performance benchmarking

---

## 🧰 Technologies Used

Python, Pandas, NumPy, Requests, SQLite, Matplotlib, Seaborn, Git, GitHub, Power BI, SQL

---

## ▶ How to Run

Install dependencies:

pip install -r requirements.txt

Run scripts:

python scripts/data_ingestion.py  
python scripts/live_nav_fetch.py  
python scripts/data_validation.py  
python scripts/fund_analysis.py  

---

## 📌 Key Outcomes

- End-to-end financial data pipeline implemented
- Live NAV data integrated using API
- Dataset validation using AMFI codes
- Mutual fund performance analysis completed
- Risk and return insights generated
- Structured analytics workflow built for financial data

---

## 👨‍💻 Author

Bluestock Fintech - Mutual Fund Anlaytics Project