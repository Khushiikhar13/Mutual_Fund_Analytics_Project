import pandas as pd

df = pd.read_csv("data/raw/07_scheme_performance.csv")

df = df.drop_duplicates()
df = df.dropna(how="all")

df.columns = df.columns.str.strip()

df = df.fillna("unknown")

df["scheme_name"] = df["scheme_name"].astype(str).str.strip()
df["fund_house"] = df["fund_house"].astype(str).str.strip()
df["category"] = df["category"].astype(str).str.strip()

df["return_1yr_pct"] = pd.to_numeric(df["return_1yr_pct"], errors="coerce")
df["return_3yr_pct"] = pd.to_numeric(df["return_3yr_pct"], errors="coerce")
df["return_5yr_pct"] = pd.to_numeric(df["return_5yr_pct"], errors="coerce")
df["aum_crore"] = pd.to_numeric(df["aum_crore"], errors="coerce")
df["expense_ratio_pct"] = pd.to_numeric(df["expense_ratio_pct"], errors="coerce")

df = df.dropna(subset=["return_1yr_pct"])
df = df.dropna(subset=["aum_crore"])

df = df[df["aum_crore"] > 0]
df = df[df["expense_ratio_pct"] < 2.5]

df = df.drop_duplicates()

df.to_csv("data/processed/07_scheme_performance_cleaned.csv", index=False)

print("done")