import pandas as pd

files = [
    "01_fund_master.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in files:
    df = pd.read_csv("data/raw/" + file)

    df = df.drop_duplicates()

    df = df.dropna(how="all")

    df.columns = df.columns.str.strip()

    df = df.fillna("unknown")

    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = df[col].astype(str).str.strip()

    df = df.drop_duplicates()

    name = file.replace(".csv", "_cleaned.csv")

    df.to_csv("data/processed/" + name, index=False)

print("done")