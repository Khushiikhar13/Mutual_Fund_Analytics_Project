import pandas as pd
from sqlalchemy import create_engine

print("Creating SQLite Database...")

engine = create_engine("sqlite:///bluestock_mf.db")

# Load cleaned datasets

nav_df = pd.read_csv(
    "data/processed/02_nav_history_cleaned.csv"
)

transactions_df = pd.read_csv(
    "data/processed/08_investor_transactions_cleaned.csv"
)

performance_df = pd.read_csv(
    "data/processed/07_scheme_performance_cleaned.csv"
)

# Save to SQLite

nav_df.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

transactions_df.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

performance_df.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("Database Created Successfully!")