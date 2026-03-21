from extract import extract_data
from transform import transform_data
from load import load_data

def run_pipeline():
    file_path = "data/raw/cases_deaths.csv"

    # Step 1: Extract
    df = extract_data(file_path)

    # Step 2: Transform
    df_clean = transform_data(df)

    # Step 3: Load
    load_data(df_clean)

if __name__ == "__main__":
    run_pipeline()
