import pandas as pd

def transform_data(file_path):
    df = pd.read_csv(file_path)

    print("Original Data Shape:", df.shape)

    # Standardize column names
    df.columns = [col.strip().lower().replace(" ", "_").replace("-", "_") for col in df.columns]

    # Drop duplicate claims
    df = df.drop_duplicates(subset=["claim_id"])

    # Convert dates
    df["date_of_service"] = pd.to_datetime(df["date_of_service"], errors="coerce")

    # Convert numeric columns
    numeric_cols = ["billed_amount", "allowed_amount", "paid_amount"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Clean text columns
    text_cols = [
        "provider_id", "patient_id", "procedure_code", "diagnosis_code",
        "insurance_type", "claim_status", "reason_code",
        "follow_up_required", "ar_status", "outcome"
    ]

    for col in text_cols:
        df[col] = df[col].astype(str).str.strip()

    # Fill missing values
    df["reason_code"] = df["reason_code"].fillna("UNKNOWN")
    df["follow_up_required"] = df["follow_up_required"].fillna("No")
    df["outcome"] = df["outcome"].fillna("Pending")

    print("Transformed Data Shape:", df.shape)

    return df
