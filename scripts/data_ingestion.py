import pandas as pd
from pathlib import Path

data_folder = Path("data/raw")

csv_files = data_folder.glob("*.csv")

for file in csv_files:
    print("\n" + "=" * 50)
    print("FILE:", file.name)

    df = pd.read_csv(file)

    print("Shape:", df.shape)
    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())