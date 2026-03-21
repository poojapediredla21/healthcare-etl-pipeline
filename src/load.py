import sqlite3

def load_dataframes_to_sqlite(dataframes, db_name="healthcare.db"):
    try:
        conn = sqlite3.connect(db_name)

        for table_name, df in dataframes.items():
            df.to_sql(table_name, conn, if_exists="replace", index=False)
            print(f"Loaded {table_name} with {len(df)} rows")

        conn.close()
        print("All tables loaded successfully into SQLite")

    except Exception as e:
        print(f"Error during loading: {e}")
