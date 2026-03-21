import pandas as pd

def transform_data(df):
    if df is None:
        print("No data to transform")
        return None

    # Drop duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df = df.fillna(method='ffill')

    # Standardize column names
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    print("Data transformed successfully")
    return df
