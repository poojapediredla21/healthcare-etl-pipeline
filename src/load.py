import sqlite3

def load_data(df, db_name="healthcare.db", table_name="claims"):
    if df is None:
        print("No data to load")
        return

    try:
        conn = sqlite3.connect(db_name)
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        conn.close()
        print(f"Data loaded successfully into {table_name} table")
    except Exception as e:
        print(f"Error during loading: {e}")
