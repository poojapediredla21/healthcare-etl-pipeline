def create_dimensions_and_fact(df):
    # Dimension tables
    dim_provider = df[["provider_id"]].drop_duplicates().reset_index(drop=True)

    dim_patient = df[["patient_id"]].drop_duplicates().reset_index(drop=True)

    dim_procedure = df[["procedure_code"]].drop_duplicates().reset_index(drop=True)

    dim_diagnosis = df[["diagnosis_code"]].drop_duplicates().reset_index(drop=True)

    dim_insurance = df[["insurance_type"]].drop_duplicates().reset_index(drop=True)

    dim_date = df[["date_of_service"]].drop_duplicates().reset_index(drop=True)
    dim_date["year"] = dim_date["date_of_service"].dt.year
    dim_date["month"] = dim_date["date_of_service"].dt.month
    dim_date["day"] = dim_date["date_of_service"].dt.day

    # Fact table
    fact_claims = df[[
        "claim_id", "provider_id", "patient_id", "procedure_code", "diagnosis_code",
        "insurance_type", "date_of_service", "billed_amount", "allowed_amount",
        "paid_amount", "claim_status", "reason_code", "follow_up_required",
        "ar_status", "outcome"
    ]].copy()

    return {
        "dim_provider": dim_provider,
        "dim_patient": dim_patient,
        "dim_procedure": dim_procedure,
        "dim_diagnosis": dim_diagnosis,
        "dim_insurance": dim_insurance,
        "dim_date": dim_date,
        "fact_claims": fact_claims
    }
