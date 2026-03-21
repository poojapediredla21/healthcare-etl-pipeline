from transform import transform_data
from model_data import create_dimensions_and_fact
from load import load_dataframes_to_sqlite, save_to_csv

def run_pipeline():
    file_path = "data/raw/claim_data.csv"

    # Transform
    df_clean = transform_data(file_path)

    # Model into dimensions + fact
    modeled_data = create_dimensions_and_fact(df_clean)

    # Load into SQLite
    load_dataframes_to_sqlite(modeled_data)

    # Save CSVs for Power BI
    save_to_csv(modeled_data)

if __name__ == "__main__":
    run_pipeline()
