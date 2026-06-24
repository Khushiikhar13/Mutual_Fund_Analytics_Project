import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

df = df.drop_duplicates()

df["date"] = pd.to_datetime(df["date"], errors="coerce")
df = df.dropna(subset=["date"])

df["nav"] = pd.to_numeric(df["nav"], errors="coerce")

df = df.sort_values(["amfi_code", "date"])

df["nav"] = df.groupby("amfi_code")["nav"].ffill()

df = df.dropna(subset=["nav"])

df = df[df["nav"] > 0]

df = df.drop_duplicates()

df = df.reset_index(drop=True)

df.to_csv("data/processed/02_nav_history_cleaned.csv", index=False)

print("done")