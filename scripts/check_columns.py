import pandas as pd

nav = pd.read_csv("data/processed/02_nav_history_cleaned.csv")
print("NAV Columns:")
print(nav.columns.tolist())

print()

txn = pd.read_csv("data/processed/08_investor_transactions_cleaned.csv")
print("Transaction Columns:")
print(txn.columns.tolist())